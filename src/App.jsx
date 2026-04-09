import { siteContent } from "./data/siteContent";
import Header from "./components/Header";
import Hero from "./components/Hero";
import Solutions from "./components/Solutions";
import Features from "./components/Features";
import Process from "./components/Process";
import Audience from "./components/Audience";
import Contact from "./components/Contact";
import Footer from "./components/Footer";

export default function App() {
  return (
    <div>
      <Header siteContent={siteContent} />
      <Hero siteContent={siteContent} />
      <Solutions siteContent={siteContent} />
      <Features siteContent={siteContent} />
      <Process siteContent={siteContent} />
      <Audience siteContent={siteContent} />
      <Contact siteContent={siteContent} />
      <Footer siteContent={siteContent} />
    </div>
  );
}
