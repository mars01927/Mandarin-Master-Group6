<template>
    <div class="relative z-10 max-w-screen-sm">
      <p v-if="user" class="fVeafc in">Hi, {{ user.user_metadata.first_name }}</p>
      <p v-else class="fVeafc">unauthenticated</p>
      <h1 class="kKxhrq">
        PRACTICE
      </h1>
      <p class="kRTmDC">
        Click any button to listen to Cantonese pronunciation.
      </p>
      <br>
      <p class="kRTmDC">
        Phrase:
      </p>

  <div class="uQxNj" v-if="user">
    <audio ref="audioPlayer1" src="/voice/bykq.wav"></audio>
        <button @click="playSound1" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            不用客气
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>

        <audio ref="audioPlayer2" src="/voice/fcgx.wav"></audio>
        <button @click="playSound2" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            非常感谢
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>

        <audio ref="audioPlayer3" src="/voice/njwykm.wav"></audio>
        <button @click="playSound3" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            今晚有空吗？
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>

        <audio ref="audioPlayer4" src="/voice/nclm.wav"></audio>
        <button @click="playSound4" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            你吃了吗？
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>

        <audio ref="audioPlayer5" src="/voice/njsmmz.wav"></audio>
        <button @click="playSound5" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            你叫什么名字？
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>

        <audio ref="audioPlayer6" src="/voice/nzznl.wav"></audio>
        <button @click="playSound6" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            你住在哪里?
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>

        <audio ref="audioPlayer7" src="/voice/qnla.wav"></audio>
        <button @click="playSound7" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            去哪里啊?
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>

        <audio ref="audioPlayer8" src="/voice/wbzd.wav"></audio>
        <button @click="playSound8" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            我不知道
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>

        <audio ref="audioPlayer9" src="/voice/wcdl.wav"></audio>
        <button @click="playSound9" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            我迟到了
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>

        <audio ref="audioPlayer10" src="/voice/wmzb.wav"></audio>
        <button @click="playSound10" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            我们走吧
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>

        </div>
        <br>

      <p class="kRTmDC">
        Sentence:
      </p>
      <div class="uQxNj" v-if="user">
    <audio ref="audioPlayer11" src="/voice/qwxsjznl.wav"></audio>
        <button @click="playSound11" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            请问洗手间在哪里？
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>

        <audio ref="audioPlayer12" src="/voice/wxdybkf.wav"></audio>
        <button @click="playSound12" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            我想点一杯咖啡
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>

        <audio ref="audioPlayer13" src="/voice/xxndbz.wav"></audio>
        <button @click="playSound13" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            谢谢你的帮助
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>

        <audio ref="audioPlayer14" src="/voice/zcnhm.wav"></audio>
        <button @click="playSound14" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            早晨，你好吗？
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>

        <audio ref="audioPlayer15" src="/voice/zgdsq.wav"></audio>
        <button @click="playSound15" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            这个多少钱？
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: var(--icon-color);">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>
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
  <!-- Thank you, Mr. Pani Xue, for your outstanding contribution to the audio of this feature. -->

  <script setup lang="ts">
  import { ref } from 'vue';
  
  const audioPlayer1 = ref(null);
  const playSound1 = () => {
    if (audioPlayer1.value) {
      audioPlayer1.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }

  const audioPlayer2 = ref(null);
  const playSound2 = () => {
    if (audioPlayer2.value) {
      audioPlayer2.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }
  const audioPlayer3 = ref(null);
  const playSound3 = () => {
    if (audioPlayer3.value) {
      audioPlayer3.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }
  const audioPlayer4 = ref(null);
  const playSound4 = () => {
    if (audioPlayer4.value) {
      audioPlayer4.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }
  const audioPlayer5 = ref(null);
  const playSound5 = () => {
    if (audioPlayer5.value) {
      audioPlayer5.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }
  const audioPlayer6 = ref(null);
  const playSound6 = () => {
    if (audioPlayer6.value) {
      audioPlayer6.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }
  const audioPlayer7 = ref(null);
  const playSound7 = () => {
    if (audioPlayer7.value) {
      audioPlayer7.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }
  const audioPlayer8 = ref(null);
  const playSound8 = () => {
    if (audioPlayer8.value) {
      audioPlayer8.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }
  const audioPlayer9 = ref(null);
  const playSound9 = () => {
    if (audioPlayer9.value) {
      audioPlayer9.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }
  const audioPlayer10 = ref(null);
  const playSound10 = () => {
    if (audioPlayer10.value) {
      audioPlayer10.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }
  const audioPlayer11 = ref(null);
  const playSound11 = () => {
    if (audioPlayer11.value) {
      audioPlayer11.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }
  const audioPlayer12 = ref(null);
  const playSound12 = () => {
    if (audioPlayer12.value) {
      audioPlayer12.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }
  const audioPlayer13 = ref(null);
  const playSound13 = () => {
    if (audioPlayer13.value) {
      audioPlayer13.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }
  const audioPlayer14 = ref(null);
  const playSound14 = () => {
    if (audioPlayer14.value) {
      audioPlayer14.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }
  const audioPlayer15 = ref(null);
  const playSound15 = () => {
    if (audioPlayer15.value) {
      audioPlayer15.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
  }

  const client = useSupabaseAuthClient()
  const user = useSupabaseUser()
  const loading = ref(false)

  
  useHead({
    title: 'Practice',
    meta: [
      { name: 'description', content: 'You can use our translation software to convert multiple dialects to Mandarin, and also learn and practice on our platform. We also provide AI based exam scoring functions.' }
    ]
  })
  </script>