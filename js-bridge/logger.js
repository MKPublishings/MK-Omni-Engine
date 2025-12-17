function logEvent(event, meta = {}) {
  console.log(`[${new Date().toISOString()}] [${event}]`, meta);
}
module.exports = logEvent;
