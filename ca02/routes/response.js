const express = require('express');
const router = express.Router();
const { generateClothingList } = require('../generateClothingList');

router.get('/', (req, res) => {
    res.render('response', { response: '' });
});

router.post('/', async (req, res) => {
    const input = req.body.input;
    const clothingList = await generateClothingList(input);
    res.json({ clothingList });
});

module.exports = router;
