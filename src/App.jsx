const siteContent = {
  projectName: "AYCA",
  projectSubtitle: "Akıllı Nöbet Planlama Sistemi",
  heroTitle: "Ecza odalarına özel geliştirilen yazılım çözümü",
  heroText:
    "Bu site, yazılım projenin ne yaptığını sade biçimde anlatmak ve teklif talebi toplamak için hazırlanmıştır. Kodlar GitHub'da tutulabilir ve Vercel benzeri bir platformda online yayınlanabilir.",
  aboutTitle: "Yazılım ne yapıyor?",
  aboutText:
    "Bu bölümde sistemin sağladığı temel faydalar anlatılır. Metinler daha sonra tek yerden kolayca değiştirilebilir.",
  features: [
    "Başvuru ve kayıt süreçlerini takip eder",
    "Kurumsal iş akışlarını daha düzenli hale getirir",
    "Yönetim için temel görünürlük ve takip sağlar",
    "Sade arayüz ile hızlı kullanım sunar",
  ],
  offerTitle: "Teklif Al",
  offerText:
    "Kurumlar bu bölümden iletişim bilgilerini bırakabilir. İstersen daha sonra bu formu e-posta veya WhatsApp bağlantısına çevirebiliriz.",
  contactNote:
    "Bu sürüm basit, tek kullanıcılık ve GitHub'dan yönetilebilir yapı hedefiyle hazırlanmıştır.",
};

