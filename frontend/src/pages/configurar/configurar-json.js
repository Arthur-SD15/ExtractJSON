import Head from 'next/head';
import 'react-toastify/dist/ReactToastify.css';

export default function ConfigurarJSON() {
  return (
    <div>
      <Head>
        <title>JSON Extract - Config</title>
        <meta name="description" content="JSON Extract" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className="flex items-center justify-center h-screen">
        <h1 className="text-4xl font-bold">Hello, World!</h1>
      </main>
      <ToastContainer />
    </div>
  );
}
