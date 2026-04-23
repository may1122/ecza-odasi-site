import os
import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================================
# SAYFA AYARI
# =========================================================
st.set_page_config(
    page_title="AYÇA | Akıllı Yazılım Çözüm Asistanı",
    page_icon="💊",
    layout="wide"
)

# =========================================================
# SABİTLER
# =========================================================
aylar_tr = {
    1: "Ocak",
    2: "Şubat",
    3: "Mart",
    4: "Nisan",
    5: "Mayıs",
    6: "Haziran",
    7: "Temmuz",
    8: "Ağustos",
    9: "Eylül",
    10: "Ekim",
    11: "Kasım",
    12: "Aralık"
}

gun_sira = ["Pzt", "Salı", "Çarş", "Perş", "Cuma", "Ctesi", "Pazar"]

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>
:root{
  --bg:#f6f8fb;
  --surface:#ffffff;
  --primary:#1f4b99;
  --primary2:#2e6bdb;
  --text:#1b2430;
  --muted:#5e6b7a;
  --line:#dbe3ee;
  --accent:#e9f1ff;
  --green:#22a06b;
  --red:#d92d20;
  --purple:#8754d9;
  --soft-red:#fff1f0;
  --soft-green:#eefbf4;
  --soft-blue:#eef4ff;
  --soft-purple:#f4efff;
  --shadow:0 16px 40px rgba(22,34,51,.08);
  --radius:22px;
}

html, body, [class*="css"] {
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
}

