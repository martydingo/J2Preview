import flowbite from "flowbite/plugin"
import daisyui from "daisyui"
import tailwind_typography from "@tailwindcss/typography"

/** @type {import('tailwindcss').Config} */

export default {
  content: [
    "./j2preview/templates/**/*.html",
    "./j2preview/static/src/**/*.js"
  ],
  darkMode: "class",
  theme: {
    extend: {},
  },
  plugins: [
    // flowbite,
    daisyui,
    tailwind_typography
  ],
}

