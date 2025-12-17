const fs = require('fs');
const path = require('path');

function loadPlugins(app) {
  const pluginsDir = path.join(__dirname, 'plugins');
  if (!fs.existsSync(pluginsDir)) return;
  fs.readdirSync(pluginsDir).forEach(file => {
    if (file.endsWith('.js')) {
      const plugin = require(path.join(pluginsDir, file));
      if (typeof plugin === 'function') plugin(app);
    }
  });
}
module.exports = loadPlugins;
