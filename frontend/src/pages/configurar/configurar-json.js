import Head from 'next/head';
import 'react-toastify/dist/ReactToastify.css';
import { ToastContainer, toast } from 'react-toastify';
import { useState } from 'react';

export default function ConfigurarJSON() {
  const [attributes, setAttributes] = useState([['']]);
  const [showExample, setShowExample] = useState(false);

  const handleAttributeLevelChange = (index, levelIndex, e) => {
    const newAttributes = [...attributes];
    newAttributes[index][levelIndex] = e.target.value;
    setAttributes(newAttributes);
  };

  const handleAddAttributeSet = () => {
    setAttributes([...attributes, ['']]);
  };

  const handleRemoveAttributeSet = (index) => {
    const newAttributes = attributes.filter((_, i) => i !== index);
    setAttributes(newAttributes);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
  };

  const toggleExample = () => {
    setShowExample(!showExample);
  };

  return (
    <div>
      <Head>
        <title>JSON Extract - Config</title>
        <meta name="description" content="JSON Extract" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className="max-w-3xl mx-auto p-8 bg-gray-50 shadow-lg mb-6 mt-8 rounded-lg">
        <form onSubmit={handleSubmit}>
          <div className="space-y-6">
            <p className="text-sm text-gray-500 mt-0">
              Obs: Para configurar os atributos e possibilitar a listagem das informações, é necessário preencher os níveis de atributos de baixo para cima. Certifique-se de definir todos os níveis necessários para extrair as informações do JSON corretamente.
            </p>
            <button
              type="button"
              onClick={toggleExample}
              className="w-full py-1 bg-gray-600 text-white rounded-md shadow-md hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500 text-sm mb-4"
            >
              {showExample ? 'Ocultar Exemplo' : 'Ver Exemplo'}
            </button>
            {showExample && (
              <div className="bg-gray-100 p-4 rounded-md border border-gray-300 mb-6">
                <p className="text-sm text-gray-700">
                  Suponha que você tenha um JSON como este:
                </p>
                <pre className="bg-gray-900 p-2 rounded-md text-xs overflow-x-auto mt-2">
                  {`
[
  {
    "id": "b87718c3-1101-4d04-9488-952d3afb2f16",
    "code": null,
    "summary": null,
    "researchProject": null,
    "students": [
      {
        "id": "fa39709c-283f-4f07-81fb-a4369b3817c4",
        "student": {
          "id": "d881cfb0-6243-4253-b4ed-7b28f9f945d5",
          "institutionId": "12a1c659-9688-41f9-8236-8bd97a559047",
          "institution": {
            "id": "12a1c659-9688-41f9-8236-8bd97a559047",
            "name": null,
            "address": {
              "id": "dbd488e2-df6c-420d-b4e9-b795244c7fd4",
              "number": "000",
              "street": "XXXXXXXXXXXXXXXX",
              "neighborhood": "XXXXXXXXXXX",
              "city": "Campo Grande",
              "state": "MS",
              "postalCode": "00000-00",
              "country": "BR",
              "additionalAddress": null
            }
          }
        }
      }
    ]
  }
]
                  `}
                </pre>
                <p className="text-sm text-gray-700 mt-2">
                  Para acessar a cidade, você deve preencher os seguintes níveis de atributos:
                </p>
                <ul className="list-disc list-inside text-sm text-gray-700 mt-2">
                  <li>students</li>
                  <li>student</li>
                  <li>institution</li>
                  <li>address</li>
                  <li>city</li>
                </ul>
              </div>
            )}
            {attributes.map((attrSet, index) => (
              <div key={index} className="bg-white p-6 rounded-lg shadow-md border border-gray-200">
                <div className="flex flex-wrap gap-4 mb-4">
                  {attrSet.map((attr, levelIndex) => (
                    <div key={levelIndex} className="flex-1 min-w-[150px] max-w-[calc(50% - 16px)]">
                      <input
                        type="text"
                        value={attr}
                        onChange={(e) => handleAttributeLevelChange(index, levelIndex, e)}
                        placeholder={`Nível: (ex: students)`}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400 text-sm text-gray-900 bg-white"
                      />
                    </div>
                  ))}
                </div>
                <div className="flex items-center space-x-3">
                  <button
                    type="button"
                    onClick={() => handleRemoveAttributeSet(index)}
                    className="px-3 py-1 bg-red-500 text-white rounded-md hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500 text-sm"
                  >
                    Remover Atributo
                  </button>
                </div>
              </div>
            ))}
            <div className="flex gap-3 mt-4">
              <button
                type="button"
                onClick={handleAddAttributeSet}
                className="inline-flex items-center px-3 py-2 bg-blue-600 text-white rounded-md shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
              >
                +
              </button>
              <button
                type="submit"
                className="inline-flex items-center px-3 py-2 bg-green-600 text-white rounded-md shadow-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 text-sm"
              >
                Salvar
              </button>
            </div>
          </div>
        </form>
      </div>
      <ToastContainer />
    </div>
  );
}