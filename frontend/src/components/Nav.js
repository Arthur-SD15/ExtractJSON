import React, { useState } from 'react';
import { useRouter } from 'next/router'; 
import { FaSignInAlt, FaSignOutAlt } from 'react-icons/fa';
import { toast } from 'react-toastify';

export default function Nav() {
    const [isConfig, setIsConfig] = useState(false);
    const router = useRouter();

    const toggleConfigInOut = () => {
        toast.info('Redirecionando...', {
            autoClose: 5000,
        });
    
        setTimeout(() => {
            setIsConfig(prevState => {
                const newConfigState = !prevState;
                router.push(newConfigState ? '/configurar/configurar-json' : '/');
                return newConfigState;
            });
        }, 5000); 
      };

    return (
        <nav className="bg-gradient-to-r from-yellow-500 via-yellow-400 to-yellow-500 text-gray-900 shadow-md border-b-2 border-yellow-700">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="relative flex items-center justify-between h-16">
                    <div className="flex items-center">
                        <img
                            src="https://www.svgrepo.com/show/361211/json.svg"
                            alt="JSON Icon"
                            className="h-8 w-8 ml-12"
                        />
                        <div className="text-xl font-semibold text-gray-900 hover:text-gray-900 transition duration-300 ease-in-out">
                            JSON Extract
                        </div>
                    </div>
                    <div className="flex items-center space-x-4 mr-12">
                        {isConfig ? (
                            <button
                                onClick={toggleConfigInOut}
                                className="text-white hover:text-gray-300 transition duration-300 ease-in-out"
                                aria-label="Sair"
                                title="Voltar"
                            >
                                <FaSignOutAlt className="h-6 w-6" />
                            </button>
                        ) : (
                            <button
                                onClick={toggleConfigInOut}
                                className="text-white hover:text-gray-300 transition duration-300 ease-in-out"
                                aria-label="Entrar"
                                title="Configurar JSON"
                            >
                                <FaSignInAlt className="h-6 w-6" />
                            </button>
                        )}
                    </div>
                </div>
            </div>
        </nav>
    );
}
