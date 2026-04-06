import { siteContent } from "./data/siteContent";

export default function App() {
  return (
    <div className="page">
      <header className="header">
        <div className="container nav">
          <div>
            <div className="brand">{siteContent.projectName}</div>
            <div className="subtitle">{siteContent.projectSubtitle}</div>
          </div>

          <nav className="menu">
            <a href="#anasayfa">Ana Sayfa</a>
            <a href="#bilgilendirme">Bilgilendirme</a>
            <a href="#teklif">Teklif Al</a>
          </nav>
        </div>
      </header>

      <main>
        <section id="anasayfa" className="hero">
          <div className="container hero-grid">
            <div>
              <div className="badge">{siteContent.heroBadge}</div>
              <h1>{siteContent.heroTitle}</h1>
              <p>{siteContent.heroText}</p>

              <div className="buttons">
                <a className="button primary" href="#bilgilendirme">
                  Yazılımı İncele
                </a>
                <a className="button secondary" href="#teklif">
                  Teklif Talep Et
                </a>
              </div>
            </div>

            <div className="card">
              <h3>Yayın mantığı</h3>
              <div className="steps">
                <div className="step">1. Kodu GitHub'a yüklersin</div>
                <div className="step">2. Vercel projeyi bağlar</div>
                <div className="step">3. Site online yayınlanır</div>
                <div className="step active">4. Güncelledikçe otomatik yenilenir</div>
              </div>
            </div>
          </div>
        </section>

        <section id="bilgilendirme" className="section alt">
          <div className="container">
            <div className="section-head">
              <span className="section-label">Bilgilendirme</span>
              <h2>{siteContent.infoTitle}</h2>
              <p>{siteContent.infoText}</p>
            </div>

            <div className="feature-grid">
              {siteContent.features.map((item) => (
                <div key={item} className="feature-card">
                  <h3>{item}</h3>
                  <p>
                    Bu alanı daha sonra kendi projenin gerçek detaylarıyla
                    değiştirebilirsin.
                  </p>
                </div>
              ))}
            </div>

            <div className="media-box">
              <h3>Görsel / video alanı</h3>
              <p>
                İstersen aşağıya ekran görüntüsü, logo veya video ekleyebilirsin.
              </p>

              <div className="media-grid">
                <img src="/images/logo.png" alt="Logo" className="media-image" />

                <video controls className="media-video">
                  <source src="/videos/tanitim.mp4" type="video/mp4" />
                  Tarayıcın video etiketini desteklemiyor.
                </video>
              </div>
            </div>
          </div>
        </section>

        <section id="teklif" className="section">
          <div className="container offer-grid">
            <div>
              <span className="section-label">Teklif Al</span>
              <h2>{siteContent.offerTitle}</h2>
              <p>{siteContent.offerText}</p>

              <div className="contact-box">
                <p>
                  <strong>E-posta:</strong>{" "}
                  <a href={`mailto:${siteContent.email}`}>{siteContent.email}</a>
                </p>
                <p>
                  <strong>WhatsApp:</strong>{" "}
                  <a
                    href={siteContent.whatsappUrl}
                    target="_blank"
                    rel="noreferrer"
                  >
                    Mesaj gönder
                  </a>
                </p>
              </div>
            </div>

            <div className="card">
              <h3>Örnek teklif formu</h3>

              <form className="form" onSubmit={(e) => e.preventDefault()}>
                <input type="text" placeholder="Kurum Adı" />
                <input type="text" placeholder="Yetkili Kişi" />
                <input type="text" placeholder="Telefon veya E-posta" />
                <textarea rows="5" placeholder="Talep veya kısa açıklama" />
                <button type="submit" className="button primary full">
                  Teklif Gönder
                </button>
              </form>

              <p className="form-note">
                Bu form şu an tasarım amaçlıdır. Sonradan çalışan hale
                getirilebilir.
              </p>
            </div>
          </div>
        </section>
      </main>

      <footer className="footer">
        <div className="container footer-wrap">
          <div>
            <strong>{siteContent.projectName}</strong> · Tanıtım ve teklif toplama
            sitesi
          </div>
          <div>{siteContent.footerNote}</div>
        </div>
      </footer>
    </div>
  );
}
