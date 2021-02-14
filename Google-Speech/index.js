// Link: https://cloud.google.com/speech-to-text/docs/async-recognize#speech_transcribe_async_gcs-nodejs

// Imports the Google Cloud client library
// const speech = require('@google-cloud/speech');
const corpus_for_Dec_4th = 
[
  'snap', 
  'light wave', 
  'light waves', 
  'project', 
  'sprite', 
  'create', 
  'code', 
  'codes', 
  'main', 
  'intensity', 
  'color', 
  'amplitude', 
  'frequency', 
  'speed', 
  'speeds',
  'wavelength', 
  'slide', 
  'slider', 
  'iamge', 
  'images',
  'set', 
  'observe', 
  'brightness', 
  'intensity', 
  'bright', 
  'too bright', 
  'perfect', 
  'too dark', 
  'violet', 
  'blue',
  'green',
  'yellow',
  'orange',
  'red',
  'spectrum',
  'block',
  'click',
  'open',
  'go to', 
  'oh', 
  'okay', 
  'right', 
  'like', 
  'yeah', 
  'one', 
  'number', 
  'blah', 
  'wait', 
  'amplitude', 
  'um', 
  'say', 
  'wave', 
  'good', 
  'yeet', 
  'press', 
  'got', 
  'lagging', 
  'color', 
  'two', 
  'blah blah', 
  'number number', 
  'oh god', 
  'oh yeah', 
  'oh okay', 
  'oh oh', 
  'main sprite', 
  'right amplitude', 
  'right good', 
  'say say', 
  'one front', 
  'wave form', 
  'right oh', 
  'one number', 
  'wow wow', 
  'dope dope', 
  'stop stop', 
  'steve harvey', 
  'okay okay', 
  'right right'
]

const corpus_for_Dec_11th = 
[
  'snap',  
  'project', 
  'sprite', 
  'sprites',
  'create', 
  'upload',
  'running',
  'code', 
  'codes',
  'activity',
  'main', 
  'message',
  'model',
  'variable',
  'variables',
  'water',
  'sugar',
  'body temperature',
  'sweat',
  'homeostasis',
  'change',
  'changes',
  'default',
  'maintain',
  'maintaining',
  'speed', 
  'speeds',
  'excercise level',
  'wait time',
  'character',
  'need water',
  'iamge', 
  'images',
  'set', 
  'increase',
  'okay', 
  'yeah', 
  'one', 
  'temperature', 
  'water', 
  'like', 
  'number', 
  'wait', 
  'going', 
  'oh', 
  'level', 
  'body', 
  'go', 
  'make', 
  'sweat', 
  'need', 
  'want', 
  'sugar', 
  'think', 
  'part', 
  'body temperature', 
  'wait wait', 
  'water level', 
  'okay okay', 
  'exercise level', 
  'one okay', 
  'set sweat', 
  'going die', 
  'oh wait', 
  'yeah yeah', 
  'temperature sweat', 
  'sweat okay', 
  'okay make', 
  'sugar water', 
  'homeostasis one', 
  'want see', 
  'first part', 
  'level number', 
  'go okay', 
  'okay think'
]

const corpus_for_Feb_2019 = 
[
  'snap',  
  'project', 
  'sprite', 
  'sprites',
  'create', 
  'upload',
  'running',
  'code', 
  'codes',
  'activity',
  'beak',
  'evolution',
  'bird',
  'birds',
  'length',
  'repreduce',
  'clone',
  'die',
  'identical',
  'parent',
  'variable',
  'variables',
  'randomly',
  'generate',
  'average beak size',
  'prompt',
  'click on',
  'log in',
  'image',
  'images',
  'background',
  'upload',
  'generation',
  'different',
  'survival',
  'count the clones',
  'beak length',
  'timer',
  'counter',
  'animation',
  'spawned',
  'spawn',
  'average beak',
  'short',
  'shorter',
  'merge',
  'merging',
  'combine',
  'create a variable',
  'clone', 
  'beak', 
  'one', 
  'like', 
  'length', 
  'yeah', 
  'wait', 
  'eight', 
  'right', 
  'change', 
  'um', 
  'okay', 
  'oh', 
  'go', 
  'counter', 
  'two', 
  'size', 
  'click', 
  'new', 
  'number', 
  'beak length', 
  'clone counter', 
  'beak size', 
  'new beak', 
  'create clone', 
  'start clone', 
  'delete clone', 
  'every time', 
  'five seconds', 
  'less eight', 
  'change beak', 
  'wait five', 
  'gon na', 
  'let try', 
  'larger eight', 
  'original one', 
  'go back', 
  'oh wait', 
  'yeah wait', 
  'counter one'
]

const speech = require('@google-cloud/speech').v1p1beta1;

async function main(){

// Creates a client
const client = new speech.SpeechClient();

const gcsUri = 'gs://yingbo_test_audio/t099 t107 group audio fixed.wav';

const basic_config = {
  encoding: 'LINEAR16',
  sampleRateHertz: 16000,
  languageCode: 'en-US',
}

const advanced_config = {
  enableWordTimeOffsets: true,
  encoding: 'LINEAR16',
  sampleRateHertz: 16000,
  languageCode: 'en-US',
  enableSpeakerDiarization: true,
  diarizationSpeakerCount: 2,
  audioChannelCount: 1,
  model:'video',
  useEnhanced: true,
  enableWordConfidence: true,
  "speechContexts": [{
    "phrases": corpus_for_Dec_11th
  }]
};

const audio = {
  uri: gcsUri,
};

const request = {
  config: advanced_config,
  audio: audio,
};

// Detects speech in the audio file. This creates a recognition job that you can wait for now, or get its result later.
const [operation] = await client.longRunningRecognize(request);
// Get a Promise representation of the final result of the job
const [response] = await operation.promise();
const transcription = response.results
  .map(result => result.alternatives[0].transcript)
  .join('\n');
const confidence = response.results
  .map(result => result.alternatives[0].confidence)
  .join('\n');
console.log(`Transcription: ${transcription} \n Confidence: ${confidence}`);

console.log('Word-Level-Confidence:');
const words = response.results.map(result => result.alternatives[0]);

for (var i = 0; i < words.length; i++){
  console.log(`Word Confidence for ` + i + 'th sentence');
  words[i].words.forEach(a => {
    console.log(` word: ${a.word}, confidence: ${a.confidence}`);
  });
}

console.log('Speaker Diarization:');
const result = response.results[response.results.length - 1];
const wordsInfo = result.alternatives[0].words;
// Note: The transcript within each result is separate and sequential per result.
// However, the words list within an alternative includes all the words
// from all the results thus far. Thus, to get all the words with speaker
// tags, you only have to take the words list from the last result:
wordsInfo.forEach(a =>
  console.log(` word: ${a.word}, speakerTag: ${a.speakerTag}`)
);

result.alternatives[0].words.forEach(wordInfo => {
  // NOTE: If you have a time offset exceeding 2^32 seconds, use the
  // wordInfo.{x}Time.seconds.high to calculate seconds.
  const startSecs =
    `${wordInfo.startTime.seconds}` +
    '.' +
    wordInfo.startTime.nanos / 100000000;
  const endSecs =
    `${wordInfo.endTime.seconds}` +
    '.' +
    wordInfo.endTime.nanos / 100000000;
  console.log(`Word: ${wordInfo.word}`);
  console.log(`\t ${startSecs} secs - ${endSecs} secs`);
});
}

main().catch(console.error);