.stApp {
  background: linear-gradient(180deg,#f9fbff 0%, #f3f6fb 100%);
}

header[data-testid="stHeader"] {
  background: rgba(0,0,0,0);
}

.block-container {
  padding-top: 1.8rem;
  padding-bottom: 2rem;
  max-width: 1280px;
}

section[data-testid="stSidebar"] {
  background: #ffffff;
  border-right: 1px solid var(--line);
  min-width: 300px !important;
  max-width: 300px !important;
}

section[data-testid="stSidebar"] > div {
  min-width: 300px !important;
  max-width: 300px !important;
}

.sidebar-logo img {
  width: 240px !important;
  display: block;
  margin-left: auto;
  margin-right: auto;
  margin-top: 10px;
  margin-bottom: 10px;
}

.brand-text{
  font-size:28px;
  font-weight:800;
  color:var(--text);
  letter-spacing:-0.02em;
}

.brand-sub{
  color:var(--muted);
  font-size:14px;
  margin-top:2px;
}

.top-divider{
  border-top:1px solid var(--line);
  margin:18px 0 26px 0;
}

.hero-box{
  background: transparent;
  border: none;
  border-radius: 0;
  padding: 0 8px 0 0;
  box-shadow: none;
  margin-bottom: 18px;
}

.eyebrow{
  display:inline-block;
  background:var(--accent);
  color:var(--primary);
  border:1px solid #cfe0ff;
  border-radius:999px;
  padding:10px 14px;
  font-size:14px;
  font-weight:700;
  margin-bottom:18px;
}

.hero-title{
  font-size:62px;
  line-height:1.06;
  letter-spacing:-0.04em;
  font-weight:800;
  color:var(--text);
  margin-bottom:18px;
}

.hero-title .blue { color: var(--primary2); }
.hero-title .green { color: var(--green); }

.hero-sub{
  color:var(--muted);
  font-size:19px;
  line-height:1.7;
  max-width:760px;
}

.section-title{
  font-size:32px;
  font-weight:800;
  color:var(--text);
  letter-spacing:-0.02em;
  margin: 22px 0 8px 0;
}

.section-sub{
  color:var(--muted);
  line-height:1.75;
  margin-bottom:18px;
}

.card{
  background:var(--surface);
  border:1px solid var(--line);
  border-radius:24px;
  padding:22px;
  box-shadow:var(--shadow);
  height:100%;
}

.card h3{
  margin:0 0 10px 0;
  color:var(--text);
  font-size:22px;
  font-weight:800;
}

.card p{
  margin:0;
  color:var(--muted);
  line-height:1.7;
}

.metric-card{
  background:rgba(255,255,255,.96);
  border:1px solid var(--line);
  border-radius:22px;
  padding:18px 18px;
  box-shadow:var(--shadow);
  height:100%;
}

.metric-value{
  font-size:28px;
  font-weight:800;
  color:var(--text);
  margin-bottom:8px;
}

.metric-label{
  font-size:15px;
  color:var(--muted);
  line-height:1.6;
}

.step-card{
  background:#ffffff;
  border:1px solid var(--line);
  border-radius:28px;
  box-shadow:var(--shadow);
  padding:28px 24px;
}

.step-num{
  width:58px;
  height:58px;
  border-radius:18px;
  background:#eef4ff;
  color:var(--primary2);
  display:flex;
  align-items:center;
  justify-content:center;
  font-weight:800;
  font-size:28px;
  margin:0 auto 14px auto;
}

.step-title{
  text-align:center;
  font-size:18px;
  font-weight:800;
  color:var(--text);
  margin-bottom:6px;
}

.step-text{
  text-align:center;
  color:var(--muted);
  line-height:1.7;
  font-size:15px;
}

.cta-box{
  background:linear-gradient(180deg,#eef4ff 0%, #ffffff 100%);
  border:1px solid #d6e4ff;
  border-radius:28px;
  box-shadow:var(--shadow);
  padding:24px 26px;
  margin-top:14px;
}

.main-title {
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--text);
  margin-top: 0.2rem;
  margin-bottom: 0.35rem;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.main-subtitle {
  color: var(--muted);
  font-size: 1rem;
  margin-bottom: 1.2rem;
}

.metric-mini{
  background:#ffffff;
  border:1px solid var(--line);
  border-radius:18px;
  padding:14px 16px;
  box-shadow:var(--shadow);
  height:100%;
}

.metric-mini .label{
  color:var(--muted);
  font-size:0.9rem;
  margin-bottom:6px;
  font-weight:600;
}

.metric-mini .value{
  color:var(--text);
  font-size:1.8rem;
  font-weight:800;
}

.small-note {
  color: var(--muted);
  font-size: 0.9rem;
}

.video-wrap {
  background: #ffffff;
  border: 1px solid var(--line);
  border-radius: 26px;
  padding: 10px;
  box-shadow: var(--shadow);
  margin-top: 10px;
  overflow: hidden;
}

.info-list-card{
  background:#ffffff;
  border:1px solid var(--line);
  border-radius:24px;
  box-shadow:var(--shadow);
  padding:20px 22px;
  margin-bottom:16px;
}

.info-list-head{
  display:flex;
  align-items:flex-start;
  gap:16px;
}

.info-icon{
  width:64px;
  height:64px;
  min-width:64px;
  border-radius:20px;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:30px;
  font-weight:700;
}

.info-icon.red{ background:var(--soft-red); }
.info-icon.green{ background:var(--soft-green); }
.info-icon.blue{ background:var(--soft-blue); }
.info-icon.purple{ background:var(--soft-purple); }

.info-title{
  font-size:22px;
  font-weight:800;
  margin-bottom:8px;
  color:var(--text);
}

.info-title.red{ color:var(--red); }
.info-title.green{ color:var(--green); }
.info-title.blue{ color:var(--primary2); }
.info-title.purple{ color:var(--purple); }

.info-list{
  margin:0;
  padding-left:20px;
}

.info-list li{
  color:var(--muted);
  margin-bottom:10px;
  line-height:1.6;
  font-size:16px;
}

.metric-strip{
  background:#ffffff;
  border:1px solid var(--line);
  border-radius:24px;
  box-shadow:var(--shadow);
  padding:18px 10px;
}

.metric-feature{
  display:flex;
  gap:14px;
  align-items:flex-start;
  padding:10px 14px;
}

.metric-feature-icon{
  width:52px;
  height:52px;
  min-width:52px;
  border-radius:18px;
  display:flex;
  align-items:center;
  justify-content:center;
  font-size:24px;
  background:#eef4ff;
}

.metric-feature-title{
  font-size:18px;
  font-weight:800;
  color:var(--text);
  margin-bottom:4px;
}

.metric-feature-text{
  color:var(--muted);
  line-height:1.6;
  font-size:15px;
}

.cta-inline{
  display:flex;
  justify-content:space-between;
  align-items:center;
  gap:18px;
}

.cta-btn{
  display:inline-block;
  background:linear-gradient(135deg, var(--primary), var(--primary2));
  color:#fff !important;
  text-decoration:none;
  padding:14px 22px;
  border-radius:16px;
  font-weight:800;
  font-size:18px;
}

div[data-testid="metric-container"] {
  background: #ffffff;
  border: 1px solid var(--line);
  padding: 14px;
  border-radius: 18px;
  box-shadow: var(--shadow);
}

.stButton > button {
  background: linear-gradient(135deg, var(--primary), var(--primary2));
  color: white;
  border: none;
  border-radius: 12px;
  padding: 0.65rem 1.1rem;
  font-weight: 700;
}

.stSelectbox > div > div,
.stTextInput > div > div > input,
.stDateInput > div > div input {
  border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA
# =========================================================
@st.cache_data
def load_excel(file):
    xls = pd.ExcelFile(file)

    all_data = []
    genel = None

    for sheet in xls.sheet_names:
        df_sheet = pd.read_excel(file, sheet_name=sheet)
        df_sheet = df_sheet.loc[:, ~df_sheet.columns.astype(str).str.contains("^Unnamed")]

        if "GENEL" in sheet.upper():
            genel_cols = [
                "Eczane",
                "Grup",
                "Geçmiş Katsayı",
                "Geçmiş Bayram",
                "Toplam Katsayı",
                "Bayram"
            ]
            mevcut_genel_cols = [c for c in genel_cols if c in df_sheet.columns]
            if len(mevcut_genel_cols) >= 2:
                genel = df_sheet[mevcut_genel_cols].copy()
            continue

        if "Tarih" not in df_sheet.columns or "Gün" not in df_sheet.columns:
            continue

        df_long = df_sheet.melt(
            id_vars=["Tarih", "Gün"],
            var_name="Grup",
            value_name="Eczane"
        )

        df_long = df_long.dropna(subset=["Eczane"]).copy()
        df_long["Tarih"] = pd.to_datetime(df_long["Tarih"], dayfirst=True, errors="coerce")
        df_long = df_long.dropna(subset=["Tarih"]).copy()
        df_long["Ay"] = sheet

        all_data.append(df_long)

    if not all_data:
        return pd.DataFrame(), genel

    df = pd.concat(all_data, ignore_index=True)
    return df, genel

# =========================================================
# HELPERS
# =========================================================
def render_sidebar_logo():
    logo_path = "logo.png"
    if os.path.exists(logo_path):
        st.sidebar.markdown('<div class="sidebar-logo">', unsafe_allow_html=True)
        st.sidebar.image(logo_path)
        st.sidebar.markdown('</div>', unsafe_allow_html=True)
    else:
        st.sidebar.markdown("## AYÇA")
        st.sidebar.caption("Akıllı Yazılım Çözüm Asistanı")

def metric_card(value, label):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">{value}</div>
            <div class="metric-label">{label}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def show_metric_mini(label, value):
    st.markdown(
        f"""
        <div class="metric-mini">
            <div class="label">{label}</div>
            <div class="value">{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

def info_card(title, text):
    st.markdown(
        f"""
        <div class="card">
            <h3>{title}</h3>
            <p>{text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def prepare_ozet_table(df, genel):
    gun_pivot = pd.pivot_table(
        df,
        index=["Eczane", "Grup"],
        columns="Gün",
        aggfunc="size",
        fill_value=0
    ).reset_index()

    mevcut_gunler = [g for g in gun_sira if g in gun_pivot.columns]
    gun_pivot = gun_pivot[["Eczane", "Grup"] + mevcut_gunler]

    if genel is not None and {"Eczane", "Grup"}.issubset(genel.columns):
        ozet = genel.merge(gun_pivot, on=["Eczane", "Grup"], how="left")
    else:
        ozet = gun_pivot.copy()

    for g in gun_sira:
        if g in ozet.columns:
            ozet[g] = ozet[g].fillna(0)

    sabit_kolonlar = [
        "Eczane",
        "Grup",
        "Geçmiş Katsayı",
        "Geçmiş Bayram",
        "Toplam Katsayı",
        "Bayram"
    ]
    mevcut_sabitler = [c for c in sabit_kolonlar if c in ozet.columns]

    return ozet[mevcut_sabitler + mevcut_gunler], mevcut_gunler

# =========================================================
# LANDING
# =========================================================
def show_landing():
    col_logo, col_brand = st.columns([1, 7])
    with col_logo:
        if os.path.exists("logo.png"):
            st.image("logo.png", width=110)
    with col_brand:
        st.markdown('<div class="brand-text">AYÇA</div>', unsafe_allow_html=True)
        st.markdown('<div class="brand-sub">Akıllı Yazılım Çözüm Asistanı</div>', unsafe_allow_html=True)

    st.markdown('<div class="top-divider"></div>', unsafe_allow_html=True)

    col_left, col_right = st.columns([1.25, 0.95], gap="large")

    with col_left:
        st.markdown("""
        <div class="hero-box">
            <div class="eyebrow">🛡️ Eczacı odaları ve nöbet planlama süreçleri için dijital çözüm</div>
            <div class="hero-title">
                Nöbet planlamasını <span class="blue">daha düzenli</span>, <span class="green">daha şeffaf</span> ve daha yönetilebilir hale getirin.
            </div>
            <div class="hero-sub">
                AYÇA; eczane nöbet dağılımı, denge kontrolü, raporlama ve kurumsal sunum süreçlerini tek çatı altında
                sadeleştiren modern bir yazılım çözümüdür.
            </div>
        </div>
        """, unsafe_allow_html=True)

        video_path = "tanitim.mp4"
        if os.path.exists(video_path):
            st.markdown('<div class="video-wrap">', unsafe_allow_html=True)
            st.video(video_path)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("Video bulunamadı. Lütfen proje klasörüne 'tanitim.mp4' dosyasını ekleyin.")

    with col_right:
        st.markdown("""
        <div class="info-list-card">
            <div class="info-list-head">
                <div class="info-icon red">⚠️</div>
                <div style="width:100%;">
                    <div class="info-title red">Sorunlar</div>
                    <ul class="info-list">
                        <li>Excel tabanlı planlamalarda hata ve tutarsızlık riski yüksektir.</li>
                        <li>Denge kontrolü ve kısıt ihlalleri çoğu zaman geç fark edilir.</li>
                        <li>Raporlama süreci dağınık ilerler ve zaman kaybettirir.</li>
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-list-card">
            <div class="info-list-head">
                <div class="info-icon green">✅</div>
                <div style="width:100%;">
                    <div class="info-title green">AYÇA’nın Çözümü</div>
                    <ul class="info-list">
                        <li>Verileri hızlıca alır, kurallara göre kontrol eder.</li>
                        <li>Denge, çakışma ve kritik ihlalleri görünür hale getirir.</li>
                        <li>Anlaşılır raporlar ve güçlü özet tablolar üretir.</li>
                        <li>Tüm süreci tek bir panelde sadeleştirir.</li>
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-list-card">
            <div class="info-list-head">
                <div class="info-icon blue">⭐</div>
                <div style="width:100%;">
                    <div class="info-title blue">Neden AYÇA?</div>
                    <ul class="info-list">
                        <li>Kullanımı kolay, sade ve modern arayüz</li>
                        <li>Kuruma özel kural ve denge yönetimi</li>
                        <li>Şeffaf, açıklanabilir ve güvenilir sonuçlar</li>
                        <li>Yönetim ve paydaşlar için profesyonel çıktılar</li>
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="cta-box">
            <div class="cta-inline">
                <div>
                    <div class="info-title purple" style="margin-bottom:6px;">Hemen deneyin</div>
                    <div style="color:var(--muted); line-height:1.7; font-size:16px;">
                        Panel sekmesine geçerek AYÇA’nın canlı kullanımını inceleyebilir, tüm modülleri keşfedebilirsiniz.
                    </div>
                </div>
                <div>
                    <span class="cta-btn">Panel’e Geç →</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="metric-strip">', unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown("""
        <div class="metric-feature">
            <div class="metric-feature-icon">🎯</div>
            <div>
                <div class="metric-feature-title">Tek merkez</div>
                <div class="metric-feature-text">Planlama, kontrol ve raporlama tek akışta yönetilir.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown("""
        <div class="metric-feature">
            <div class="metric-feature-icon" style="background:#eefbf4;">🛡️</div>
            <div>
                <div class="metric-feature-title">Daha az hata</div>
                <div class="metric-feature-text">Çakışma, dengesizlik ve kritik ihlaller görünür hale gelir.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with m3:
        st.markdown("""
        <div class="metric-feature">
            <div class="metric-feature-icon" style="background:#f4efff;">📊</div>
            <div>
                <div class="metric-feature-title">Kurumsal sunum</div>
                <div class="metric-feature-text">Karar vericilere güçlü ve anlaşılır çıktı üretir.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.write("")
    st.markdown('<div class="section-title" style="text-align:center;">Çalışma süreci</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub" style="text-align:center;">Sade, anlaşılır ve hızlı uygulanabilen dört adımlı yapı.</div>', unsafe_allow_html=True)

    s1, s2, s3, s4 = st.columns(4, gap="large")
    with s1:
        st.markdown("""
        <div class="step-card">
            <div class="step-num">1</div>
            <div class="step-title">Veri Alımı</div>
            <div class="step-text">Mevcut nöbet ve eczane verileri sisteme alınır.</div>
        </div>
        """, unsafe_allow_html=True)
    with s2:
        st.markdown("""
        <div class="step-card">
            <div class="step-num" style="background:#eefbf4;color:var(--green);">2</div>
            <div class="step-title">Kural Tanımı</div>
            <div class="step-text">Kuruma özel denge ve kısıtlar yapılandırılır.</div>
        </div>
        """, unsafe_allow_html=True)
    with s3:
        st.markdown("""
        <div class="step-card">
            <div class="step-num" style="background:#f4efff;color:var(--purple);">3</div>
            <div class="step-title">Kontrol</div>
            <div class="step-text">Planlama çıktıları sistem tarafından taranır.</div>
        </div>
        """, unsafe_allow_html=True)
    with s4:
        st.markdown("""
        <div class="step-card">
            <div class="step-num">4</div>
            <div class="step-title">Rapor</div>
            <div class="step-text">Yönetim ve paydaşlar için düzenli çıktı hazırlanır.</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.caption("Mail: info@ayca.com.tr  |  Web: ayca.com.tr")

# =========================================================
# DASHBOARD
# =========================================================
def show_dashboard():
    st.markdown('<div class="main-title">AYÇA | Eczane Nöbet Takip Sistemi</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="main-subtitle">Nöbet planını yalnızca görüntülemek değil, daha şeffaf ve daha yönetilebilir hale getirmek için tasarlandı.</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card" style="padding:28px; margin-bottom:18px;">
        <div class="eyebrow">Akıllı kontrol paneli</div>
        <div class="hero-title" style="font-size:40px; margin-bottom:10px;">
            Nöbet planı hazır. <span class="blue">Peki gerçekten</span> <span class="green">adil mi?</span>
        </div>
        <div class="hero-sub">
            AYÇA ile nöbet dağılımını tarih, grup ve eczane bazında izleyebilir; gün dengesi, dağılım görünümü ve özet tabloları tek ekranda takip edebilirsin.
        </div>
    </div>
    """, unsafe_allow_html=True)

    file = st.file_uploader("Excel dosyasını yükleyin", type=["xlsx"])

    if not file:
        st.info("Başlamak için Excel dosyasını yükleyin.")
        return

    df, genel = load_excel(file)

    if df.empty:
        st.error("Excel dosyasında okunabilir nöbet verisi bulunamadı.")
        return

    menu = st.sidebar.radio(
        "Panel Menü",
        [
            "Genel Özet",
            "Tarih Seç",
            "Aylık Takvim",
            "Grup Analizi",
            "Eczane Analizi"
        ]
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        <div class="small-note">
        Bu panel; nöbet dağılımını daha anlaşılır, daha düzenli ve daha kurumsal şekilde takip etmeniz için düzenlenmiştir.
        </div>
        """,
        unsafe_allow_html=True
    )

    if menu == "Genel Özet":
        toplam_nobet = len(df)
        toplam_eczane = df["Eczane"].nunique()
        toplam_ay = df["Ay"].nunique()
        ortalama_nobet = round(toplam_nobet / toplam_eczane, 2) if toplam_eczane else 0

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            show_metric_mini("Toplam Nöbet", toplam_nobet)
        with c2:
            show_metric_mini("Toplam Eczane", toplam_eczane)
        with c3:
            show_metric_mini("Toplam Ay", toplam_ay)
        with c4:
            show_metric_mini("Ortalama Nöbet", ortalama_nobet)

        st.markdown('<div class="section-title">Gün Dağılımı</div>', unsafe_allow_html=True)

        gun_sayim = df["Gün"].value_counts().reset_index()
        gun_sayim.columns = ["Gün", "Sayı"]
        gun_sayim["Gün"] = pd.Categorical(gun_sayim["Gün"], categories=gun_sira, ordered=True)
        gun_sayim = gun_sayim.sort_values("Gün")

        fig = px.pie(
            gun_sayim,
            names="Gün",
            values="Sayı",
            hole=0.55,
            color="Gün",
            color_discrete_sequence=[
                "#1f4b99", "#2e6bdb", "#4d8af0", "#7bb0ff", "#22a06b", "#49c38a", "#9edcbf"
            ]
        )
        fig.update_traces(textposition="inside", textinfo="percent+label")
        fig.update_layout(
            margin=dict(l=10, r=10, t=10, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend_title_text=""
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown('<div class="section-title">Özet Tablo</div>', unsafe_allow_html=True)
        ozet, _ = prepare_ozet_table(df, genel)
        st.dataframe(ozet, use_container_width=True, height=500)

    elif menu == "Tarih Seç":
        min_tarih = df["Tarih"].min().date()
        max_tarih = df["Tarih"].max().date()

        col1, col2 = st.columns([1, 2])
        with col1:
            tarih = st.date_input(
                "Tarih seçin",
                value=min_tarih,
                min_value=min_tarih,
                max_value=max_tarih
            )

        secilen_tarih = tarih.to_pydatetime().date() if hasattr(tarih, "to_pydatetime") else tarih
        sonuc = df[df["Tarih"].dt.date == secilen_tarih].copy().sort_values(["Grup", "Eczane"])

        with col2:
            st.markdown(
                f"""
                <div class="card">
                    <h3>Seçilen Tarih</h3>
                    <p style="font-size:1.15rem;">{secilen_tarih.day} {aylar_tr[secilen_tarih.month]} {secilen_tarih.year}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown('<div class="section-title">O gün nöbetçi olan eczaneler</div>', unsafe_allow_html=True)

        if sonuc.empty:
            st.warning("Seçilen tarihte kayıt bulunamadı.")
        else:
            st.dataframe(sonuc[["Tarih", "Gün", "Grup", "Eczane"]], use_container_width=True, height=450)

    elif menu == "Aylık Takvim":
        ay = st.selectbox("Ay seç", sorted(df["Ay"].unique()))
        sonuc = df[df["Ay"] == ay].copy()

        st.markdown('<div class="section-title">Aylık nöbet takvimi</div>', unsafe_allow_html=True)

        if sonuc.empty:
            st.warning("Seçilen ay için veri bulunamadı.")
        else:
            pivot = pd.pivot_table(
                sonuc,
                index="Tarih",
                columns="Grup",
                values="Eczane",
                aggfunc="first"
            )

            pivot = pivot.fillna("")
            pivot = pivot.sort_index()
            pivot.index = pd.to_datetime(pivot.index).strftime("%d.%m.%Y")
            pivot = pivot.reset_index().rename(columns={"index": "Tarih"})

            st.dataframe(pivot, use_container_width=True, height=650)

    elif menu == "Grup Analizi":
        if genel is not None and "Grup" in genel.columns:
            grup_listesi = sorted(genel["Grup"].dropna().unique())
        else:
            grup_listesi = sorted(df["Grup"].dropna().unique())

        st.markdown('<div class="section-title">Grup görünümü</div>', unsafe_allow_html=True)
        grup = st.selectbox("Grup seç", grup_listesi)

        ozet, _ = prepare_ozet_table(df, genel)
        grup_ozet = ozet[ozet["Grup"] == grup].copy()

        st.dataframe(grup_ozet, use_container_width=True, height=400)

        st.markdown('<div class="section-title">Grup günlere göre nöbet dağılımı</div>', unsafe_allow_html=True)

        sonuc = df[df["Grup"] == grup].copy()

        sayim = (
            sonuc.groupby(["Gün", "Eczane"])
            .size()
            .reset_index(name="Nöbet Sayısı")
        )

        sayim["Gün"] = pd.Categorical(
            sayim["Gün"],
            categories=gun_sira,
            ordered=True
        )
        sayim = sayim.sort_values("Gün")

        fig = px.bar(
            sayim,
            x="Gün",
            y="Nöbet Sayısı",
            color="Eczane",
            barmode="group",
            category_orders={"Gün": gun_sira},
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig.update_layout(
            margin=dict(l=10, r=10, t=30, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend_title_text=""
        )
        st.plotly_chart(fig, use_container_width=True)

    elif menu == "Eczane Analizi":
        st.markdown('<div class="section-title">Eczane arama</div>', unsafe_allow_html=True)

        arama = st.text_input("Eczane adı ara")
        eczane_listesi = sorted(df["Eczane"].dropna().unique())

        if arama:
            eczane_listesi = [e for e in eczane_listesi if arama.lower() in e.lower()]

        if not eczane_listesi:
            st.warning("Arama kriterine uygun eczane bulunamadı.")
            return

        eczane = st.selectbox("Eczane seç", eczane_listesi)
        sonuc = df[df["Eczane"] == eczane].copy().sort_values("Tarih")

        c1, c2 = st.columns([1, 2])
        with c1:
            show_metric_mini("Toplam Nöbet", len(sonuc))
        with c2:
            grup_bilgisi = sonuc["Grup"].iloc[0] if not sonuc.empty else "-"
            show_metric_mini("Grup", grup_bilgisi)

        st.markdown('<div class="section-title">Eczane nöbet geçmişi</div>', unsafe_allow_html=True)
        st.dataframe(sonuc[["Tarih", "Gün", "Grup", "Ay"]], use_container_width=True, height=450)

# =========================================================
# APP
# =========================================================
render_sidebar_logo()

st.sidebar.markdown("---")
st.sidebar.caption("Akıllı Yazılım Çözüm Asistanı")

tab1, tab2 = st.tabs(["Tanıtım", "Panel"])

with tab1:
    show_landing()

with tab2:
    show_dashboard()
