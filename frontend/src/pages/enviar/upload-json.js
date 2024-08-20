import { useState, useRef } from 'react';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

export default function UploadForm() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      toast.error("Nenhum arquivo selecionado.");
      return;
    }

    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await fetch('http://localhost:3001/api/upload', {
        method: 'POST',
        body: formData,
      });

      if (res.ok) {
        const data = await res.json();
        setResponse(data);
        toast.success("Arquivo enviado com sucesso.");
      } else {
        const data = await res.json();
        toast.error(`${data.error}`);
      }
    } catch (err) {
      toast.error(`${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = async () => {
    setFile(null);
    setResponse(null);
    setError(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }

    try {
        const res = await fetch('http://localhost:3001/api/reset', {
            method: 'POST',
        });

        if (res.ok) {
            toast.info("Formulário resetado e arquivos excluídos.");
        } else {
            const data = await res.json();
            toast.error(`Erro ao excluir arquivos: ${data.error}`);
        }
    } catch (err) {
        toast.error(`${err.message}`);
    }
  };

  const handleExport = async () => {
    try {
      const res = await fetch('http://localhost:3001/api/export', {
        method: 'GET',
      });

      if (res.ok) {
        const blob = await res.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'data.xlsx';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        toast.success("Planilha exportada com sucesso.");
      } else {
        const data = await res.json();
        toast.error(`${data.error}`);
      }
    } catch (err) {
      toast.error(`${err.message}`);
    }
  };

  return (
    <>
      
      <div className="max-w-4xl mx-auto p-4 bg-white shadow-2xl mt-4 rounded-lg">
        <form onSubmit={handleSubmit} className="flex items-center space-x-2">
          <div className="flex-1 flex flex-col">
            <input
              id="file-upload"
              type="file"
              onChange={handleFileChange}
              className="block w-full text-sm text-gray-500 file:bg-blue-50 file:border-0 file:text-blue-700 file:font-medium file:rounded-md file:py-2 file:px-3 hover:file:bg-blue-100 focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm"
              ref={fileInputRef}
            />
          </div>
          <button
            type="submit"
            className="py-2 px-4 bg-blue-600 text-white text-sm rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
            disabled={loading}
          >
            {loading ? 'Uploading...' : 'Upload'}
          </button>
          <button
            type="button"
            onClick={handleExport}
            className="py-2 px-4 bg-green-600 text-white text-sm rounded-md shadow-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2"
          >
            Exportar Planilha
          </button>
          <button
            type="button"
            onClick={handleReset}
            className="py-2 px-4 bg-gray-600 text-white text-sm rounded-md shadow-md hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2"
          >
            Resetar
          </button>
        </form>
      </div>

      <div className="max-w-4xl mx-auto p-4 my-6 bg-white border border-gray-300 rounded-lg shadow-lg overflow-hidden">
        {!response && !error ? (
          <div className="text-gray-600 text-sm text-center">
            Nenhum arquivo JSON foi enviado.
          </div>
        ) : error ? (
          <div className="text-red-600 text-center">
            {error}
          </div>
        ) : (
          <div className="space-y-4">
            {response.map((item, index) => (
              <div key={index} className="p-2 border border-gray-200 rounded-lg">
                <p className="text-gray-600 text-sm mt-1 whitespace-pre-wrap">{item.value}</p>
              </div>
            ))}
          </div>
        )}
      </div>
      <ToastContainer />
    </>
  );
}
