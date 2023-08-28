const express = require('express');
const router = express.Router();
const axios = require('axios');

router.get('/:name', async (req, res) => {
    const pokemonName = req.params.name.toLowerCase();

    try {
        const response = await axios.get(`https://api.pokemontcg.io/v2/cards?q=name:${pokemonName}`);
        const cards = response.data.data;

        if (cards.length === 0) {
            res.status(404).json({error: 'Pokemon not found'});
            return;
        }

        const cardData = cards[0];
        res.json(cardData);
    } catch (error) {
        res.status(500).json({error: 'An error occurred'});
    }
});

module.exports = router;
