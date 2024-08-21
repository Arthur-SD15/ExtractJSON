import '@/styles/globals.css'; 
import Head from 'next/head';
import Nav from '../components/Nav';
import Footer from '../components/Footer';
import { useRouter } from 'next/router';
import { useEffect } from 'react';

export default function App({ Component, pageProps }) {
  const router = useRouter();
  const { pathname } = router;

  useEffect(() => {
    const validRoutes = ['/', '/configurar/configurar-json'];
    if (!validRoutes.includes(pathname)) {
      router.push('/');
    }
  }, [pathname, router]);

  return (
    <>
      <Head>
        <title>JSON Extract</title>
        <meta name="description" content="JSON Extract" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      
      <div className="flex flex-col min-h-screen">
        <Nav />
        <main className="flex-grow">
          <Component {...pageProps} />
        </main>
        <Footer />
      </div>
    </>
  );
}
