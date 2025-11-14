from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Job
from .forms import SearchSortForm

def home(request):
    return render(request, "home.html")

class JobList(ListView):
    model = Job
    paginate_by = 10

    SORT_MAP = {
        "new": ("-posted_at", "-id"),
        "old": ("posted_at", "id"),
        "title": ("title", "id"),
        "company": ("company", "id"),
    }

    def get_queryset(self):
        """
        求人リストの取得と検索/ソート機能を提供するメソッド
        
        Returns:
            QuerySet: フィルタリングとソートが適用された求人のクエリセット
        """
        # 基本の求人リストを取得
        qs = super().get_queryset()
        
        # 検索フォームを初期化（GETパラメータから）
        self.form = SearchSortForm(self.request.GET or None)
        
        if self.form.is_valid():
            # 検索キーワードを取得（空文字の場合は""）
            q = (self.form.cleaned_data.get("q") or "").strip()
            # ソート条件を取得（デフォルトは"new"）
            sort = self.form.cleaned_data.get("sort") or "new"

            # キーワードをスペースで分割し、空でない単語のリストを作成
            words = [w for w in q.split() if w]
            
            # 各キーワードでAND検索を実行
            # 各キーワードについて、title/company/location/descriptionのいずれかに
            # 部分一致（大文字小文字区別なし）するものを検索
            for w in words:
                qs = qs.filter(
                    Q(title__icontains=w) |      # タイトルに含まれる
                    Q(company__icontains=w) |     # 会社名に含まれる
                    Q(location__icontains=w) |    # 勤務地に含まれる
                    Q(description__icontains=w)   # 説明文に含まれる
                )

            # ソート順を適用（存在しない場合は"new"の順序を使用）
            order = self.SORT_MAP.get(sort, self.SORT_MAP["new"])
            qs = qs.order_by(*order)
        return qs


    def get_context_data(self, **kwargs):
        """
        テンプレートに渡すコンテキストデータを生成するメソッド
        
        Args:
            **kwargs: 親クラスに渡す追加の引数
        
        Returns:
            dict: テンプレートで使用するコンテキストデータ
        """
        # 親クラスのコンテキストデータを取得
        ctx = super().get_context_data(**kwargs)
        
        # 検索フォームをコンテキストに追加
        # self.formが存在しない場合は新しいフォームを作成
        ctx["form"] = getattr(self, "form", SearchSortForm())

        # ページネーションのために現在のGETパラメータを処理
        qd = self.request.GET.copy()  # GETパラメータのコピーを作成
        qd.pop("page", True)          # pageパラメータを削除（ページ切り替え時に維持しない）
        ctx["qparams"] = qd.urlencode()  # 残りのパラメータをURLエンコード

        # 検索結果の総件数を取得
        ctx["total_count"] = self.get_queryset().count()
        return ctx

class JobDetail(DetailView):
    model = Job
