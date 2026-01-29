var express = require('express');
var app = express();
app.listen(80);

require('date-utils');
let today = new Date()

var str_text = new String('<h1>シナリオ #3 チェックテスト</h1><br><br>')

str_text = str_text + "テスト時の時刻は、"
str_text = str_text + today.toFormat('YYYY年MM月DD日')+''
str_text= str_text + '　■■時■■分です。'

app.get('/',(req,res)=>{
    //res.send(str_text = today.toFormat('YYYY年MM月DD日\n'))
    res.send(str_text)
    res.send('Content-Type', 'text/plain;charset=utf-8');
    res.end();
})