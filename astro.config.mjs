import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://repuvechihuahua.com',
  trailingSlash: 'always',
  build: {
    format: 'directory'
  }
});
