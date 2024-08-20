import Head from 'next/head';
import UploadForm from './enviar/upload-json';

export default function Home() {
  return (
    <div>
      <Head>
        <title>JSON Extract - Configurar</title>
        <meta name="description" content="JSON Extract" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <UploadForm />
    </div>
  );
}
