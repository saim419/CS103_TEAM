const openai = require('openai');
console.log(input)
const generateClothingList = async (input) => {
    // Set up the OpenAI API client
    openai.apiKey = process.env.OPENAI_API_KEY;

    // Define the prompt for generating a list of shoes
    const prompt = `List the top 10 clothing items according to ${input}`;

    // Use the OpenAI API to generate a response
    const response = await openai.complete({
        engine: 'davinci',
        prompt: prompt,
        maxTokens: 200,
        n: 1,
        stop: '\n',
        temperature: 0.5,
    });

    // Extract the list of shoes from the response
    const clothingList = response.choices[0].text.trim();

    // Return the generated shoe list
    return clothingList;
};

module.exports = { generateClothingList };
