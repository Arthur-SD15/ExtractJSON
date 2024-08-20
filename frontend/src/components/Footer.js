import React from 'react';

export default function Footer() {
    return (
        <footer className="bg-gradient-to-r from-yellow-500 via-yellow-400 to-yellow-500 text-gray-900 py-3 shadow-md border-t-2 border-yellow-700">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                <p className="text-sm">
                    &copy; {new Date().getFullYear()} JSON Extract | todos os direitos reservados.
                </p>
            </div>
        </footer>
    );
}
