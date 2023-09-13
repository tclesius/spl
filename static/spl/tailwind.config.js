/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
        "./node_modules/tw-elements/dist/js/**/*.js"

    ],
    theme: {
        extend: {
            colors: {
                'ash-gray': "#2D2D2D",
                'dew-gray': "#F7F7F7"
            },
            fontFamily: {
                'inter': ['Inter', 'sans-serif']
            },
        },
    },
    plugins: [require("tw-elements/dist/plugin.cjs")],
    darkMode: "class"
}