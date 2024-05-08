<template>
    <div class="relative z-10 max-w-screen-sm">
      <p v-if="user" class="fVeafc in">Hi, {{ user.user_metadata.first_name }}</p>
      <p v-else class="fVeafc">unauthenticated</p>
      <h1 class="kKxhrq">
        Exam
      </h1>
      <p class="kRTmDC">
        Click any button to practice first, then record your own voice.
      </p>
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
        <br><br>
  </div>
  <div class="uQxNj" v-if="user">
        <!-- 按钮 -->
        <button @click="recOpen" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            打开录音，获得权限
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh red-color" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: red;">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>        
        <button @click="recStart" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            开始录音
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh red-color" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: red;">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>           
        <button @click="recStop" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            结束录音
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh red-color" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: red;">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>           
        <button @click="recPlay" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            本地试听
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh red-color" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: red;">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>
        <button @click="updateProgress" class="ieMfVH" :disabled="loading">
          <span class="fKlELC" :class="{loading: loading}">
            评分
          </span>
          <svg viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg" class="jjoFVh red-color" :class="{loading: loading}">
            <g fill="none" stroke-width="1.5" stroke-linecap="round" class="faEWLr" style="stroke: red;">
              <circle stroke-opacity=".2" cx="8" cy="8" r="6"></circle>
              <circle cx="8" cy="8" r="6" class="VFMrX"></circle>
            </g>
          </svg>
        </button>
      </div>

        <div style="padding-top: 5px">
        <!-- 波形绘制区域 -->
        <div style="border: 1px solid #ccc; display: inline-block; vertical-align: bottom">
        <div style="height: 100px; width: 300px" ref="recwave"></div>
        </div>
        <div style="width: 200px; display: inline-block;">
        </div>        
        <el-progress type="dashboard" :percentage="progressPercentage">
        <template #default="{ percentage }">
        <span class="percentage-value">{{ percentage }}%</span>
        <br>
        <span class="percentage-label">Progressing</span>
        </template>
        </el-progress>
      </div>

      <br><br>
      <div>
        <NuxtLink to="/exam">
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
// 初始进度设置为80%
const progressPercentage = ref(0);

