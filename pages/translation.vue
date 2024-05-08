<template>
    <div class="relative z-10 max-w-screen-sm">
      <p v-if="user" class="fVeafc in">Hi, {{ user.user_metadata.first_name }}</p>
      <p v-else class="fVeafc">unauthenticated</p>
      <!-- <h1 class="kKxhrq">
        TRANSLATION
      </h1>
      <p class="kRTmDC">
        You can use our translation software to convert multiple dialects to Mandarin, and also learn and practice on our platform. We also provide AI based exam scoring functions.
      </p> -->
      <br><br>
      <h1 class="text-2xl font-bold text-center text-blue-800">Cantonese Translation Model</h1>
    <p class="text-gray-600 text-center mt-2">
      Use our AI-powered tools to translate text into Cantonese, enhance your language skills, or prepare for exams.
    </p>

        <div class="flex justify-center items-center mt-6">
      <textarea v-model="inputText" class="border p-2 w-full max-w-lg" placeholder="Enter text here..." rows="4"></textarea>
    </div>
    <div class="text-center my-4">
      <button @click="translateText" :disabled="loading" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Translate
      </button>
    </div>

    <div v-if="translation" class="max-w-lg mx-auto mt-4">
      <h2 class="text-lg font-semibold">Translation:</h2>
      <p class="border p-2">{{ translation }}</p>
    </div>
      <br><br><br><br>
      <div>
        <NuxtLink to="/home">
          <button class="ieMfVH">
            <span class="fKlELC">
              Back
            </span>
          </button>
        </NuxtLink>
    </div>
    </div>
  </template>
  
  <script setup lang="ts">

import { ref } from 'vue';
// import { useSupabaseAuthClient } from '@/composables/useSupabaseAuth';
import axios from 'axios';
import md5 from 'md5';

const inputText = ref('');
const translation = ref('');
const loading = ref(false);

const appid = '20240508002045408';
const key = 'ITW006BC5yVWRL93P4pX';
const apiUrl = 'https://api.fanyi.baidu.com/api/trans/vip/translate';

const client = useSupabaseAuthClient()
const user = useSupabaseUser()
  // const client = useSupabaseAuthClient()
  
  async function translateText() {
  if (!inputText.value.trim()) return;
  loading.value = true;
  const salt = Date.now();
  const sign = md5(`${appid}${inputText.value}${salt}${key}`);
  try {
    const response = await axios.get(apiUrl, {
      params: {
        q: inputText.value,
        from: 'en',
        to: 'yue', // Cantonese
        appid: appid,
        salt: salt,
        sign: sign
      }
    });
    if (response.data && response.data.trans_result) {
      translation.value = response.data.trans_result[0].dst;
    } else {
      console.error('No translation result:', response.data);
      translation.value = 'No translation result returned.';
    }
  } catch (error) {
    console.error('Translation error:', error);
    translation.value = 'Translation failed: ' + (error.response?.data?.error_msg || error.message);
  }
  loading.value = false;
}
const logout = async () => {
  loading.value = true
  const { error } = await client.auth.signOut()
  if (error) {
    loading.value = false
    return alert('Something went wrong !')
  }
}
  
  useHead({
    title: 'Translation',
    meta: [
      { name: 'description', content: 'You can use our translation software to convert multiple dialects to Mandarin, and also learn and practice on our platform. We also provide AI based exam scoring functions.' }
    ]
  })
  </script>

  <style scoped>
  .container {
    max-width: 640px;
  }
  </style>