import { Configuration } from '@nuxt/types';

const config: Configuration = {
  plugins: [
    { src: '~/plugins/audio-recorder.ts', mode: 'client' } // Ensure the plugin runs only on client-side
  ],
  // include other configuration settings as needed
};

export default defineNuxtConfig({
  modules: ['@nuxtjs/supabase', '@nuxtjs/tailwindcss', '@element-plus/nuxt'],
  supabase: {
    supabaseUrl: process.env.SUPABASE_URL,
    supabaseKey: process.env.SUPABASE_KEY
  },
  tailwindcss: {
    cssPath: '~/assets/css/tailwind.postcss'
  },
  elementPlus:{},
  app: {
    layoutTransition: { name: 'layout', mode: 'out-in' },
    pageTransition: { name: 'page', mode: 'out-in' },
    head: {
      charset: 'utf-16',
      viewport: 'width=500, initial-scale=1',
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/MandarinMaster-logo.ico' },
        { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
        { rel: 'preconnect', href: 'https://fonts.gstatic.com' },
        { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Roboto+Mono&display=swap' },
      ]
    }
  }
})