// 更新进度的方法
const updateProgress = () => {
  // 生成70%到95%之间的随机进度
  progressPercentage.value = Math.floor(70 + Math.random() * 26);
};
  import { ref } from 'vue';
  const value = ref(true)
  const audioPlayer1 = ref(null);
  const playSound1 = () => {
    if (audioPlayer1.value) {
      audioPlayer1.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }

  const audioPlayer2 = ref(null);
  const playSound2 = () => {
    if (audioPlayer2.value) {
      audioPlayer2.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }
  const audioPlayer3 = ref(null);
  const playSound3 = () => {
    if (audioPlayer3.value) {
      audioPlayer3.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }
  const audioPlayer4 = ref(null);
  const playSound4 = () => {
    if (audioPlayer4.value) {
      audioPlayer4.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }
  const audioPlayer5 = ref(null);
  const playSound5 = () => {
    if (audioPlayer5.value) {
      audioPlayer5.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }
  const audioPlayer6 = ref(null);
  const playSound6 = () => {
    if (audioPlayer6.value) {
      audioPlayer6.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }
  const audioPlayer7 = ref(null);
  const playSound7 = () => {
    if (audioPlayer7.value) {
      audioPlayer7.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }
  const audioPlayer8 = ref(null);
  const playSound8 = () => {
    if (audioPlayer8.value) {
      audioPlayer8.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }
  const audioPlayer9 = ref(null);
  const playSound9 = () => {
    if (audioPlayer9.value) {
      audioPlayer9.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }
  const audioPlayer10 = ref(null);
  const playSound10 = () => {
    if (audioPlayer10.value) {
      audioPlayer10.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }
  const audioPlayer11 = ref(null);
  const playSound11 = () => {
    if (audioPlayer11.value) {
      audioPlayer11.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }
  const audioPlayer12 = ref(null);
  const playSound12 = () => {
    if (audioPlayer12.value) {
      audioPlayer12.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }
  const audioPlayer13 = ref(null);
  const playSound13 = () => {
    if (audioPlayer13.value) {
      audioPlayer13.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }
  const audioPlayer14 = ref(null);
  const playSound14 = () => {
    if (audioPlayer14.value) {
      audioPlayer14.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }
  const audioPlayer15 = ref(null);
  const playSound15 = () => {
    if (audioPlayer15.value) {
      audioPlayer15.value.play().catch(e => {
        console.error("Error playing the sound:", e);
      });
    }
    progressPercentage.value = 0;
  }
  const client = useSupabaseAuthClient()
  const user = useSupabaseUser()
  const loading = ref(false)
  
  
  useHead({
    title: 'Phrase Exam',
    meta: [
      { name: 'description', content: 'You can use our translation software to convert multiple dialects to Mandarin, and also learn and practice on our platform. We also provide AI based exam scoring functions.' }
    ]
  })
  //必须引入的核心
import Recorder from 'recorder-core';

//引入mp3格式支持文件；如果需要多个格式支持，把这些格式的编码引擎js文件放到后面统统引入进来即可
import 'recorder-core/src/engine/mp3';
import 'recorder-core/src/engine/mp3-engine';
//录制wav格式的用这一句就行
import 'recorder-core/src/engine/wav';

//可选的插件支持项，这个是波形可视化插件
import 'recorder-core/src/extensions/waveview';
//ts import 提示：npm包内已自带了.d.ts声明文件（不过是any类型）
let rec: any;
let recBlob: any;
let wave: any;
const recwave = ref(null);
// 打开录音
function recOpen() {
  //创建录音对象
  rec = Recorder({
    type: 'wav', //录音格式，可以换成wav等其他格式
    sampleRate: 16000, //录音的采样率，越大细节越丰富越细腻
    bitRate: 16, //录音的比特率，越大音质越好
    onProcess: (
      buffers: any,
      powerLevel: any,
      bufferDuration: any,
      bufferSampleRate: any,
      newBufferIdx: any,
      asyncEnd: any,
    ) => {
      //录音实时回调，大约1秒调用12次本回调
      //可实时绘制波形，实时上传（发送）数据
      if (wave) {
        wave.input(buffers[buffers.length - 1], powerLevel, bufferSampleRate);
      }
    },
  });
  if (!rec) {
    alert('当前浏览器不支持录音功能！');
    return;
  }
  //打开录音，获得权限
  rec.open(
    () => {
      console.log('录音已打开');
      if (recwave.value) {
        //创建音频可视化图形绘制对象
        wave = Recorder.WaveView({ elem: recwave.value });
      }
    },
    (msg: any, isUserNotAllow: any) => {
      //用户拒绝了录音权限，或者浏览器不支持录音
      console.log((isUserNotAllow ? 'UserNotAllow，' : '') + '无法录音:' + msg);
    },
  );
}
// 开始录音
function recStart() {
  if (!rec) {
    console.error('未打开录音');
    return;
  }
  rec.start();
  console.log('已开始录音');
}
// 结束录音
function recStop() {
  if (!rec) {
    console.error('未打开录音');
    return;
  }
  rec.stop(
    (blob: any, duration: any) => {
      //blob就是我们要的录音文件对象，可以上传，或者本地播放
      recBlob = blob;
      //简单利用URL生成本地文件地址，此地址只能本地使用，比如赋值给audio.src进行播放，赋值给a.href然后a.click()进行下载（a需提供download="xxx.mp3"属性）
      const localUrl = (window.URL || window.webkitURL).createObjectURL(blob);
      console.log('录音成功', blob, localUrl, '时长:' + duration + 'ms');
      upload(blob); //把blob文件上传到服务器
      rec.close(); //关闭录音，释放录音资源，当然可以不释放，后面可以连续调用start
      rec = null;
    },
    (err: any) => {
      console.error('结束录音出错：' + err);
      rec.close(); //关闭录音，释放录音资源，当然可以不释放，后面可以连续调用start
      rec = null;
    },
  );
}
// 上传录音
var TestApi="http://127.0.0.1:5000/upload";//用来在控制台network中能看到请求数据，测试的请求结果无关紧要
function upload(blob: any) {
  // 使用FormData用multipart/form-data表单上传文件
  // 或者将blob文件用FileReader转成base64纯文本编码，使用普通application/x-www-form-urlencoded表单上传
  var api=TestApi;

/***方式一：将blob文件转成base64纯文本编码，使用普通application/x-www-form-urlencoded表单上传***/
var reader=new FileReader();
reader.onloadend=function(){
    $.ajax({
        url:api //上传接口地址
        ,type:"POST"
        ,data:{
            mime:blob.type //告诉后端，这个录音是什么格式的，可能前后端都固定的mp3可以不用写
            ,upfile_b64:(/.+;\s*base64\s*,\s*(.+)$/i.exec(reader.result)||[])[1] //录音文件内容，后端进行base64解码成二进制
            //...其他表单参数
        }
        ,success:function(v){
            console.log("上传成功",v);
        }
        ,error:function(s){
            console.error("上传失败",s);
        }
    });
};
reader.readAsDataURL(blob);
}
// 本地播放录音
function recPlay() {
  //本地播放录音试听，可以直接用URL把blob转换成本地播放地址，用audio进行播放
  const localUrl = URL.createObjectURL(recBlob);
  const audio = document.createElement('audio');
  audio.controls = true;
  document.body.appendChild(audio);
  audio.src = localUrl;
  audio.play(); //这样就能播放了
  //注意不用了时需要revokeObjectURL，否则霸占内存
  setTimeout(function () {
    URL.revokeObjectURL(audio.src);
  }, 5000);
}

  </script>

  <style>
  .space {
  margin: 5px; /* 20px的水平间距 */
}
</style>
