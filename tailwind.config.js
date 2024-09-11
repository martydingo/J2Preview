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
  daisyui: {
    themes: [
      {
        halcyon: {
          "primary": "#ffcc66",
          "secondary": "#f6d860",
          "accent": "#37cdbe",
          "neutral": "#3d4451",
          "base-100": "#171c28",
          "base-200": "#1d2433",
          "base-300": "#2f3b54",
          "base-content": "#d7dce2"


        },
      },
    ],
  },
}

