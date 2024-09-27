const express = require('express');
const app = express();
const port = process.env.PORT || 5000;

app.get('/api', (req, res) => {
  res.json({ message: "This is my boy Jog" });
});

app.listen(port, () => {
  console.log(`Backend server is running on port ${port}`);
});