export default function EczaOdasiLandingPage() {
  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <header className="sticky top-0 z-40 border-b border-white/10 bg-slate-950/90 backdrop-blur">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
          <div className="flex items-center gap-3">
            <img
              src="/images/logo.png"
              alt="AYCA Logo"
              className="h-12 w-12 rounded-xl object-contain"
            />

            <div>
              <div className="text-lg font-semibold tracking-tight">
                {siteContent.projectName}
              </div>
              <div className="text-xs text-slate-400">
                {siteContent.projectSubtitle}
              </div>
            </div>
          </div>

          <nav className="hidden gap-6 text-sm text-slate-300 md:flex">
            <a href="#anasayfa" className="transition hover:text-white">
              Ana Sayfa
            </a>
            <a href="#hakkinda" className="transition hover:text-white">
              Bilgilendirme
            </a>
            <a href="#teklif" className="transition hover:text-white">
              Teklif Al
            </a>
          </nav>
        </div>
      </header>

      <section id="anasayfa" className="relative overflow-hidden">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(59,130,246,0.18),transparent_30%),radial-gradient(circle_at_top_left,rgba(34,197,94,0.14),transparent_30%)]" />
        <div className="relative mx-auto grid max-w-6xl gap-10 px-6 py-20 md:grid-cols-2 md:py-28">
          <div className="flex flex-col justify-center">
            <div className="mb-4 inline-flex w-fit rounded-full border border-cyan-400/20 bg-cyan-400/10 px-3 py-1 text-xs text-cyan-300">
              Basit ve online yayınlanabilir yapı
            </div>

            <h1 className="max-w-2xl text-4xl font-semibold leading-tight tracking-tight md:text-6xl">
              {siteContent.heroTitle}
            </h1>

            <p className="mt-6 max-w-xl text-base leading-7 text-slate-300 md:text-lg">
              {siteContent.heroText}
            </p>

            <div className="mt-8 flex flex-col gap-3 sm:flex-row">
              <a
                href="#hakkinda"
                className="rounded-2xl bg-cyan-400 px-5 py-3 text-center text-sm font-semibold text-slate-950 shadow-xl transition hover:scale-[1.02]"
              >
                Yazılımı İncele
              </a>

              <a
                href="#teklif"
                className="rounded-2xl border border-white/15 px-5 py-3 text-center text-sm font-medium text-white transition hover:bg-white/5"
              >
                Teklif Talep Et
              </a>
            </div>
          </div>

          <div className="rounded-[32px] border border-white/10 bg-white/5 p-6 shadow-2xl backdrop-blur">
            <div className="rounded-[24px] border border-white/10 bg-slate-900/70 p-6">
              <div className="text-sm font-medium text-slate-300">
                Yayın mantığı
              </div>

              <div className="mt-4 space-y-3 text-sm text-slate-300">
                <div className="rounded-2xl border border-white/10 bg-white/5 p-4">
                  1. Kodu GitHub'a yüklersin
                </div>
                <div className="rounded-2xl border border-white/10 bg-white/5 p-4">
                  2. Vercel / Netlify projeyi okur
                </div>
                <div className="rounded-2xl border border-white/10 bg-white/5 p-4">
                  3. Site online yayınlanır
                </div>
                <div className="rounded-2xl border border-cyan-400/20 bg-cyan-400/10 p-4 text-cyan-100">
                  4. Değişiklik yaptıkça yeniden güncellenir
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="hakkinda" className="border-y border-white/10 bg-white/5">
        <div className="mx-auto max-w-6xl px-6 py-20">
          <div className="max-w-3xl">
            <div className="text-sm font-medium text-cyan-300">
              Bilgilendirme
            </div>

            <h2 className="mt-3 text-3xl font-semibold tracking-tight md:text-4xl">
              {siteContent.aboutTitle}
            </h2>

            <p className="mt-5 text-base leading-8 text-slate-300">
              {siteContent.aboutText}
            </p>
          </div>

          <div className="mt-12 grid gap-6 md:grid-cols-2">
            {siteContent.features.map((item) => (
              <div
                key={item}
                className="rounded-3xl border border-white/10 bg-slate-900/70 p-6 shadow-lg"
              >
                <div className="text-lg font-semibold">{item}</div>
                <p className="mt-3 text-sm leading-7 text-slate-300">
                  Bu alanı daha sonra kendi projenin gerçek detayları ile
                  değiştirebilirsin.
                </p>
              </div>
            ))}
          </div>

          <div className="mt-12 rounded-[28px] border border-white/10 bg-slate-900/70 p-8">
            <div className="text-xl font-semibold">Görsel ve video ekleme</div>
            <p className="mt-4 text-sm leading-7 text-slate-300">
              Panel olmadan da proje klasörüne görsel veya video koyup sayfada
              gösterebilirsin. Bu yapı o mantığa uygun olacak şekilde sade
              tutulmuştur.
            </p>
          </div>
        </div>
      </section>

      <section id="teklif" className="mx-auto max-w-6xl px-6 py-20">
        <div className="grid gap-10 md:grid-cols-2">
          <div>
            <div className="text-sm font-medium text-cyan-300">Teklif Al</div>

            <h2 className="mt-3 text-3xl font-semibold tracking-tight md:text-4xl">
              {siteContent.offerTitle}
            </h2>

            <p className="mt-5 max-w-xl text-base leading-8 text-slate-300">
              {siteContent.offerText}
            </p>

            <div className="mt-6 rounded-2xl border border-white/10 bg-white/5 p-5 text-sm text-slate-300">
              İstersen bu bölümü daha sonra sadece mailto bağlantısı, WhatsApp
              butonu veya çalışan form olarak düzenleyebiliriz.
            </div>
          </div>

          <div className="rounded-[32px] border border-white/10 bg-white/5 p-6 shadow-xl">
            <div className="grid gap-4">
              <input
                className="rounded-2xl border border-white/10 bg-slate-950 px-4 py-3 text-sm outline-none placeholder:text-slate-500"
                placeholder="Kurum Adı"
              />
              <input
                className="rounded-2xl border border-white/10 bg-slate-950 px-4 py-3 text-sm outline-none placeholder:text-slate-500"
                placeholder="Yetkili Kişi"
              />
              <input
                className="rounded-2xl border border-white/10 bg-slate-950 px-4 py-3 text-sm outline-none placeholder:text-slate-500"
                placeholder="Telefon veya E-posta"
              />
              <textarea
                rows={5}
                className="rounded-2xl border border-white/10 bg-slate-950 px-4 py-3 text-sm outline-none placeholder:text-slate-500"
                placeholder="Talep veya kısa açıklama"
              />
              <button className="rounded-2xl bg-cyan-400 px-5 py-3 text-sm font-semibold text-slate-950 transition hover:scale-[1.01]">
                Teklif Gönder
              </button>
              <p className="text-xs leading-6 text-slate-500">
                Bu form şu an tasarım amaçlıdır. İstersen sonradan çalışan hale
                getiririz.
              </p>
            </div>
          </div>
        </div>
      </section>

      <footer className="border-t border-white/10 bg-slate-950">
        <div className="mx-auto flex max-w-6xl flex-col gap-3 px-6 py-8 text-sm text-slate-400 md:flex-row md:items-center md:justify-between">
          <div>
            <span className="font-medium text-white">
              {siteContent.projectName}
            </span>{" "}
            · Tanıtım ve teklif toplama sitesi
          </div>
          <div>{siteContent.contactNote}</div>
        </div>
      </footer>
    </div>
  );
}
