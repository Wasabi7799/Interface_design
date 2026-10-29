"""資料驅動的 CL Taipei 分類與原型貼文資料。"""

MAIN_CATEGORIES = (
    ("community", "community", "社群", "👥"),
    ("housing", "housing", "住居", "🏠"),
    ("services", "services", "服務", "🛠️"),
    ("autos", "autos", "汽機車", "🚗"),
    ("discussion-forums", "discussion forums", "討論區", "💬"),
    ("for-sale", "for sale", "出售", "🛍️"),
    ("jobs", "jobs", "工作", "💼"),
    ("gigs", "gigs", "接案", "✨"),
)

# 一張正規化的資料表；畫面依 parent_slug 分組，而非各頁複製分類清單。
_ROWS = """
community|activities|activities|活動
community|artists|artists|藝術家
community|childcare|childcare|托育
community|general|general|綜合
community|groups|groups|社團
community|local-news|local news|地方新聞
community|lost-found|lost+found|失物招領
community|missed-connections|missed connections|尋人啟事
community|musicians|musicians|樂手
community|pets|pets|寵物
community|politics|politics|政治
community|rants-raves|rant+raves|抱怨與讚美
community|rideshare|rideshare|共乘
community|volunteers|volunteers|志工
housing|apts-housing|apartments / housing for rent|公寓出租
housing|housing-swap|housing swap|住宅交換
housing|housing-wanted|housing wanted|徵屋
housing|office-commercial|office / commercial|商用空間
housing|parking-storage|parking + storage|車位／倉儲
housing|real-estate-sale|real estate for sale|房地產出售
housing|rooms-shared|rooms / shared|分租雅房
housing|sublets-temporary|sublets / temporary|短期轉租
housing|vacation-rentals|vacation rentals|度假短租
services|automotive|automotive|汽車服務
services|beauty|beauty|美容
services|cell-mobile|cell / mobile|手機
services|computer|computer|電腦
services|creative|creative|創意設計
services|cycle|cycle|自行車
services|event|event|活動
services|farm-garden|farm + garden|農園藝
services|financial|financial|財務
services|health-wellness|health / wellness|健康
services|household|household|家事
services|labor-move|labor / move|搬運
services|legal|legal|法律
services|lessons|lessons|家教
services|marine|marine|船舶
services|pet|pet|寵物
services|real-estate|real estate|房地產
services|skilled-trade|skilled trade|專業技工
services|smb-advertising|small business ads|小型商家廣告
services|tax|tax|稅務
services|tech|tech|科技
services|travel-vacation|travel / vacation|旅遊
services|writing-editing|writing / editing|寫作編輯
autos|cars-trucks|cars + trucks|轎車／貨車
autos|motorcycles-scooters|motorcycles / scooters|機車／速克達
autos|rvs|RVs|露營車
autos|trailers|trailers|拖車
autos|auto-parts|auto parts|汽車零件
autos|wheels-tires|auto wheels & tires|輪胎／輪框
autos|aviation|aviation|航空
autos|boats|boats|船隻
autos|boat-parts|boat parts|船用零件
autos|bikes|bikes|自行車
autos|commercial-trucks|commercial trucks|商用卡車
autos|heavy-equipment|heavy equipment|重型機具
discussion-forums|general|general discussion|一般討論
discussion-forums|housing|housing|租屋經驗
discussion-forums|transport|transport|交通
discussion-forums|living|living in Taipei|台北生活
discussion-forums|buy-sell|buy & sell|買賣交流
for-sale|antiques|antiques|古董
for-sale|appliances|appliances|家電
for-sale|arts-crafts|arts + crafts|工藝
for-sale|atv-utv-snow|ATV / UTV / snow|越野車
for-sale|auto-parts|auto parts|汽車零件
for-sale|baby-kids|baby + kids|嬰幼童
for-sale|barter|barter|以物易物
for-sale|beauty-health|beauty + health|美妝保健
for-sale|bike-parts|bike parts|自行車零件
for-sale|bikes|bikes|自行車
for-sale|boat-parts|boat parts|船用零件
for-sale|boats|boats|船隻
for-sale|books|books|書籍
for-sale|business|business|商業設備
for-sale|cars-trucks|cars + trucks|轎車／貨車
for-sale|cds-dvd-vhs|CDs / DVDs / VHS|影音
for-sale|cell-phones|cell phones|手機
for-sale|clothes-accessories|clothes + accessories|服飾配件
for-sale|collectibles|collectibles|收藏品
for-sale|computer-parts|computer parts|電腦零件
for-sale|computers|computers|電腦
for-sale|electronics|electronics|電子產品
for-sale|farm-garden|farm + garden|農園藝
for-sale|free|free|免費
for-sale|furniture|furniture|家具
for-sale|garage-sale|garage sale|車庫拍賣
for-sale|general|general|綜合
for-sale|heavy-equipment|heavy equipment|重型機具
for-sale|household|household|居家用品
for-sale|jewelry|jewelry|珠寶
for-sale|materials|materials|建材
for-sale|motorcycles|motorcycles|機車
for-sale|music-instruments|musical instruments|樂器
for-sale|photo-video|photo + video|攝影器材
for-sale|rvs|RVs|露營車
for-sale|sporting|sporting goods|運動用品
for-sale|tickets|tickets|票券
for-sale|tools|tools|工具
for-sale|toys-games|toys + games|玩具
for-sale|trailers|trailers|拖車
for-sale|video-gaming|video gaming|電玩
for-sale|wanted|wanted|徵求
jobs|accounting-finance|accounting + finance|會計財務
jobs|admin-office|admin / office|行政
jobs|arch-engineering|arch / engineering|建築工程
jobs|art-media-design|art / media / design|藝術媒體設計
jobs|business-management|business / management|商業管理
jobs|customer-service|customer service|客服
jobs|education|education|教育
jobs|energy|energy|能源
jobs|engineering|engineering|工程
jobs|food-beverage-hospitality|food / beverage / hospitality|餐飲旅宿
jobs|general-labor|general labor|一般勞動
jobs|government|government|政府
jobs|healthcare|healthcare|醫療
jobs|human-resources|human resources|人資
jobs|legal-paralegal|legal / paralegal|法律
jobs|manufacturing|manufacturing|製造
jobs|marketing-advertising|marketing / advertising|行銷廣告
jobs|nonprofit|nonprofit|非營利
jobs|real-estate|real estate|房地產
jobs|retail-wholesale|retail / wholesale|零售批發
jobs|sales|sales|業務
jobs|salon-spa-fitness|salon / spa / fitness|美髮健身
jobs|science-biotech|science / biotech|科學生技
jobs|security|security|保全
jobs|skilled-trade-artisan|skilled trade / artisan|技工
jobs|software-qa-dba|software / QA / DBA|軟體
jobs|systems-networking|systems / networking|系統網路
jobs|technical-support|technical support|技術支援
jobs|transport|transport|運輸
jobs|tv-film-video|TV / film / video|影視
jobs|web-design|web / HTML / info design|網頁設計
jobs|writing-editing|writing / editing|寫作編輯
gigs|computer-gigs|computer gigs|電腦接案
gigs|creative-gigs|creative gigs|創意接案
gigs|crew-gigs|crew gigs|團隊接案
gigs|domestic-gigs|domestic gigs|家事接案
gigs|event-gigs|event gigs|活動接案
gigs|labor-gigs|labor gigs|勞動接案
gigs|talent-gigs|talent gigs|才藝接案
gigs|writing-gigs|writing gigs|寫作接案
"""

