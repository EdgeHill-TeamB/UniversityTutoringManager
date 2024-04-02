/**
 * "IMPORTANT: THIS FILE IS GENERATED, CHANGES SHOULD BE MADE WITHIN '@okta/generator'"
 **/

import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import envCompatible from 'vite-plugin-env-compatible'
import path from 'path'





// https://vitejs.dev/config/
export default defineConfig( {
    base:  '/',
    plugins: [react(), envCompatible()],
    server: {
      port: process.env.PORT || 3001
    },
    preview: {
      port: process.env.PORT || 8080
    },
    build: {
      outDir: "build",
      rollupOptions: {
        // always throw with build warnings
        onwarn (warning, warn) {
          warn('\nBuild warning happened, customize "onwarn" callback in vite.config.js to handle this error.');
          throw new Error(warning);
        }
      }
    }
  }
);


