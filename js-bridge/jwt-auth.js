const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const users = require('./users');

const JWT_SECRET = process.env.JWT_SECRET || "superjwtsecret";
const JWT_EXPIRE = '15m';
const JWT_REFRESH_SECRET = process.env.JWT_REFRESH_SECRET || "refreshjwtsecret";
const JWT_REFRESH_EXPIRE = '7d';

function authenticateJWT(req, res, next) {
  const token = req.headers['authorization']?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'Missing token' });
  jwt.verify(token, JWT_SECRET, (err, user) => {
    if (err) return res.status(403).json({ error: 'Invalid token' });
    req.user = user;
    next();
  });
}

function issueTokens(user) {
  const accessToken = jwt.sign({ id: user.id, username: user.username }, JWT_SECRET, { expiresIn: JWT_EXPIRE });
  const refreshToken = jwt.sign({ id: user.id }, JWT_REFRESH_SECRET, { expiresIn: JWT_REFRESH_EXPIRE });
  return { accessToken, refreshToken };
}

function addAuthRoutes(app) {
  app.post('/auth/login', async (req, res) => {
    const { username, password } = req.body;
    const user = users.find(u => u.username === username);
    if (!user) return res.status(401).json({ error: 'Invalid credentials' });
    if (!(await bcrypt.compare(password, user.passwordHash))) return res.status(401).json({ error: 'Invalid credentials' });
    res.json(issueTokens(user));
  });
  app.post('/auth/refresh', (req, res) => {
    const token = req.body.refreshToken;
    if (!token) return res.status(401).json({ error: 'Missing token' });
    jwt.verify(token, JWT_REFRESH_SECRET, (err, user) => {
      if (err) return res.status(403).json({ error: 'Invalid token' });
      const realUser = users.find(u => u.id === user.id);
      if (!realUser) return res.status(401).json({ error: 'User not found' });
      res.json(issueTokens(realUser));
    });
  });
}

module.exports = { authenticateJWT, addAuthRoutes };
