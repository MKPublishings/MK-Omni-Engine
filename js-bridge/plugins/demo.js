module.exports = function(app) {
  app.get('/plugin-demo', (req, res) => res.json({ msg: "Hello from a plugin!" }));
};
