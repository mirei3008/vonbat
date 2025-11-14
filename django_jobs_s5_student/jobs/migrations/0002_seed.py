from django.db import migrations

def seed_jobs(apps, schema_editor):
    Job = apps.get_model('jobs', 'Job')
    data = [
        ("バックエンドエンジニア", "Acme Tech", "東京", "Django/API開発、RDB設計"),
        ("フロントエンドエンジニア", "Beta Soft", "横浜", "React/TypeScript"),
        ("データエンジニア", "Cloud Nine", "札幌", "ETL/BigQuery"),
        ("SRE", "Delta Ops", "大阪", "監視/インフラ自動化"),
        ("QAエンジニア", "Echo Quality", "名古屋", "E2Eテスト/自動化"),
        ("PM", "Foxtrot Works", "福岡", "要件定義/進行管理"),
        ("UI/UXデザイナ", "Gamma Design", "東京", "ユーザ調査/プロトタイピング"),
        ("モバイルエンジニア", "Helios Mobile", "仙台", "Kotlin/Swift"),
        ("セキュリティエンジニア", "Iota Secure", "東京", "脆弱性診断/対策"),
        ("機械学習エンジニア", "Juno AI", "京都", "推論/学習パイプライン"),
        ("テクニカルサポート", "Kappa Support", "神戸", "顧客対応/トラブルシュート"),
        ("社内SE", "Lumos Corp", "新潟", "社内システム運用"),
        ("フルスタック", "Mimir Lab", "東京", "Django/React"),
        ("バックエンド", "Nexus Tech", "福岡", "API/性能改善"),
        ("IoTエンジニア", "Orion Devices", "金沢", "組込み/クラウド"),
        ("ゲームサーバ", "Pixel Play", "札幌", "低レイテンシ/スケール"),
        ("テスト自動化", "Quanta QA", "広島", "pytest/CI"),
        ("DevRel", "Relay Dev", "東京", "コミュニティ/ドキュメント"),
        ("CS", "Sigma Care", "横浜", "ユーザー支援"),
        ("データアナリスト", "Titan Data", "仙台", "可視化/SQL"),
        ("クラウドアーキテクト", "Umbra Cloud", "大阪", "AWS/設計"),
        ("R&Dエンジニア", "Vega Labs", "京都", "PoC/検証"),
        ("Djangoエンジニア", "Webify", "東京", "CRM開発"),
        ("サーバーサイド", "Xenon", "名古屋", "高負荷対策"),
        ("ヘルプデスク", "Yotta Help", "福岡", "一次対応"),
        ("プロダクトマネージャ", "Zenith", "東京", "ロードマップ"),
    ]
    for t,c,l,d in data:
        Job.objects.create(title=t, company=c, location=l, description=d)

def unseed_jobs(apps, schema_editor):
    Job = apps.get_model('jobs', 'Job')
    Job.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [("jobs","0001_initial")]
    operations = [migrations.RunPython(seed_jobs, reverse_code=unseed_jobs)]
