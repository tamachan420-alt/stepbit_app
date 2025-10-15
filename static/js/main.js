async function fetchJSON(url, options={}){
  const res = await fetch(url, options);
  if(!res.ok) throw new Error('HTTP ' + res.status);
  return await res.json();
}

async function loadChallenges(){
  try{
    const list = await fetchJSON('/api/challenges');
    const box = document.getElementById('challengeList');
    if(!box) return;
    box.innerHTML = '';
    list.forEach(item => {
      const div = document.createElement('div');
      div.textContent = `${item.title}  ${item.date || ''}  [${item.status}]`;
      box.appendChild(div);
    });
  }catch(e){ console.error(e); }
}

async function addChallenge(){
  const input = document.getElementById('challengeTitle');
  if(!input || !input.value.trim()) return;
  await fetchJSON('/api/challenges', {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body: JSON.stringify({title: input.value.trim()})
  });
  input.value='';
  loadChallenges();
}

async function askAI(){
  const mood = document.getElementById('mood')?.value || 'ふつう';
  const data = await fetchJSON('/api/suggest', {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body: JSON.stringify({mood})
  });
  const out = document.getElementById('aiSuggestion');
  if(out) out.textContent = data.suggestion;
}

document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('addBtn')?.addEventListener('click', addChallenge);
  document.getElementById('aiBtn')?.addEventListener('click', askAI);
  loadChallenges();
});

// === 🎯 今日のチャレンジをAIにお願いする関数 ===
async function getSuggestion() {
  const res = await fetch("/api/suggest", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      name: "たま",
      goal: "笑顔で過ごす",
      mood: "やる気が出ない"
    })
  });
  const data = await res.json();
  console.log("AIの提案：", data.suggestion);
  return data.suggestion;
}

// === 💬 実施結果のコメントをAIにもらう関数 ===
async function getComment() {
  const res = await fetch("/api/comment", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      name: "たま",
      goal: "笑顔で過ごす",
      result: "できた",   // ← ここは後でUIから変えられるようにする
      dialect: "imabari"  // ← .envの設定に合わせてもOK
    })
  });
  const data = await res.json();
  console.log("AIのコメント：", data.comment);
  return data.comment;
}

