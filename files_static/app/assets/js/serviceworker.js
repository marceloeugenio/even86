var staticCacheName = 'even86-v1';

// var filesToCache = [
//     '/offline',
//     '/css/django-pwa-app.css',
//     '/media/icon-160x160.png',
//     '/media/icon-160x160.png',
//     '/media/splash-640x1136.png',
//     '/images/icons/icon-144x144.png',
//     '/images/icons/icon-152x152.png',
//     '/images/icons/icon-192x192.png',
//     '/images/icons/icon-384x384.png',
//     '/images/icons/icon-512x512.png',
//     '/static/images/icons/splash-640x1136.png',
//     '/static/images/icons/splash-750x1334.png',
//     '/static/images/icons/splash-1242x2208.png',
//     '/static/images/icons/splash-1125x2436.png',
//     '/static/images/icons/splash-828x1792.png',
//     '/static/images/icons/splash-1242x2688.png',
//     '/static/images/icons/splash-1536x2048.png',
//     '/static/images/icons/splash-1668x2224.png',
//     '/static/images/icons/splash-1668x2388.png',
//     '/static/images/icons/splash-2048x2732.png'
// ];
 
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '',
      ]);
    })
  );
});
 
self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match('/offline/'));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});