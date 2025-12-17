// Simple token authentication middleware
const API_TOKEN = process.env.API_TOKEN || "supersecrettoken";

function authenticate(req, res, next) {
  const token = req.headers['authorization'];
  if (token === `Bearer ${API_TOKEN}`) {
    next();
  } else {
    res.status(401).json({ error: 'Unauthorized' });
  }
}

module.exports = authenticate;
