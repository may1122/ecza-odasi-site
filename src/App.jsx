const logoSrc = "/images/logo.png";

const siteContent = {
  brand: "AYÇA",
  subtitle: "Akıllı Yazılım Çözüm Asistanı",
  slogan: "Nöbet Dağılımında Adalet ve Denge",
  heroText:
    "Şehirlerde ve ilçelerde nöbet planlaması yapılırken adalet, denge ve memnuniyet aynı anda sağlanmak zor olabilir. AYÇA, bu süreci daha akıllı ve daha yönetilebilir hale getirmek için tasarlanmıştır.",
  questions: [
    "Nöbet yazarken problem mi yaşıyorsunuz?",
    "Eczacılardan sürekli şikayet mi alıyorsunuz?",
    "Bayram ve hafta sonu dağılımında denge kurmakta zorlanıyor musunuz?",
  ],
  problems: [
    "Manuel planlama hataları",
    "Adaletsiz nöbet dağılımı",
    "Bayram ve hafta sonu dengesizliği",
    "Süreçte zaman kaybı",
    "Eczacılardan gelen itirazlar",
  ],
  strategySteps: [
    "Eczaneler sisteme tanımlanır",
    "Geçmiş nöbet verileri eklenir",
    "Sistem algoritması çalıştırılır",
    "En dengeli nöbet listesi oluşturulur",
  ],
  differentiators: [
    "Ağırlıklı gün katsayı sistemi",
    "Bayram adaleti algoritması",
    "Minimum nöbet aralığı kontrolü",
    "Dinamik eczane yönetimi",
    "Çok kriterli optimizasyon",
  ],
  advantages: [
    "Adil nöbet dağılımı",
    "Yönetim yükünü azaltır",
    "Eczacı memnuniyetini artırır",
    "Hızlı ve güvenilir sonuç",
    "Veri odaklı karar destek",
  ],
};

