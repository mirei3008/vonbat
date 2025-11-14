from django import forms

# 求人検索・並び替え用フォームの定義
# ユーザーがキーワードで求人を検索したり、並び順を選択できるようにする

class SearchSortForm(forms.Form):
    # 検索キーワード入力欄（未入力でもOK）
    q = forms.CharField(label="キーワード", required=False)

    # 並び順の選択肢（新着順・古い順・職種名順・会社名順）
    SORT_CHOICES = [
        ("new", "新着順"),      # 投稿日の新しい順
        ("old", "古い順"),      # 投稿日の古い順
        ("title", "職種名 A→Z"), # 職種名の昇順
        ("company", "会社名 A→Z"), # 会社名の昇順
    ]
    # 並び順選択欄（未選択でもOK）
    sort = forms.ChoiceField(label="並び順", choices=SORT_CHOICES, required=False)