CATEGORIES = tuple(
    {
        "parent_slug": parent,
        "slug": slug,
        "name_en": name_en,
        "name_zh": name_zh,
        "sort_order": order,
        "icon": "•",
    }
    for order, line in enumerate(_ROWS.strip().splitlines())
    for parent, slug, name_en, name_zh in [line.split("|")]
)

DISTRICTS = ("中正區", "大安區", "信義區", "松山區", "中山區", "士林區", "北投區")

MOCK_LISTINGS = (
    {"id": "1001", "category": "housing", "sub": "apts-housing", "title": "近捷運站採光兩房", "price": 28500, "district": "大安區", "created": "2026-10-28", "status": "active", "seller": "Taipei Home", "description": "步行五分鐘到捷運站，家具齊全，歡迎預約看屋。", "views": 86},
    {"id": "1002", "category": "for-sale", "sub": "furniture", "title": "北歐風實木書桌", "price": 3200, "district": "中山區", "created": "2026-10-27", "status": "active", "seller": "Lin", "description": "保存良好，自取優先。", "views": 42},
    {"id": "1003", "category": "jobs", "sub": "software-qa-dba", "title": "Python 後端工程師", "price": 65000, "district": "信義區", "created": "2026-10-26", "status": "active", "seller": "Open Studio", "description": "尋找熟悉 Python 與 PostgreSQL 的夥伴。", "views": 125},
    {"id": "1004", "category": "services", "sub": "lessons", "title": "一對一中文與英文家教", "price": 800, "district": "士林區", "created": "2026-10-25", "status": "active", "seller": "Mia", "description": "可線上或面授，依程度安排課程。", "views": 31},
    {"id": "1005", "category": "autos", "sub": "motorcycles-scooters", "title": "通勤速克達 125", "price": 38000, "district": "松山區", "created": "2026-10-22", "status": "sold", "seller": "Ken", "description": "定期保養，里程低。", "views": 203},
    {"id": "1006", "category": "community", "sub": "activities", "title": "週末大安森林公園慢跑團", "price": None, "district": "大安區", "created": "2026-10-21", "status": "active", "seller": "Run Taipei", "description": "新手友善，週六早上集合。", "views": 68},
)