export default function AycaPreview() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-100 via-sky-50 to-emerald-100 text-slate-800">
      <header className="sticky top-0 z-40 border-b border-slate-300 bg-slate-50/90 backdrop-blur">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
          <div className="flex items-center gap-4">
            <img
              src={logoSrc}
              alt="AYÇA Logo"
              className="h-14 w-auto rounded-xl bg-white p-1 shadow-sm"
            />
            <div>
              <div className="text-xl font-bold tracking-tight text-slate-900">
                {siteContent.brand}
              </div>
              <div className="text-sm text-slate-600">
                {siteContent.subtitle}
              </div>
            </div>
          </div>

          <nav className="hidden gap-6 text-sm text-slate-600 md:flex">
            <a href="#anasayfa" className="transition hover:text-slate-900">
              Ana Sayfa
            </a>
            <a href="#problem" className="transition hover:text-slate-900">
              Problem
            </a>
            <a href="#cozum" className="transition hover:text-slate-900">
              AYÇA'nın Çözüm Stratejisi
            </a>
            <a href="#teklif" className="transition hover:text-slate-900">
              Teklif Al
            </a>
          </nav>
        </div>
      </header>

      <section
        id="anasayfa"
        className="relative overflow-hidden border-b border-slate-200"
      >
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(59,130,246,0.14),transparent_28%),radial-gradient(circle_at_top_left,rgba(16,185,129,0.14),transparent_24%)]" />
        <div className="relative mx-auto grid max-w-6xl gap-10 px-6 py-16 md:grid-cols-2 md:py-24">
          <div className="flex flex-col justify-center">
            <div className="mb-4 inline-flex w-fit rounded-full border border-sky-200 bg-sky-100 px-3 py-1 text-xs text-sky-700">
              Ecza odaları için daha sade ve daha akıllı planlama
            </div>

            <img
              src={logoSrc}
              alt="AYÇA Logo"
              className="mb-6 h-20 w-auto rounded-2xl bg-white p-2 shadow-md"
            />

            <h1 className="max-w-3xl text-4xl font-semibold leading-tight tracking-tight text-slate-900 md:text-6xl">
              {siteContent.slogan}
            </h1>

            <p className="mt-6 max-w-xl text-base leading-8 text-slate-600 md:text-lg">
              {siteContent.heroText}
            </p>

            <div className="mt-8 flex flex-col gap-3 sm:flex-row">
              <a
                href="#problem"
                className="rounded-2xl bg-sky-600 px-5 py-3 text-center text-sm font-semibold text-white shadow-lg transition hover:scale-[1.02]"
              >
                Problemi İncele
              </a>
              <a
                href="#teklif"
                className="rounded-2xl border border-slate-300 bg-white px-5 py-3 text-center text-sm font-medium text-slate-700 transition hover:bg-slate-50"
              >
                Teklif Al
              </a>
            </div>
          </div>

          <div className="rounded-[32px] border border-sky-100 bg-white/85 p-6 shadow-xl backdrop-blur">
            <div className="rounded-[24px] border border-slate-100 bg-gradient-to-br from-sky-50 to-emerald-50 p-6">
              <div className="mb-4 text-sm font-medium text-sky-700">
                Sık karşılaşılan sorular
              </div>

              <div className="space-y-3">
                {siteContent.questions.map((item) => (
                  <div
                    key={item}
                    className="rounded-2xl border border-slate-200 bg-slate-50 p-4 text-sm font-medium text-slate-700 shadow-sm"
                  >
                    {item}
                  </div>
                ))}
              </div>

              <div className="mt-5 rounded-2xl border border-emerald-200 bg-emerald-100 p-4 text-sm text-emerald-800">
                AYÇA, şehir ve ilçe düzeyinde nöbet planlamasını daha adil, daha
                hızlı ve daha şeffaf hale getirmeyi hedefler.
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="problem" className="border-b border-slate-200 bg-slate-50">
        <div className="mx-auto max-w-6xl px-6 py-20">
          <div className="max-w-3xl">
            <div className="text-sm font-medium text-rose-600">Problem</div>
            <h2 className="mt-3 text-3xl font-semibold tracking-tight text-slate-900 md:text-4xl">
              Eczane nöbet planlamasında yaşanan temel sorunlar
            </h2>
            <p className="mt-5 text-base leading-8 text-slate-600">
              Özellikle şehirlerde ve yoğun bölgelerde nöbet listesi
              hazırlanırken adalet, denge ve memnuniyet aynı anda korunmakta
              zorlanabilir.
            </p>
          </div>

          <div className="mt-12 grid gap-6 md:grid-cols-2 xl:grid-cols-3">
            {siteContent.problems.map((item) => (
              <div
                key={item}
                className="rounded-3xl border border-slate-200 bg-gradient-to-br from-white to-rose-100 p-6 shadow-sm"
              >
                <div className="text-lg font-semibold text-slate-900">
                  {item}
                </div>
              </div>
            ))}
          </div>

          <div className="mt-12 grid gap-6 md:grid-cols-[1.1fr_0.9fr]">
            <div className="rounded-[28px] border border-slate-200 bg-slate-50 p-8">
              <div className="text-xl font-semibold text-slate-900">
                Problem akışı
              </div>
              <p className="mt-3 text-sm leading-7 text-slate-600">
                Gantt yerine, sorunun nasıl oluştuğunu anlatan sade bir akış
                şeması daha anlaşılır olur.
              </p>

              <div className="mt-6 grid gap-3 text-sm">
                <div className="rounded-2xl bg-white p-4 text-slate-700 shadow-sm ring-1 ring-slate-200">
                  Veri toplama ve manuel değerlendirme
                </div>
                <div className="rounded-2xl bg-white p-4 text-slate-700 shadow-sm ring-1 ring-slate-200">
                  Bayram, hafta sonu ve geçmiş nöbet dengesini kurma çabası
                </div>
                <div className="rounded-2xl bg-white p-4 text-slate-700 shadow-sm ring-1 ring-slate-200">
                  İtirazlar, düzeltmeler ve yeniden planlama ihtiyacı
                </div>
                <div className="rounded-2xl bg-rose-100 p-4 font-medium text-rose-700 ring-1 ring-rose-200">
                  Sonuç: zaman kaybı, memnuniyetsizlik ve dengesizlik riski
                </div>
              </div>
            </div>

            <div className="rounded-[28px] border border-rose-200 bg-gradient-to-br from-rose-50 to-orange-50 p-8">
              <div className="text-xl font-semibold text-slate-900">
                Ana sonuç
              </div>
              <p className="mt-4 text-base leading-8 text-slate-700">
                Bu durum hem oda yönetimini hem eczacıları zorlamaktadır.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section
        id="cozum"
        className="border-b border-slate-200 bg-gradient-to-b from-sky-50 to-white"
      >
        <div className="mx-auto max-w-6xl px-6 py-20">
          <div className="max-w-3xl">
            <div className="text-sm font-medium text-sky-700">
              AYÇA'nın Çözüm Stratejisi
            </div>
            <h2 className="mt-3 text-3xl font-semibold tracking-tight text-slate-900 md:text-4xl">
              Sadece planlama değil, akıllı dengeleme
            </h2>
            <p className="mt-5 text-base leading-8 text-slate-600">
              AYÇA, geçmiş verileri ve çok kriterli yaklaşımı kullanarak daha
              dengeli, daha hızlı ve daha şeffaf nöbet listeleri üretmeyi
              hedefler.
            </p>
          </div>

          <div className="mt-12 grid gap-6 md:grid-cols-2">
            <div className="rounded-[28px] border border-slate-200 bg-white/90 p-8 shadow-sm">
              <div className="text-xl font-semibold text-slate-900">
                Sistem nasıl çalışır?
              </div>

              <div className="mt-6 space-y-3">
                {siteContent.strategySteps.map((item, index) => (
                  <div
                    key={item}
                    className="flex items-start gap-4 rounded-2xl border border-slate-200 bg-slate-50 p-4"
                  >
                    <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-sky-600 text-sm font-bold text-white">
                      {index + 1}
                    </div>
                    <div className="text-sm leading-7 text-slate-700">
                      {item}
                    </div>
                  </div>
                ))}
              </div>

              <div className="mt-6 rounded-2xl border border-emerald-200 bg-emerald-100 p-4 text-sm font-medium text-emerald-800">
                Sonuç: Optimum ve adil planlama
              </div>
            </div>

            <div className="rounded-[28px] border border-slate-200 bg-white/90 p-8 shadow-sm">
              <div className="text-xl font-semibold text-slate-900">
                AYÇA'nın farkı
              </div>

              <div className="mt-6 grid gap-3">
                {siteContent.differentiators.map((item) => (
                  <div
                    key={item}
                    className="rounded-2xl border border-slate-200 bg-gradient-to-r from-sky-50 to-white p-4 text-sm text-slate-700"
                  >
                    {item}
                  </div>
                ))}
              </div>

              <div className="mt-6 rounded-2xl border border-sky-200 bg-sky-100 p-4 text-sm text-sky-800">
                Sadece planlama değil, akıllı dengeleme yapar.
              </div>
            </div>
          </div>

          <div className="mt-10 rounded-[28px] border border-slate-200 bg-white/90 p-8 shadow-sm">
            <div className="text-xl font-semibold text-slate-900">
              Sağladığı avantajlar
            </div>
            <div className="mt-6 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
              {siteContent.advantages.map((item) => (
                <div
                  key={item}
                  className="rounded-2xl border border-emerald-200 bg-emerald-50 p-4 text-sm font-medium text-slate-700"
                >
                  ✔ {item}
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      <section id="teklif" className="mx-auto max-w-6xl px-6 py-20">
        <div className="grid gap-10 md:grid-cols-2">
          <div>
            <div className="text-sm font-medium text-sky-700">Teklif Al</div>
            <h2 className="mt-3 text-3xl font-semibold tracking-tight text-slate-900 md:text-4xl">
              AYÇA hakkında detaylı bilgi ve teklif talebi
            </h2>
            <p className="mt-5 max-w-xl text-base leading-8 text-slate-600">
              Bu bölüm, kurumlardan geri dönüş almak için sade tutuldu. İlk
              sürümde iletişim ve teklif akışı odaklı ilerler.
            </p>
            <div className="mt-6 rounded-2xl border border-slate-200 bg-slate-50 p-5 text-sm text-slate-600">
              Telefon ve e-posta bilgileri burada yer alacak. İstersen daha
              sonra WhatsApp butonu da eklenebilir.
            </div>
          </div>

          <div className="rounded-[32px] border border-slate-200 bg-white/92 p-6 shadow-xl">
            <div className="grid gap-4">
              <input
                className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none placeholder:text-slate-400"
                placeholder="Kurum Adı"
              />
              <input
                className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none placeholder:text-slate-400"
                placeholder="Yetkili Kişi"
              />
              <input
                className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none placeholder:text-slate-400"
                placeholder="Telefon veya E-posta"
              />
              <textarea
                rows={5}
                className="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm outline-none placeholder:text-slate-400"
                placeholder="Kısa açıklama veya talep"
              />
              <button className="rounded-2xl bg-sky-600 px-5 py-3 text-sm font-semibold text-white transition hover:scale-[1.01]">
                Teklif Gönder
              </button>
              <p className="text-xs leading-6 text-slate-500">
                İlk aşamada bu form görünüm amaçlıdır. Sonra gerçek çalışır
                forma dönüştürülebilir.
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
