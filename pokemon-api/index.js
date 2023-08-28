const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Require your cards router
const cardsRouter = require('./cards');
app.use('/api/cards', cardsRouter);

app.listen(PORT, () => {
    console.log('Server is running on port ${PORT}');
});
