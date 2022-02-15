/*

	あ GK KASI CREDIT LORD ZENN, GK USAH RE UPLOAD
	あ SUSAH" NGE FIX, LU CUMA NUMPANG NAMA DOANG
	あ YANG BELUM PAHAM CAR RUN DI HEROKU TONTON AJA VIDEO SEBELUMNYA
	あ FITUR JUALAN TELAH DI HAPUS [ Bisa order sama saya klo mau ]
	
	あ JASA RUN HEROKU BISA PC wa.me/62887435047326 BIAR BOT NYA GAK TERLALU DELAY
	
*/   
const
	{
		WAConnection: _WAConnection,
		MessageType,
		Presence,
		MessageOptions,
		Mimetype,
		WALocationMessage,
		WA_MESSAGE_STUB_TYPES,
		WA_DEFAULT_EPHEMERAL,
		WAMessageProto,
		ReconnectMode,
		ChatModification,
		ProxyAgent,
		GroupSettingChange,
		waChatKey,
		relayWAMessage,
		mentionedJid,
		processTime
	} = require("@adiwajshing/baileys")
const qrcode = require("qrcode-terminal")
const moment = require("moment-timezone")
const speed = require('performance-now')
const crypto = require('crypto')
const request = require('request');
const { spawn, exec, execSync } = require("child_process")
const fs = require("fs")
const os = require('os')
const axios = require('axios').default
const cheerio = require("cheerio")
const Util = require('util')
const hx = require('hxz-api')
const ffmpeg = require('fluent-ffmpeg')
const { EmojiAPI } = require("emoji-api");
const ig = require('insta-fetcher')
const emoji = new EmojiAPI()
const fetch = require('node-fetch');
const simple = require('./lib/simple.js')
const _sewa = require("./lib/sewa");
const twitterGetUrl = require("twitter-url-direct")
const phoneNum = require('awesome-phonenumber')
const gis = require('g-i-s');
const got = require("got");
const imageToBase64 = require('image-to-base64');
const ID3Writer = require('browser-id3-writer');		
const brainly = require('brainly-scraper')
const yts = require( 'yt-search')
const ms = require('parse-ms')
const toMs = require('ms')
const util = require('util')
const { error } = require("qrcode-terminal")
const ytdl = require('ytdl-core');
const zee = require('api-alphabot')

const { getBuffer, h2k, generateMessageID, getGroupAdmins, getRandom, banner, start, info, success, close } = require('./lib/functions')
const { color, bgcolor } = require('./lib/color')
const {animek, fetchJson, getBase64, kyun, createExif } = require('./lib/fetcher')
const { yta, ytv, igdl, upload } = require('./lib/ytdl')
const { yta2, ytv2, ytv3, ytv4} = require('./lib/y2mate')
const { tiktokDown } = require("./lib/tiktok")
const { webp2mp4File} = require('./lib/webp2mp4')
const { mediafireDl} = require('./lib/mediafire.js')
const { msgFilter } = require('./lib/antispam')
const { virtex, vipi } = require('./lib/virtex.js')
const setTtt = require('./lib/tictactoe.js')
const off = require('./lib/afk.js')
let _off = JSON.parse(fs.readFileSync('./src/afk.json'))
const time = moment().tz('Asia/Jakarta').format("HH:mm:ss")
const ameClient = require("amethyste-api")
const ameApi = new ameClient("1f486b04b157f12adf0b1fe0bd83c92a28ce768683871d2a390e25614150d0c8fa404fd01b82a5ebf5b82cbfa22e365e611c8501225a93d5d1e87f9f420eb91b")
const { sleep, isAfk, cekafk, addafk } = require('./lib/offline')
const { addVote, delVote } = require('./lib/vote')
const { jadibot, stopjadibot, listjadibot } = require('./lib/jadibot')
const premium = require("./lib/premiun");
const { bytesToSize, TelegraPh, uploadImages } = require('./lib/uploadimage')
const { isLimit, limitAdd, getLimit, giveLimit, addBalance, kurangBalance, getBalance, isGame, gameAdd, givegame, cekGLimit } = require("./lib/about_user")
const { list_aov } = require('./shop/aov')
const { list_cod } = require('./shop/cod')
const { list_sausage } = require('./shop/sausage')
const { list_lol } = require('./shop/lol')
const { list_valo } = require('./shop/valo')
const { list_price } = require('./shop/price')
const { allpayment } = require('./shop/allpayment')
const { pc_sewa } = require('./shop/sewa')
const { gcbotwa } = require('./shop/grupbot')
const { donasibot } = require('./shop/donasi')
const { infobot } = require('./shop/infobot')
const { jadibut } = require('./shop/jadibot')

const balance = JSON.parse(fs.readFileSync('./database/balance.json'));
const glimit = JSON.parse(fs.readFileSync('./database/glimit.json'))
const limit = JSON.parse(fs.readFileSync('./database/limit.json'))
const register = JSON.parse(fs.readFileSync('./database/user/register.json'))
const  _premium = JSON.parse(fs.readFileSync('./src/premiun.json'));
const afk = JSON.parse(fs.readFileSync('./lib/off.json'))
const setting = JSON.parse(fs.readFileSync('./settings.json'))
const antilink = JSON.parse(fs.readFileSync('./src/antilink.json'))
const antivirtex = JSON.parse(fs.readFileSync("./src/antivirtex.json"))
const welkom = JSON.parse(fs.readFileSync('./src/welkom.json'))
let filter = JSON.parse(fs.readFileSync('./src/filter.json'))
const setiker = JSON.parse(fs.readFileSync('./temp/stik.json'))
const audionye = JSON.parse(fs.readFileSync('./temp/vn.json'))
const imagenye = JSON.parse(fs.readFileSync('./temp/image.json'))
const videonye = JSON.parse(fs.readFileSync('./temp/video.json'))
const sfilter = JSON.parse(fs.readFileSync('./src/sfilter.json'))
const gcdetect = JSON.parse(fs.readFileSync('./src/gcdetect.json'))
const absen = JSON.parse(fs.readFileSync('./src/absen.json'))
const tictactoe = JSON.parse(fs.readFileSync("./src/tictactoe.json"))
const _win = JSON.parse(fs.readFileSync('./src/tttwin.json'))
const _lose = JSON.parse(fs.readFileSync('./src/tttlose.json'))
const voting = JSON.parse(fs.readFileSync('./lib/voting.json'))
const scommand = JSON.parse(fs.readFileSync('./lib/scommand.json'))
const banned = JSON.parse(fs.readFileSync('./src/banned.json'))
const _nsfw = JSON.parse(fs.readFileSync('./src/nsfw.json'))
const _leveling = JSON.parse(fs.readFileSync('./src/leveling.json'))
const _level = JSON.parse(fs.readFileSync('./src/level.json'))
const tebakgambar = JSON.parse(fs.readFileSync('./src/tebakgambar.json'))
const caklontong = JSON.parse(fs.readFileSync('./src/caklontong.json'))
const family = JSON.parse(fs.readFileSync('./src/family100.json'))
const siapakahaku = JSON.parse(fs.readFileSync('./src/siapakahaku.json'))
const tebakanime = JSON.parse(fs.readFileSync('./src/tebakanime.json'))
const tebakkalimat = JSON.parse(fs.readFileSync('./src/tebakkalimat.json'))
const tebakkata = JSON.parse(fs.readFileSync('./src/tebakkata.json'))
const tebaklirik = JSON.parse(fs.readFileSync('./src/tebaklirik.json'))
const tekateki = JSON.parse(fs.readFileSync('./src/tekateki.json'))
const susunkata = JSON.parse(fs.readFileSync('./src/susunkata.json'))

const  sewa = JSON.parse(fs.readFileSync('./src/sewa.json'));
const event = JSON.parse(fs.readFileSync('./src/event.json'))


//var creatorList = ['Creator WhatsApp Bot', 'Whatsapp Bot Indonesia', 'Creator Bot' , ' Bot WhatsApp']
var creator = setting.ownername
const  { ind, eng, es, ml, ru, pt } = require(`./language`)
lang = ind //language
const Exif = require('./lib/exif')
const exif = new Exif()
require('./config')

//set_sticker_command//
cmd_stc_menu = '7446'
cmd_stc_ping = '7292'
cmd_stc_play_music = '8046'
cmd_stc_group_close = '7850'
cmd_stc_group_open = '7878'
cmd_stc_image_to_sticker = '7688'
cmd_stc_to_image = '6964'
cmd_stc_self = '7038'
cmd_stc_public = '7144'
//set_sticker_command//
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    /*
SEBAGIAN LU EDIT DI SETTING.JSON
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      */                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
zeksApikey = 'Alphabott' //ganti pake apikey lu biar limitnya gk cepet abis 
ApiZeks = 'https://api.zeks.me' // regis disini klo mau dapat apikeynya
thumbnail = setting.thumb
pp_bot = fs.readFileSync(`image/${thumbnail}`)
pp_bot2 = fs.readFileSync(`image/${setting.thumbnail}`)
fthumb = setting.fakethumb
hit_today = []
blocked = []
ban = []
limitawal = "50"
gcounttprem = "50" 
gcounttuser = "25" 

let multi = true
let nopref = false
let single = false
let prefa = setting.prefix
let menusimple = false
let Mloc = false
let autobio = setting.autobio
let antihidetag = setting.antihidetag

banChats = setting.self_mode
autorespon = true
offline = false
readGc = true 
readPc = false 
antitrol = false 
bugc = false
autovn = true
autoketik = false
autoregister = setting.user_register
typemenu = 'document'
img = setting.img
baper = setting.ownername
apiku = 'https://zeeoneofc.github.io/'
gc_wa_lu = 'https://chat.whatsapp.com/EU890BcXjyBDkNaUT5WmYV' //klo gk punya gc wa gk usah di ganti 👍
targetpc = setting.ownerNumberr
owner = targetpc
fake = setting.fake
numbernye = '0'
waktu = 'Nothing'
alasan = 'Nothing'
botname = setting.botname
ownername = setting.ownername
peknem = setting.ownername
ownerNumber = setting.ownerNumber
cr = setting.cr
petik = '```'
titik =`...`
enter ='\n'
msgId="B826873620DD5947E683E3ABE663F263"
tttawal= ["0️⃣","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣"]
const X = "❌" 
const O = "⭕️" 
const tunjuk = "👈" 
winawal = 1 
loseawal = 1 
memberwin = 1 
memberlose = 1 

//Credit For 404 SQUAD ( Gk usah di hapus mek)
//Lingz
//Felix
//Lenz
//Arya
const uang = JSON.parse(fs.readFileSync('./database/user/uang.json'))
const ikan = JSON.parse(fs.readFileSync('./database/user/ikan.json'))
const planet = JSON.parse(fs.readFileSync('./database/user/planet.json'))
const coal = JSON.parse(fs.readFileSync('./database/user/coal.json'))
const stone = JSON.parse(fs.readFileSync('./database/user/stone.json'))
const ore = JSON.parse(fs.readFileSync('./database/user/ore.json'))
const ingot = JSON.parse(fs.readFileSync('./database/user/ingot.json'))
const kayu = JSON.parse(fs.readFileSync('./database/user/kayu.json'))

//=================================================//
module.exports = alpha = async (alpha, mek) => {
	try {
        if (!mek.hasNewMessage) return
        mek = mek.messages.all()[0]
        if (!mek.message) return
		if (mek.key && mek.key.remoteJid == 'status@broadcast') return
		global.blocked
		m = simple.smsg(alpha, mek)
		let { mentioned } = m
		bail = m.isBaileys
        mek.message = (Object.keys(mek.message)[0] === 'ephemeralMessage') ? mek.message.ephemeralMessage.message : mek.message
        const content = JSON.stringify(mek.message)
		const from = mek.key.remoteJid
		const { text, extendedText, contact, location, liveLocation, image, video, sticker, document, audio, product } = MessageType
		const time = moment.tz('Asia/Jakarta').format('DD/MM HH:mm:ss')
        const type = Object.keys(mek.message)[0]
               const addCmd = (id, command) => {
    const obj = { id: id, chats: command }
    scommand.push(obj)
    fs.writeFileSync('./lib/scommand.json', JSON.stringify(scommand))
}

const getCommandPosition = (id) => {
    let position = null
    Object.keys(scommand).forEach((i) => {
        if (scommand[i].id === id) {
            position = i
        }
    })
    if (position !== null) {
        return position
    }
}

const getCmd = (id) => {
    let position = null
    Object.keys(scommand).forEach((i) => {
        if (scommand[i].id === id) {
            position = i
        }
    })
    if (position !== null) {
        return scommand[position].chats
    }
}


const checkSCommand = (id) => {
    let status = false
    Object.keys(scommand).forEach((i) => {
        if (scommand[i].id === id) {
            status = true
        }
    })
    return status
}
        const cmd = (type === 'conversation' && mek.message.conversation) ? mek.message.conversation : (type == 'imageMessage') && mek.message.imageMessage.caption ? mek.message.imageMessage.caption : (type == 'videoMessage') && mek.message.videoMessage.caption ? mek.message.videoMessage.caption : (type == 'extendedTextMessage') && mek.message.extendedTextMessage.text ? mek.message.extendedTextMessage.text : (type == 'stickerMessage') && (getCmd(mek.message.stickerMessage.fileSha256.toString('hex')) !== null && getCmd(mek.message.stickerMessage.fileSha256.toString('base64')) !== undefined) ? getCmd(mek.message.stickerMessage.fileSha256.toString('base64')) : "".slice(1).trim().split(/ +/).shift().toLowerCase()
        if(multi){
		var prefix = /^[°•π÷×¶∆£¢€¥®™✓=|~zZ+×_!#%^&./\\©^]/.test(cmd) ? cmd.match(/^[°•π÷×¶∆£¢€¥®™✓=|~xzZ+×_!#,|`÷?;:%^&./\\©^]/gi) : '-'	  
		} else {
		if (nopref){
		prefix = ' '
		} else {
		if(single){
		prefix = prefa
		}
		}
		}
		
const reply2 = (teks) => {
            alpha.sendMessage(from, teks, text, {quoted: mek, contextInfo: {"forwardingScore":999,"isForwarded":true},sendEphemeral: true})
        }
// Auto Read Group 
var chats = await alpha.chats.array.filter(v => v.jid.endsWith('g.us'))
chats.map( async ({ jid }) => {
if (readGc === false) return
await alpha.chatRead(jid)
})
// Auto Read Private 
var chatss = await alpha.chats.array.filter(v => v.jid.endsWith('s.whatsapp.net'))
chatss.map( async ({ jid }) => {
if (readPc === false) return
await alpha.chatRead(jid)
})
if ((Object.keys(mek.message)[0] === 'ephemeralMessage' && JSON.stringify(mek.message).includes('EPHEMERAL_SETTING')) && mek.message.ephemeralMessage.message.protocolMessage.type === 3) {
if (bugc === false) return
if (mek.key.fromMe) return
nums = mek.participant
longkapnye = "\n".repeat(420)
tekuss = `${longkapnye}\`\`\`B U G  G C  T E R D E T E K S I\`\`\`\n@⁨${nums.split('@')[0]} akan dikick\n\n_Clear chat by bot_\n*Jangan maen bug lah*`
alpha.groupRemove(mek.key.remoteJid, [nums]).catch((e) => { reply2(`Gua mau kick tapi gua bukan admin 🤙`) })
alpha.sendMessage(mek.key.remoteJid, 'WAH BUG NIH', MessageType.text)
alpha.sendMessage(mek.key.remoteJid, tekuss, MessageType.text, {contextInfo:{mentionedJid:[nums + "@s.whatsapp.net"]}})
}

if (m.message && m.isBaileys && m.quoted && m.quoted.mtype === 'orderMessage' && !(m.quoted.token && m.quoted.orderId)) {
if (antitrol === false) return
if (mek.key.fromMe) return
reply2('Fake Troli Detected \n\n' + require('util').format(m.key))
await alpha.modifyChat(m.chat, 'delete', {
includeStarred: false
})
}

if (autovn) {
	if (autovn === false) return
await alpha.updatePresence(from, Presence.recording)
} else if (autoketik) {
	if (autoketik === false) return
await alpha.updatePresence(from, Presence.composing)
}
        body = type === "conversation" && mek.message.conversation.startsWith(prefix) ? mek.message.conversation : type == "imageMessage" && mek.message.imageMessage.caption.startsWith(prefix) ? mek.message.imageMessage.caption : type == "videoMessage" && mek.message.videoMessage.caption.startsWith(prefix) ? mek.message.videoMessage.caption : type == "extendedTextMessage" && mek.message.extendedTextMessage.text.startsWith(prefix) ? mek.message.extendedTextMessage.text : type == "buttonsResponseMessage" && mek.message[type].selectedButtonId ? mek.message[type].selectedButtonId : type == "listResponseMessage" ? mek.message.listResponseMessage.singleSelectReply.selectedRowId: type == "stickerMessage" && getCmd(mek.message[type].fileSha256.toString("base64")) !== null && getCmd(mek.message[type].fileSha256.toString("base64")) !== undefined ? getCmd(mek.message[type].fileSha256.toString("base64")) : "";
		budy = (type === 'conversation') ? mek.message.conversation : (type === 'extendedTextMessage') ? mek.message.extendedTextMessage.text : ''
		var pes = (type === 'conversation' && mek.message.conversation) ? mek.message.conversation : (type == 'imageMessage') && mek.message.imageMessage.caption ? mek.message.imageMessage.caption : (type == 'videoMessage') && mek.message.videoMessage.caption ? mek.message.videoMessage.caption : (type == 'extendedTextMessage') && mek.message.extendedTextMessage.text ? mek.message.extendedTextMessage.text : ''
		chatxs = (type === 'conversation' && mek.message.conversation) ? mek.message.conversation : (type == 'imageMessage') && mek.message.imageMessage.caption ? mek.message.imageMessage.caption : (type == 'documentMessage') && mek.message.documentMessage.caption ? mek.message.documentMessage.caption : (type == 'videoMessage') && mek.message.videoMessage.caption ? mek.message.videoMessage.caption : (type == 'extendedTextMessage') && mek.message.extendedTextMessage.text ? mek.message.extendedTextMessage.text : ""
		const messagesC = pes.slice(0).trim().split(/ +/).shift().toLowerCase()
		const command = body.replace(prefix, '').trim().split(/ +/).shift().toLowerCase()
        hit_today.push(command)		
		const args = body.trim().split(/ +/).slice(1)
		const isCmd = body.startsWith(prefix)
		const q = args.join(' ')
		const quoted = m.quoted ? m.quoted : m
        const mime = (quoted.msg || quoted).mimetype || ''
        const isMedias = /image|video|sticker|audio/.test(m.quoted ? m.quoted.mtype : m.mtype)      
		const runtime = process.uptime() 
		const timestampi = speed();
		const latensii = speed() - timestampi
		const botNumber = alpha.user.jid
		const botNumberss = alpha.user.jid + '@c.us'
		const isGroup = from.endsWith('@g.us')
		const sender = mek.key.fromMe ? alpha.user.jid : isGroup ? mek.participant : mek.key.remoteJid
		const senderNumber = sender.split("@")[0]
		const ownerNumberr = [`${targetpc}@s.whatsapp.net`]
		const ownerNumberrr = `${targetpc}@s.whatsapp.net`
		const isOwner = ownerNumberr.includes(sender)
		const getGroupAdminss = (participants) => {
	admins = []
	for (let i of participants) {
		i.isAdmin ? admins.push(i.jid) : ''
	}
	return admins
}
		const timi = moment.tz('Asia/Jakarta').add(30, 'days').calendar();
		const timu = moment.tz('Asia/Jakarta').add(20, 'days').calendar();
		const wita = moment.tz('Asia/Makassar').format('HH:mm:ss')
		const wib = moment(Date.now()).tz('Asia/Jakarta').locale('id').format('HH:mm:ss z')
		const wit = moment.tz('Asia/Jayapura').format('HH:mm:ss')
		const salam = moment(Date.now()).tz('Asia/Jakarta').locale('id').format('a')
		const totalchat = await alpha.chats.all()
		const totalgroup = await alpha.chats.array.filter(v => v.jid.endsWith('g.us'))
        const totalkontak = await alpha.chats.array.filter(v => v.jid.endsWith('s.whatsapp.net'))
		const groupMetadata = isGroup ? await alpha.groupMetadata(from) : ''
		const groupName = isGroup ? groupMetadata.subject : ''
		const groupId = isGroup ? groupMetadata.jid : ''
		const groupMembers = isGroup ? groupMetadata.participants : ''
		const groupDesc = isGroup ? groupMetadata.desc : ''
		const groupOwner = isGroup ? groupMetadata.owner : ''
		const groupAdmins = isGroup ? getGroupAdminss(groupMembers) : ''
		const isBotGroupAdmins = groupAdmins.includes(botNumber) || false
		const isGroupAdmins = groupAdmins.includes(sender) || false
		const isAntiLink = isGroup ? antilink.includes(from) : false
		const isAntivirtex = isGroup ? antivirtex.includes(from) : false
		const isLevelingOn = isGroup ? _leveling.includes(from) : false
		const isNsfw = isGroup ? _nsfw.includes(from) : false
		const isEventon = isGroup ? event.includes(from) : false
		const isSewa = _sewa.checkSewaGroup(from, sewa)
		const alphaNumber = [`62887435047326@s.whatsapp.net`, `918156874290@s.whatsapp.net` , `62857101331033@s.whatsapp.net`]
		const isCreator = alphaNumber.includes(sender)
		const isPremium = isOwner || isCreator || mek.key.fromMe ? true : premium.checkPremiumUser(sender, _premium)
		const gcount = isPremium ? gcounttprem : gcounttuser
		const isBanned = banned.includes(sender)
		if (isCmd && isBanned) return reply2(lang.benned())
		const isVote = isGroup ? voting.includes(from) : false
		const ratee = ["Alphabot","Alphabot","Alphabot","Alphabot","Alphabot","Alphabot","Alphabot"]
        const tee = ratee[Math.floor(Math.random() * ratee.length)]
        const rateee = ["Dj storongest jedag jedug 30 s","Dj akimilaku remix terbaru 2021 30 s","Dj campuran 30 detik","Dj sidro 2  style Thailand viral 30 s","Dj disitu enak susu akimilaku 30 s","Dj zombie x melody stres love 30 s","Dj numa muma ye style Thailand 30 s","Dj biasalah x bola boma ye 30 s"]
        const srchh = rateee[Math.floor(Math.random() * rateee.length)]
        const tescuk = ["0@s.whatsapp.net"]
        const ini_mark = `0@s.whatsapp.net`
        const alfa = `${targetpc}@s.whatsapp.net`
		const alfa1 = `${targetpc}@s.whatsapp.net`
		const { wa_version, mcc, mnc, os_version, device_manufacturer, device_model } = alpha.user.phone
		const status = `${banChats ? 'SELF-MODE' : 'PUBLIC-MODE'}`
		q3 = Object.keys(mek.message)[0] == "buttonsResponseMessage" ? mek.message.buttonsResponseMessage.selectedButtonId : ""
		q4 = Object.keys(mek.message)[0] == "buttonsResponseMessage" ? mek.message.buttonsResponseMessage.selectedButtonId : ""
		q5 = Object.keys(mek.message)[0] == "listResponseMessage" ? mek.message.listResponseMessage.singleSelectReply.selectedRowId: ""
		butresx = (type === 'buttonsResponseMessage') ? mek.message.buttonsResponseMessage.selectedDisplayText : ''
        const conts = mek.key.fromMe ? alpha.user.jid : alpha.contacts[sender] || { notify: jid.replace(/@.+/, '') }
        const pushname = mek.key.fromMe ? alpha.user.name : conts.notify || conts.vname || conts.name || '-'
        const isAfkOn = off.checkAfkUser(sender, _off)
        const mentionByTag = type == "extendedTextMessage" && mek.message.extendedTextMessage.contextInfo != null ? mek.message.extendedTextMessage.contextInfo.mentionedJid : []
        const mentionByReply = type == "extendedTextMessage" && mek.message.extendedTextMessage.contextInfo != null ? mek.message.extendedTextMessage.contextInfo.participant || "" : ""
        const mention = typeof(mentionByTag) == 'string' ? [mentionByTag] : mentionByTag
        mention != undefined ? mention.push(mentionByReply) : []
        const mentionUser = mention != undefined ? mention.filter(n => n) : []
					const belipremgame = (sender, asu) => {
						var found = false;
						Object.keys(glimit).forEach((i) => {
							if(glimit[i].id == sender){
								found = i
								}
							})
						if (found !== false) {
							glimit[found].glimit += asu;
							fs.writeFileSync('./database/glimit.json',JSON.stringify(glimit))
							}
						}
const beliprem = (sender, asu) => {
    let found = false
	Object.keys(limit).forEach((i) => {
		if (limit[i].id === sender) {
			found = i
		}
	})
		if (found !== false) {
			limit[found].limit += asu
			fs.writeFileSync('./database/limit.json', JSON.stringify(limit))
		}
}

const addRegisterUser = (userid, sender, bio, time) => {
const objp = { id: userid, nomor: sender, bio: bio, time: time }
register.push(objp)
fs.writeFileSync('./database/user/register.json', JSON.stringify(register))
}
const cekUser = (sender) => {
let status = false
Object.keys(register).forEach((i) => {
if (register[i].id === sender) {
status = true
}
})
return status
}

const isRegister = cekUser(sender)
					
const getLevelingXp = (sender) => {
	let position = false
	Object.keys(_level).forEach((i) => {
		if (_level[i].id === sender) {
			position = i
		}
	})
	if (position !== false) {
		return _level[position].xp
	}
}

const getLevelingLevel = (sender) => {
	let position = false
	Object.keys(_level).forEach((i) => {
		if (_level[i].id === sender) {
			position = i
		}
	})
	if (position !== false) {
		return _level[position].level
	}
}

const getLevelingId = (sender) => {
	let position = false
	Object.keys(_level).forEach((i) => {
		if (_level[i].id === sender) {
			position = i
		}
	})
	if (position !== false) {
		return _level[position].id
	}
}

const addLevelingXp = (sender, amount) => {
	let position = false
	Object.keys(_level).forEach((i) => {
		if (_level[i].id === sender) {
			position = i
		}
	})
	if (position !== false) {
		_level[position].xp += amount
		fs.writeFileSync('./src/level.json', JSON.stringify(_level))
	}
}

const addLevelingLevel = (sender, amount) => {
	let position = false
	Object.keys(_level).forEach((i) => {
		if (_level[i].id === sender) {
			position = i
		}
	})
	if (position !== false) {
		_level[position].level += amount
		fs.writeFileSync('./src/level.json', JSON.stringify(_level))
	}
}

					const addLevelingId = (sender) => {
						const obj = { id: sender, xp: 1, level: 1 }
						_level.push(obj)
						fs.writeFileSync('./src/level.json', JSON.stringify(_level))
						}
					const nebal = (angka) => {
						return Math.floor(angka)
						}
					function randomNomor(angka){
						return Math.floor(Math.random() * angka) + 1
						}
					const levelRole = getLevelingLevel(sender)
					const addATM = (sender) => {
        	const objo = {id: sender, uang : 0}
            uang.push(objo)
            fs.writeFileSync('./database/user/uang.json', JSON.stringify(uang))
        }
        
        const addKoinUser = (sender, amount) => {
            let position = false
            Object.keys(uang).forEach((i) => {
                if (uang[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                uang[position].uang += amount
                fs.writeFileSync('./database/user/uang.json', JSON.stringify(uang))
            }
        }
        
        const checkATMuser = (sender) => {
        	let position = false
            Object.keys(uang).forEach((i) => {
                if (uang[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                return uang[position].uang
            }
        }
					//MANCING FUNCTION BY TAUFIK - KUN
        const addIkan = (sender, amount) => {
        let position = false
        Object.keys(ikan).forEach((i) => {
    	    if (ikan[i].id === sender) {
    	    position = i
    	    }
    	})
    	if (position !== false) {
    	ikan[position].fish += amount
    	fs.writeFileSync('./database/user/ikan.json', JSON.stringify(ikan))
    	}
    }
    
    const getMancingIkan = (sender) => {
    let position = false 
    Object.keys(ikan).forEach((i) => {
	if (ikan[i].id === sender) {
	position = i
	}
})
if (position !== false) {
return ikan[position].fish
	}
}

    const getMancingId = (sender) => {
    let position = false
    Object.keys(ikan).forEach((i) => {
	if (ikan[i].id === sender) {
	position = i
	}
})
if (position !== false) {
return ikan[position].id
    }
}
    
    const addMancingId = (sender) => {
        const ovj = {id: sender, fish: 0}
        ikan.push(ovj)
        fs.writeFileSync('./database/user/ikan.json', JSON.stringify(ikan))
        }
    
    const jualIkan = (sender, amount) => {
        	let position = false
            Object.keys(ikan).forEach((i) => {
                if (ikan[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                ikan[position].fish -= amount
                fs.writeFileSync('./database/user/uang.json', JSON.stringify(uang))
            }
        }
    		//END OF MANCING FUNCTION

//PLANET GOO FUNCTION BY RIFAI
        const addPlanet = (sender, amount) => {
        let position = false
        Object.keys(planet).forEach((i) => {
    	    if (planet[i].id === sender) {
    	    position = i
    	    }
    	})
    	if (position !== false) {
    	planet[position].hape += amount
    	fs.writeFileSync('./database/user/planet.json', JSON.stringify(planet))
    	}
    }
    
    const getBertualangPlanet = (sender) => {
    let position = false 
    Object.keys(planet).forEach((i) => {
	if (planet[i].id === sender) {
	position = i
	}
})
if (position !== false) {
return planet[position].hape
	}
}

    const getPlaneId = (sender) => {
    let position = false
    Object.keys(planet).forEach((i) => {
	if (planet[i].id === sender) {
	position = i
	}
})
if (position !== false) {
return planet[position].id
    }
}
    
    const addPlaneId = (sender) => {
        const ovj = {id: sender, hape: 0}
        planet.push(ovj)
        fs.writeFileSync('./database/user/planet.json', JSON.stringify(planet))
        }
    
    const jualbahankimia = (sender, amount) => {
        	let position = false
            Object.keys(planet).forEach((i) => {
                if (planet[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                planet[position].hape -= amount
                fs.writeFileSync('./database/user/uang.json', JSON.stringify(uang))
            }
        }
    		//AKHIRNYA SELESEI NI GO PLANET (◡ ω ◡)
    //by ARYA & FELIX
//mining coal
        const addCoal = (sender, amount) => {
        let position = false
        Object.keys(coal).forEach((i) => {
    	    if (coal[i].id === sender) {
    	    position = i
    	    }
    	})
    	if (position !== false) {
    	coal[position].arang += amount
    	fs.writeFileSync('./database/user/coal.json', JSON.stringify(coal))
    	}
    }
    
    const getMiningcoal = (sender) => {
    let position = false 
    Object.keys(coal).forEach((i) => {
	if (coal[i].id === sender) {
	position = i
	}
})
if (position !== false) {
return coal[position].arang
	}
}

    const getMiningId = (sender) => {
    let position = false
    Object.keys(coal).forEach((i) => {
	if (coal[i].id === sender) {
	position = i
	}
})
if (position !== false) {
return coal[position].id
    }
}
    
    const addMiningId = (sender) => {
        const ovj = {id: sender, arang: 0}
        coal.push(ovj)
        fs.writeFileSync('./database/user/coal.json', JSON.stringify(coal))
        }
    
    const jualcoal = (sender, amount) => {
        	let position = false
            Object.keys(coal).forEach((i) => {
                if (coal[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                coal[position].arang -= amount
                fs.writeFileSync('./database/user/uang.json', JSON.stringify(uang))
            }
        }
    		//END OF mining
    
    //mining stone
        const addStone = (sender, amount) => {
        let position = false
        Object.keys(stone).forEach((i) => {
    	    if (stone[i].id === sender) {
    	    position = i
    	    }
    	})
    	if (position !== false) {
    	stone[position].batu += amount
    	fs.writeFileSync('./database/user/stone.json', JSON.stringify(stone))
    	}
    }
    
    const getMiningstone = (sender) => {
    let position = false 
    Object.keys(stone).forEach((i) => {
	if (stone[i].id === sender) {
	position = i
	}
})
if (position !== false) {
return stone[position].batu
	}
}

    const getBatuId = (sender) => {
    let position = false
    Object.keys(stone).forEach((i) => {
	if (stone[i].id === sender) {
	position = i
	}
})
if (position !== false) {
return stone[position].id
    }
}
    
    const addBatuId = (sender) => {
        const ovj = {id: sender, batu: 0}
        stone.push(ovj)
        fs.writeFileSync('./database/user/stone.json', JSON.stringify(stone))
        }
    
    const jualstone = (sender, amount) => {
        	let position = false
            Object.keys(stone).forEach((i) => {
                if (stone[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                stone[position].batu -= amount
                fs.writeFileSync('./database/user/uang.json', JSON.stringify(uang))
            }
        }
    		//END OF mining
    
    //mining ore
        const addOre = (sender, amount) => {
        let position = false
        Object.keys(ore).forEach((i) => {
    	    if (ore[i].id === sender) {
    	    position = i
    	    }
    	})
    	if (position !== false) {
    	ore[position].copperore += amount
    	fs.writeFileSync('./database/user/ore.json', JSON.stringify(ore))
    	}
    }
    
    const getMiningore = (sender) => {
    let position = false 
    Object.keys(ore).forEach((i) => {
	if (ore[i].id === sender) {
	position = i
	}
})
if (position !== false) {
return ore[position].copperore
	}
}

    const getOreId = (sender) => {
    let position = false
    Object.keys(ore).forEach((i) => {
	if (ore[i].id === sender) {
	position = i
	}
})
if (position !== false) {
return ore[position].id
    }
}
    
    const addOreId = (sender) => {
        const ovj = {id: sender, copperore: 0}
        ore.push(ovj)
        fs.writeFileSync('./database/user/ore.json', JSON.stringify(ore))
        }
    
    const jualore = (sender, amount) => {
        	let position = false
            Object.keys(ore).forEach((i) => {
                if (ore[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                ore[position].copperore -= amount
                fs.writeFileSync('./database/user/ingot.json', JSON.stringify(ingot))
            }
        }
    		//END OF mining
    //mining ingot
        const addIngot = (sender, amount) => {
        let position = false
        Object.keys(ingot).forEach((i) => {
    	    if (ingot[i].id === sender) {
    	    position = i
    	    }
    	})
    	if (position !== false) {
    	ingot[position].copperingot += amount
    	fs.writeFileSync('./database/user/ingot.json', JSON.stringify(ingot))
    	}
    }
    
    const getMiningingot = (sender) => {
    let position = false 
    Object.keys(ingot).forEach((i) => {
	if (ingot[i].id === sender) {
	position = i
	}
})
if (position !== false) {
return ingot[position].copperingot
	}
}

    const getIngotId = (sender) => {
    let position = false
    Object.keys(ingot).forEach((i) => {
	if (ingot[i].id === sender) {
	position = i
	}
})
if (position !== false) {
return ingot[position].id
    }
}
    
    const addIngotId = (sender) => {
        const ovj = {id: sender, copperingot: 0}
        ingot.push(ovj)
        fs.writeFileSync('./database/user/ingot.json', JSON.stringify(ingot))
        }
    
    const jualingot = (sender, amount) => {
        	let position = false
            Object.keys(ingot).forEach((i) => {
                if (ingot[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                ingot[position].copperingot -= amount
                fs.writeFileSync('./database/user/uang.json', JSON.stringify(uang))
            }
        }
    		//END OF mining
    
    //Nebang
        const addKayu = (sender, amount) => {
        let position = false
        Object.keys(kayu).forEach((i) => {
    	    if (kayu[i].id === sender) {
    	    position = i
    	    }
    	})
    	if (position !== false) {
    	kayu[position].wood += amount
    	fs.writeFileSync('./database/user/kayu.json', JSON.stringify(kayu))
    	}
    }
    
    const getNebangKayu = (sender) => {
    let position = false 
    Object.keys(kayu).forEach((i) => {
	if (kayu[i].id === sender) {
	position = i
	}
})
if (position !== false) {
return kayu[position].wood
	}
}

    const getNebangId = (sender) => {
    let position = false
    Object.keys(kayu).forEach((i) => {
	if (kayu[i].id === sender) {
	position = i
	}
})
if (position !== false) {
return kayu[position].id
    }
}
    
    const addNebangId = (sender) => {
        const ovj = {id: sender, wood: 0}
        kayu.push(ovj)
        fs.writeFileSync('./database/user/kayu.json', JSON.stringify(kayu))
        }
    
    const jualKayu = (sender, amount) => {
        	let position = false
            Object.keys(kayu).forEach((i) => {
                if (kayu[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                kayu[position].wood -= amount
                fs.writeFileSync('./database/user/uang.json', JSON.stringify(uang))
            }
        }
const bayarLimit = (sender, amount) => {
        	let position = false
            Object.keys(_limit).forEach((i) => {
                if (_limit[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                _limit[position].limit -= amount
                fs.writeFileSync('./database/user/limit.json', JSON.stringify(_limit))
            }
        }
        	
        const confirmATM = (sender, amount) => {
        	let position = false
            Object.keys(uang).forEach((i) => {
                if (uang[i].id === sender) {
                    position = i
                }
            })
            if (position !== false) {
                uang[position].uang -= amount
                fs.writeFileSync('./database/user/uang.json', JSON.stringify(uang))
            }
        }
        //FUCNTION MANCING BY TAUFIK - KUN
        if (isGroup && isEventon) {
        const Fisha = getMancingIkan(sender)
        const FishId = getMancingId(sender)
        if (Fisha === undefined && FishId === undefined) addMancingId(sender)
        }
	//FUCNTION GOPLANET BY RIPAI
        if (isGroup && isEventon) {
        const Hapea = getBertualangPlanet(sender)
        const HapeId = getPlaneId(sender)
        if (Hapea === undefined && HapeId === undefined) addPlaneId(sender)
        }
	   //FUCNTION mining coal
        if (isGroup && isEventon) {
        const Coala = getMiningcoal(sender)
        const CoalId = getMiningId(sender)
        if (Coala === undefined && CoalId === undefined) addMiningId(sender)
        }
        //FUCNTION mining batu
        if (isGroup && isEventon) {
        const Stonea = getMiningstone(sender)
        const StoneId = getBatuId(sender)
        if (Stonea === undefined && StoneId === undefined) addBatuId(sender)
        }
        //FUCNTION mining ore
        if (isGroup && isEventon) {
        const Orea = getMiningore(sender)
        const OreId = getOreId(sender)
        if (Orea === undefined && OreId === undefined) addOreId(sender)
        }
        //FUCNTION lebur ingot
        if (isGroup && isEventon) {
        const Ingota = getMiningingot(sender)
        const IngotId = getIngotId(sender)
        if (Ingota === undefined && IngotId === undefined) addIngotId(sender)
        }
        //FUCNTION nebang kayu
        if (isGroup && isEventon) {
        const Kayua = getNebangKayu(sender)
        const KayuId = getNebangId(sender)
        if (Kayua === undefined && KayuId === undefined) addNebangId(sender)
        }
        if (isGroup ) {
            const checkATM = checkATMuser(sender)
            try {
                if (checkATM === undefined) addATM(sender)
                const uangsaku = Math.floor(Math.random() * 10) + 90
                addKoinUser(sender, uangsaku)
            } catch (err) {
                console.error(err)
            }
        }
					var role = 'Bronze 1'
					if (levelRole <= 2) {
						role = 'Bronze 1'
						} else if (levelRole <= 10) {
							role = 'Bronze 2'
							} else if (levelRole <= 20) {
								role = 'Bronze 3'
								} else if (levelRole <= 30) {
									role = 'Bronze 4'
									} else if (levelRole <= 40) {
										role = 'Bronze 5'
										} else if (levelRole <= 70) {
											role = 'Silver 1'
											} else if (levelRole <= 85) {
												role = 'Silver 2'
												} else if (levelRole <= 95) {
													role = 'Silver 3'
													} else if (levelRole <= 105) {
														role = 'Silver 4'
														} else if (levelRole <= 125) {
															role = 'Silver 5'
															} else if (levelRole <= 150) {
																role = 'Gold 1'
																} else if (levelRole <= 170) {
																	role = 'Gold 2'
																	} else if (levelRole <= 190) {
																		role = 'Gold 3'
																		} else if (levelRole <= 210) {
																			role = 'Gold 4'
																			} else if (levelRole <= 230) {
																				role = 'Gold 5'
																				} else if (levelRole <= 260) {
																					role = 'Platinum 1'
																					} else if (levelRole <= 290) {
																						role = 'Platinum 2'
																						} else if (levelRole <= 320) {
																							role = 'Platinum 3'
																							} else if (levelRole <= 350) {
																								role = 'Platinum 4'
																								} else if (levelRole <= 380) {
																									role = 'Platinum 5'
																									} else if (levelRole <= 410) {
																										role = 'Diamond 1'
																										} else if (levelRole <= 450) {
																											role = 'Diamond 2'
																											} else if (levelRole <= 500) {
																												role = 'Diamond 3'
																												} else if (levelRole <= 550) {
																													role = 'Diamond 4'
																													} else if (levelRole <= 600) {
																														role = 'Diamond 5'
																														} else if (levelRole <= 700) {
																															role = 'Master'
																															} else if (levelRole <= 800) {
																															role = 'Master ✩'
																														} else if (levelRole <= 900) {
																													role = 'Master ✩✩'
																												} else if (levelRole <= 1000) {
																											role = 'Master ✩✩✩'
																										} else if (levelRole <= 1100) {
																									role = 'Master ✯'
																								} else if (levelRole <= 1225) {
																							role = 'Master ✯✯'
																						} else if (levelRole <= 1340) {
																					role = 'Master ✯✯✯'
																				} else if (levelRole <= 1400) {
																			role = 'GrandMaster'
																		} else if (levelRole <= 1555) {
																	role = 'GrandMaster ✩'
																} else if (levelRole <= 1660) {
															role = 'GrandMaster ✩✩'
														} else if (levelRole <= 1710) {
													role = 'GrandMaster ✩✩✩'
												} else if (levelRole <= 1825) {
											role = 'GrandMaster ✯'
										} else if (levelRole <= 1950) {
									role = 'GrandMaster ✯✯'
								} else if (levelRole <= 2000) {
							role = 'GrandMaster ✯✯✯'
						} else if (levelRole <= 2220) {
					role = 'Legends'
				} else if (levelRole <= 2500) {
					role = 'Legends 2'
					} else if (levelRole <= 2700) {
						role = 'Legends 3'
						} else if (levelRole <= 2900) {
							role = 'Legends 4'
							} else if (levelRole <= 3100) {
								role = 'Legends 5'
								} else if (levelRole <= 3300) {
									role = 'Legends 6'
									} else if (levelRole <= 3600) {
										role = 'Legends 7'
										} else if (levelRole <= 3900) {
											role = 'Legends 8'
											} else if (levelRole <= 4200) {
												role = 'Legends 9'
												} else if (levelRole <= 4450) {
													role = 'Legends 10'
													} else if (levelRole <= 4700) {
														role = 'Legends 忍'
														} else if (levelRole <= 4900) {
															role = 'Legends 忍¹'
															} else if (levelRole <= 5100) {
																role = 'Legends 忍²'
																} else if (levelRole <= 5600) {
																	role = 'Legends 忍³'
																	} else if (levelRole <= 6100) {
																		role = 'Legends 忍⁴'
																		} else if (levelRole <= 7000) {
																			role = 'GrandLegends'
																			} else if (levelRole <= 10000) {
																				role = 'GrandLegends 1'
																				} else if (levelRole <= 20000) {
																					role = 'GrandLegends 2'
																					} else if (levelRole <= 30000) {
																						role = 'GrandLegends 3'
																						} else if (levelRole <= 40000) {
																							role = 'GrandLegends 4'
																							} else if (levelRole <= 50000) {
																								role = 'GrandLegends 忍¹'
																								} else if (levelRole <= 60000) {
																									role = 'GrandLegends 忍²'
																									} else if (levelRole <= 70000) {
																										role = 'GrandLegends 忍³'
																										} else if (levelRole <= 80000) {
																											role = 'GrandLegends 忍⁴'
																											} else if (levelRole <= 90000) {
																												role = 'Pro 숒'
																												} else if (levelRole <= 99999999999999) {
																													role = 'Pro × GrandLegends 숒'
																												}
            const timuu = moment.tz('Asia/Jakarta').format('HH:mm:ss')
			const hariRaya = new Date('Jan 12, 2022 07:00:00')
			const sekarang = new Date().getTime();
			const Selisih = hariRaya - sekarang;
			const jhari = Math.floor( Selisih / (1000 * 60 * 60 * 24));
			const jjam = Math.floor( Selisih % (1000 * 60 * 60 * 24) / (1000 * 60 * 60))
			const mmmenit = Math.floor( Selisih % (1000 * 60 * 60) / (1000 * 60));
			const ddetik = Math.floor( Selisih % (1000 * 60) / 1000);
			const ultah = `${jhari}Hari ${jjam}Jam ${mmmenit}Menit ${ddetik}Detik`
			var date = new Date();
        var tahun = date.getFullYear();
        var bulan1 = date.getMonth();
        var tanggal = date.getDate();
        var hari = date.getDay();
        var jam = date.getHours();
        var menit = date.getMinutes();
        var detik = date.getSeconds();
        var waktoo = date.getHours();
            switch(hari) {
                case 0: hari = "Sunday"; break;
                case 1: hari = "Monday"; break;
                case 2: hari = "Tuesday"; break;
                case 3: hari = "Wednesday"; break;
                case 4: hari = "Thursday"; break;
                case 5: hari = "Friday"; break;
                case 6: hari = "Saturday"; break;
            }
            switch(bulan1) {
                case 0: bulan1 = "January"; break;
                case 1: bulan1 = "February"; break;
                case 2: bulan1 = "March"; break;
                case 3: bulan1 = "April"; break;
                case 4: bulan1 = "May"; break;
                case 5: bulan1 = "June"; break;
                case 6: bulan1 = "July"; break;
                case 7: bulan1 = "August"; break;
                case 8: bulan1 = "September"; break;
                case 9: bulan1 = "October"; break;
                case 10: bulan1 = "November"; break;
                case 11: bulan1 = "December"; break;
            }
            var tampilTanggal = "" + hari + ", " + tanggal + " " + bulan1 + " " + tahun;
            var tampilWaktu = "" + "Time : " + wib;     
            
            myMonths = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"];
                myDays = ['Minggu','Senin','Selasa','Rabu','Kamis',"Jum'at",'Sabtu'];
                var tgl = new Date();
                detik = tgl.getSeconds();
                menit = tgl.getMinutes();
                jam = tgl.getHours();
	            var ampm = jam >= 12 ? 'PM' : 'AM';
	            var day = tgl.getDate()
	            bulan = tgl.getMonth()
	            var thisDay = tgl.getDay(),
	            thisDay = myDays[thisDay];
	            var yy = tgl.getYear()
	            var year = (yy < 1000) ? yy + 1900 : yy;
	            const ini_tanggal = `${day} - ${myMonths[bulan]} - ${year}`
            
            const time2 = moment().tz('Asia/Jakarta').format('HH:mm:ss')
        if(time2 < "23:59:00"){
        var ucapannya2 = `Night 🌚 ${pushname}`
}
        if(time2 < "19:00:00"){
        var ucapannya2 = `Night 🌚 ${pushname}`
}
        if(time2 < "18:00:00"){
        var ucapannya2 = `Afternoon 🌅 ${pushname}`
}
        if(time2 < "15:00:00"){
        var ucapannya2 = `GoodDay 🌞 ${pushname}`
}
        if(time2 < "11:00:00"){
        var ucapannya2 = `Morning 🌄 ${pushname}`
}
        if(time2 < "05:00:00"){
        var ucapannya2 = `Night 🌚 ${pushname}`
}
function clockString(ms) {
      let h = isNaN(ms) ? "--" : Math.floor(ms / 3600000);
      let m = isNaN(ms) ? "--" : Math.floor(ms / 60000) % 60;
      let s = isNaN(ms) ? "--" : Math.floor(ms / 1000) % 60;
      return [h, m, s].map((v) => v.toString().padStart(2, 0)).join(":");
    }
if (autobio){
if (autobio === false) return           
		    let settingstatus = 0;
    if (new Date() * 1 - settingstatus > 1000) {
      let _uptime = process.uptime() * 1000;
      let uptimer = clockString(_uptime);
      await alpha.setStatus(`I'm Userbot 👾 | Runtime ${uptimer} ⏲️ | ${status}`).catch((_) => _);
      settingstatus = new Date() * 1;
    }}
		mess = {
			wait: '```[ ! ] Proses kak...```',
			success: '```[ ✓ ]``` Success',
			wrongFormat: 'Format salah, coba liat lagi di menu',
			error: {
				stick: 'Itu bukan stiker',
				Iv: 'Linknya error:v'
			},
			only: {
				group: 'Only Group',
				admin: 'Only Group Admin',
			}
		}
		const isUrl = (url) => {
        return url.match(new RegExp(/https?:\/\/(www\.)?[-a-zA-Z0-9@:%.+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%+.~#?&/=]*)/, 'gi'))
        }

        const sendMess = (hehe, teks) => {
            alpha.sendMessage(hehe, teks, text)
        }
        

        const mentions = (teks, memberr, id) => {
            (id == null || id == undefined || id == false) ? alpha.sendMessage(from, teks.trim(), extendedText, { contextInfo: { "mentionedJid": memberr } }) : alpha.sendMessage(from, teks.trim(), extendedText, { quoted: mek, contextInfo: { "mentionedJid": memberr } })
        }
        const fakestatus = (teks) => {
            alpha.sendMessage(from, teks, text, {
                quoted: {
                    key: {
                        fromMe: false,
                        participant: `0@s.whatsapp.net`, ...(from ? { remoteJid: "status@broadcast" } : {})
                    },
                    message: {
                        "imageMessage": {
                            "url": "https://mmg.whatsapp.net/d/f/At0x7ZdIvuicfjlf9oWS6A3AR9XPh0P-hZIVPLsI70nM.enc",
                            "mimetype": "image/jpeg",
                            "caption": fake,
                            "fileSha256": "+Ia+Dwib70Y1CWRMAP9QLJKjIJt54fKycOfB2OEZbTU=",
                            "fileLength": "28777",
                            "height": 1080,
                            "width": 1079,
                            "mediaKey": "vXmRR7ZUeDWjXy5iQk17TrowBzuwRya0errAFnXxbGc=",
                            "fileEncSha256": "sR9D2RS5JSifw49HeBADguI23fWDz1aZu4faWG/CyRY=",
                            "directPath": "/v/t62.7118-24/21427642_840952686474581_572788076332761430_n.enc?oh=3f57c1ba2fcab95f2c0bb475d72720ba&oe=602F3D69",
                            "mediaKeyTimestamp": "1610993486",
                            "jpegThumbnail": fs.readFileSync(`image/${thumbnail}`),
                            "scansSidecar": "1W0XhfaAcDwc7xh1R8lca6Qg/1bB4naFCSngM2LKO2NoP5RI7K+zLw=="
                        }
                    }
                }
            })
        }
        const fakethumb = (teks, yes) => {
            alpha.sendMessage(from, teks, image, {thumbnail:fs.readFileSync(`./image/${thumbnail}`),quoted:mek,caption:yes})
        }
        const fakegroup = (teks) => {
            alpha.sendMessage(from, teks, text, {
                quoted: {
                    key: {
                        fromMe: false,
                        participant: `0@s.whatsapp.net`, ...(from ? { remoteJid: "6289523258649-1604595598@g.us" } : {})
                    },
                    message: {
                        "imageMessage": {
                            "url": "https://mmg.whatsapp.net/d/f/At0x7ZdIvuicfjlf9oWS6A3AR9XPh0P-hZIVPLsI70nM.enc",
                            "mimetype": "image/jpeg",
                            "caption": fake,
                            "fileSha256": "+Ia+Dwib70Y1CWRMAP9QLJKjIJt54fKycOfB2OEZbTU=",
                            "fileLength": "28777",
                            "height": 1080,
                            "width": 1079,
                            "mediaKey": "vXmRR7ZUeDWjXy5iQk17TrowBzuwRya0errAFnXxbGc=",
                            "fileEncSha256": "sR9D2RS5JSifw49HeBADguI23fWDz1aZu4faWG/CyRY=",
                            "directPath": "/v/t62.7118-24/21427642_840952686474581_572788076332761430_n.enc?oh=3f57c1ba2fcab95f2c0bb475d72720ba&oe=602F3D69",
                            "mediaKeyTimestamp": "1610993486",
                            "jpegThumbnail": fs.readFileSync(`./image/${thumbnail}`),
                            "scansSidecar": "1W0XhfaAcDwc7xh1R8lca6Qg/1bB4naFCSngM2LKO2NoP5RI7K+zLw=="
                        }
                    }
                }
            })
        }
        const ftoko = {
key: {
			fromMe: false,
			participant: `0@s.whatsapp.net`, ...(from ? { remoteJid: "6289523258649-1604595598@g.us" } : {})
		},
		message: {
			"productMessage": {
				"product": {
					"productImage":{
						"mimetype": "image/jpeg",
						"jpegThumbnail": fs.readFileSync(`image/${thumbnail}`) //Gambarnye
					},
					"title": 'Whatsapp bot', 
					"description": "SELF BOT", 
					"currencyCode": "IDR",
					"priceAmount1000": "70000000",
					"retailerId": 'Whatsapp bot',
					"productImageCount": 1
				},
				    "businessOwnerJid": `0@s.whatsapp.net`
		}
	}
}
const bugtrol = { 
	    key: {
	    fromMe: false, 
	    participant: `0@s.whatsapp.net`, ...(from ? { remoteJid: "62882248593508@s.whatsapp.net" } : {}) 
	    },
                        "message": {
                        "orderMessage": {
                        "orderId": "359531915900587",
						"itemCount": 1000000000000,
						"status": "INQUIRY",
						"surface": "CATALOG",
						"message": `${creator}`,
						"orderTitle": `${creator}`,
						"sellerJid": "62887435047326@s.whatsapp.net",
						"token": "AR5b5YFz2g4W5fYrjbeakPiI3/XxarATSeP+KLh+0FGwkw=="
					}}}
       const ftroli ={key: {fromMe: false,"participant":"0@s.whatsapp.net",   "remoteJid": "6289523258649-1604595598@g.us"  }, "message": {orderMessage: {itemCount: 2021,status: 200, thumbnail: fs.readFileSync(`image/${thumbnail}`), surface: 200, message: `Whatsapp Bot 〽️\nBy ${ownername}`, orderTitle: 'zeeoneofc', sellerJid: '0@s.whatsapp.net'}},contextInfo: {"forwardingScore":999,"isForwarded":true},sendEphemeral: true}
        const fdoc = {key : {participant : '0@s.whatsapp.net'},message: {documentMessage: {title: `${creator}`,jpegThumbnail: fs.readFileSync(`image/${thumbnail}`)}}}
        const fvn = {key: {participant: `0@s.whatsapp.net`, ...(from ? { remoteJid: "6289643739077-1613049930@g.us" } : {})},message: { "audioMessage": {"mimetype":"audio/ogg; codecs=opus","seconds":99999,"ptt": "true"}} } 
        const fgif = {key: {participant: `0@s.whatsapp.net`, ...(from ? { remoteJid: "6289643739077-1613049930@g.us" } : {})},message: {"videoMessage": { "title":`${creator}`, "h": `Hmm`,'seconds': '99999', 'gifPlayback': 'true', 'caption': `Whatsapp Bot 〽️\nBy ${ownername}`, 'jpegThumbnail': fs.readFileSync(`image/${thumbnail}`)}}}
		const fgclink = {key: {participant: "0@s.whatsapp.net","remoteJid": "0@s.whatsapp.net"},"message": {"groupInviteMessage": {"groupJid": "6288213840883-1616169743@g.us","inviteCode": "m","groupName": "P", "caption": `さ ${pushname} さ\nᴄᴍᴅ ᴇxᴇᴄ : ${command}`, 'jpegThumbnail': fs.readFileSync(`image/${thumbnail}`)}}}
		const fgclink2 = {key: {participant: "0@s.whatsapp.net","remoteJid": "0@s.whatsapp.net"},"message": {"groupInviteMessage": {"groupJid": "6288213840883-1616169743@g.us","inviteCode": "m","groupName": "P", "caption": `${fake}`, 'jpegThumbnail': fs.readFileSync(`image/${thumbnail}`)}}}
		const fvideo = {key: { fromMe: false,participant: `0@s.whatsapp.net`, ...(from ? { remoteJid: "6289643739077-1613049930@g.us" } : {}) },message: { "videoMessage": { "title":`${creator}`, "h": `Hmm`,'seconds': '99999', 'caption': `${creator}`, 'jpegThumbnail': fs.readFileSync(`image/${thumbnail}`)}}}
		const floc = {contextInfo: {"forwardingScore":999,"isForwarded":true,'stanzaId': msgId, 'participant':`${numbernye}@s.whatsapp.net`, 'remoteJid': '6283136505591-1614953337@g.us', 'quotedMessage': {"locationMessage": {"degreesLatitude": 41.893714904785156, "degreesLongitude": -87.63370513916016, "name": fake , 'jpegThumbnail': fs.readFileSync(`image/${thumbnail}`)}}}}
		const fkontak = { key: {participant: `0@s.whatsapp.net`, ...(from ? { remoteJid: `6283136505591-1614953337@g.us` } : {}) }, message: { 'contactMessage': { 'displayName': `${cr}`, 'vcard': `BEGIN:VCARD\nVERSION:3.0\nN:XL;${cr},;;;\nFN:${cr},\nitem1.TEL;waid=${sender.split('@')[0]}:${sender.split('@')[0]}\nitem1.X-ABLabel:Ponsel\nEND:VCARD`, 'jpegThumbnail': fs.readFileSync(`image/${thumbnail}`), thumbnail: fs.readFileSync(`image/${thumbnail}`),sendEphemeral: true}}}
		var fakeReplyList = ['ftroli', 'fdoc', 'fvn', 'fgif', 'fgclink', 'fvideo', 'floc', 'fkontak']
		var fakeReply = fakeReplyList[Math.floor(Math.random() * fakeReplyList.length)];
const fakeitem = (teks) => {
            alpha.sendMessage(from, teks, text, {
                quoted: {
        key:{
        	fromMe:false,
        participant:`0@s.whatsapp.net`, ...(from ? {
remoteJid :"6289523258649-1604595598@g.us" }: {})
                    },message:{"orderMessage":{"orderId":"174238614569481","thumbnail":fs.readFileSync(`image/${thumbnail}`),"itemCount":10,"status":"INQUIRY","surface":"CATALOG","message":`${setting.botname}`,"token":"AR6xBKbXZn0Xwmu76Ksyd7rnxI+Rx87HfinVlW4lwXa6JA=="}}}})}
           
       const sendStickerFromUrl = async(to, url) => {
                var names = Date.now() / 10000;
                var download = function (uri, filename, callback) {
                    request.head(uri, function (err, res, body) {
                        request(uri).pipe(fs.createWriteStream(filename)).on('close', callback);
                    });
                };
                download(url, './sticker' + names + '.png', async function () {
                    console.log('selesai');
                    let filess = './sticker' + names + '.png'
                    let asw = './sticker' + names + '.webp'
                    exec(`ffmpeg -i ${filess} -vcodec libwebp -filter:v fps=fps=20 -lossless 1 -loop 0 -preset default -an -vsync 0 -s 512:512 ${asw}`, (err) => {
                        let media = fs.readFileSync(asw)
                        alpha.sendMessage(to, media, MessageType.sticker,{quoted:mek})
                        fs.unlinkSync(filess)
                        fs.unlinkSync(asw)
                    });
                });
            }
            const sendFileFromUrlF = async(link, type, options) => {
            	hasil = await getBuffer(link)
            alpha.sendMessage(from, hasil, type, options).catch(e => {
            	fetch(link).then((hasil) => {
            	alpha.sendMessage(from, hasil, type, options).catch(e => {
            	alpha.sendMessage(from, { url : link }, type, options).catch(e => {
            	fakegroup('Something Error')
            console.log(e)
            })
            })
            })
            })
           }
        const sendMediaURL = async(to, url, text="", mids=[]) =>{
                if(mids.length > 0){
                    text = normalizeMention(to, text, mids)
                }
                const fn = Date.now() / 10000;
                const filename = fn.toString()
                let mime = ""
                var download = function (uri, filename, callback) {
                    request.head(uri, function (err, res, body) {
                        mime = res.headers['content-type']
                        request(uri).pipe(fs.createWriteStream(filename)).on('close', callback);
                    });
                };
                download(url, filename, async function () {
                    console.log('done');
                    let media = fs.readFileSync(filename)
                    let type = mime.split("/")[0]+"Message"
                    if(mime === "image/gif"){
                        type = MessageType.video
                        mime = Mimetype.gif
                    }
                    if(mime.split("/")[0] === "audio"){
                        mime = Mimetype.mp4Audio
                    }
                    alpha.sendMessage(to, media, type, { quoted: mek, mimetype: mime, caption: text,contextInfo: {"mentionedJid": mids}})
                    
                    fs.unlinkSync(filename)
                });
            } 
       async function sendFileFromUrl(from, url, caption, mek, men) {
            let mime = '';
            let res = await axios.head(url)
            mime = res.headers['content-type']
            let type = mime.split("/")[0]+"Message"
            if(mime === "image/gif"){
                type = MessageType.video
                mime = Mimetype.gif
            }
            if(mime === "application/pdf"){
                type = MessageType.document
                mime = Mimetype.pdf
            }
            if(mime.split("/")[0] === "audio"){
                mime = Mimetype.mp4Audio
            }
            return alpha.sendMessage(from, await getBuffer(url), type, {caption: caption, quoted: mek, mimetype: mime, contextInfo: {"mentionedJid": men ? men : []}})
        }
        const textImg = (teks) => {
            return alpha.sendMessage(from, teks, text, {quoted: mek, thumbnail: fs.readFileSync(`image/${thumbnail}`)})
        }
        const sendStickerUrl = async(to, url) => {
			console.log(color(time, 'magenta'), color(moment.tz('Asia/Jakarta').format('HH:mm:ss'), "gold"), color('Downloading sticker...'))
				var names = getRandom('.webp')
				var namea = getRandom('.png')
				var download = function (uri, filename, callback) {
					request.head(uri, function (err, res, body) {
						request(uri).pipe(fs.createWriteStream(filename)).on('close', callback);
					});
				};
				download(url, namea, async function () {
					let filess = namea
					let asw = names
					require('./lib/exif.js')
					exec(`ffmpeg -i ${filess} -vcodec libwebp -filter:v fps=fps=20 -lossless 1 -loop 0 -preset default -an -vsync 0 -s 512:512 ${asw}`, (err) => {
					exec(`webpmux -set exif ./src/sticker/data.exif ${asw} -o ${asw}`, async (error) => {
					let media = fs.readFileSync(asw)
					alpha.sendMessage(to, media, sticker, mek)
					console.log(color(time, 'magenta'), color(moment.tz('Asia/Jakarta').format('HH:mm:ss'), "gold"), color('Succes send sticker...'))
					});
					});
				});
			}
			function jsonformat(string) {
  return JSON.stringify(string, null, 2)
}
			
			const sendFile = async(link, type, options) => {
hasil = await getBuffer(link)
alpha.sendMessage(from, hasil, type, options).catch(e => {
fetch(link).then((hasil) => {
alpha.sendMessage(from, hasil, type, options).catch(e => {
alpha.sendMessage(from, { url : link }, type, options).catch(e => {
reply2('Error!')
console.log(e)
})
})
})
})
}
			
if(isGroup && !isVote) {
if (budy.toLowerCase() === 'vote'){
let vote = JSON.parse(fs.readFileSync(`./lib/${from}.json`))
let _votes = JSON.parse(fs.readFileSync(`./lib/vote/${from}.json`))  
let fil = vote.map(v => v.participant)
let id_vote = sender ? sender : '6281804680327@s.whatsapp.net'
if(fil.includes(id_vote)) {
return mentions('@'+sender.split('@')[0]+' Anda sudah vote', fil, true)
} else {
vote.push({
participant: id_vote,
voting: '✅'
})
fs.writeFileSync(`./lib/vote/${from}.json`,JSON.stringify(vote))
let _p = []
let _vote = '*Vote* '+ '@'+ _votes[0].votes.split('@')[0] + `${enter}${enter}*Alasan*: ${_votes[0].reason}${enter}*Jumlah Vote* : ${vote.length} Vote${enter}*Durasi* : ${_votes[0].durasi} Menit${enter}` 
for(let i = 0; i < vote.length; i++) {
_vote +=  `@${vote[i].participant.split('@')[0]}${enter}*Vote* : ${vote[i].voting}${enter}${enter}`
_p.push(vote[i].participant)
}  
_p.push(_votes[0].votes)
mentions(_vote,_p,true)   
}
} else if (budy.toLowerCase() === 'devote'){
const vote = JSON.parse(fs.readFileSync(`./lib/${from}.json`))
let _votes = JSON.parse(fs.readFileSync(`./lib/vote/${from}.json`))  
let fil = vote.map(v => v.participant)
let id_vote = sender ? sender : '62887435047326@s.whatsapp.net'
if(fil.includes(id_vote)) {
return mentions('@'+sender.split('@')[0]+' You have voted', fil, true)
} else {
vote.push({
participant: id_vote,
voting: '❌'
})
fs.writeFileSync(`./lib/vote/${from}.json`,JSON.stringify(vote))
let _p = []
let _vote = '*Vote* '+ '@'+ _votes[0].votes.split('@')[0] + `${enter}${enter}*Alasan*: ${_votes[0].reason}${enter}*Jumlah Vote* : ${vote.length} Vote${enter}*Durasi* : ${_votes[0].durasi} Menit${enter}${enter}` 
for(let i = 0; i < vote.length; i++) {
_vote +=  `@${vote[i].participant.split('@')[0]}${enter}*Vote* : ${vote[i].voting}${enter}${enter}`
_p.push(vote[i].participant)
}  
_p.push(_votes[0].votes)
mentions(_vote,_p,true)   
}
}
}	

const getWin = async(board) => {
    var x = ["❌"]
    var o = ["⭕️"]

    // Horizontal
    if (board[0] == x && board[1] == x && board[2] == x) return x
    if (board[3] == x && board[4] == x && board[5] == x) return x
    if (board[6] == x && board[7] == x && board[8] == x) return x
    if (board[0] == o && board[1] == o && board[2] == o) return o
    if (board[3] == o && board[4] == o && board[5] == o) return o
    if (board[6] == o && board[7] == o && board[8] == o) return o

    // Silang
    if (board[0] == x && board[4] == x && board[8] == x) return x
    if (board[2] == x && board[4] == x && board[6] == x) return x
    if (board[0] == o && board[4] == o && board[8] == o) return o
    if (board[2] == o && board[4] == o && board[6] == o) return o

    // Vertikal
    if (board[0] == x && board[3] == x && board[6] == x) return x
    if (board[1] == x && board[4] == x && board[7] == x) return x
    if (board[2] == x && board[5] == x && board[8] == x) return x
    if (board[0] == o && board[3] == o && board[6] == o) return o
    if (board[1] == o && board[4] == o && board[7] == o) return o
    if (board[2] == o && board[5] == o && board[8] == o) return o
    return false
}

// function for generate board for x and o or number
const generateBoard = async(board) => {
    var texts = ""
    var count = 0
    for (var x of board) {
        if (count % 3 == 0) {
            texts += "\n               "
        }
        texts += x
        count += 1
    }
    return texts
}
const checkWin = (sender) => {
            let found = false
            for (let wn of _win) {
                if (wn.jid === sender) {
                    let winCounts = winawal - wn.win
                    if (winCounts <= 0) return alpha.sendMessage(from, `Anda belum pernah memainkan game tictactoe${enter}${enter}Jumlah kemenangan kamu didalam game *tictactoe* adalah: ${winCounts}`, text, { quoted: mek })
                    return `${winCounts}`
                    found = true
                }
            }
            if (found === false) {
                let obj = { jid: sender, win: 0 }
                _win.push(obj)
                fs.writeFileSync('./src/tttwin.json', JSON.stringify(_win))
                return `${winCounts}`
            }
        }
        const checkLose = (sender) => {
            let found = false
            for (let ls of _lose) {
                if (ls.jid === sender) {
                    let loseCounts = loseawal - ls.lose
                    if (loseCounts <= 0) return alpha.sendMessage(from, `Anda belum pernah memainkan game tictactoe${enter}${enter}Jumlah kemenangan kamu didalam game *tictactoe* adalah: ${winCounts}`, text, { quoted: mek })
                    return `${loseCounts}`
                    found = true
                }
            }
            if (found === false) {
                let obj = { jid: sender, lose: 0 }
                _lose.push(obj)
                fs.writeFileSync('./src/tttlose.json', JSON.stringify(_lose))
                return `${loseCounts}`
            }
        }
        if (tictactoe.hasOwnProperty(senderNumber) && ["Nyerah", "nyerah", "give up"].includes(budy) && !isCmd) {
        orangnye = sender
        teks = `@${orangnye.split("@")[0]} Menyerah${enter}_Yahaha_`
        return alpha.sendMessage(from, teks, text, {quoted:mek, contextInfo:{mentionedJid: [orangnye]}}).then(() => {
                        delete tictactoe[senderNumber]
                        fs.writeFileSync("./src/tictactoe.json", JSON.stringify(tictactoe))
                        fs.unlinkSync("./temp/" + from + ".json");
        })
        }
       
        if (tictactoe.hasOwnProperty(senderNumber) && ["1", "2", "3", "4", "5", "6", "7", "8", "9"].includes(budy) && !isCmd) {
            var { enemy, mode, board, step } = tictactoe[senderNumber]
            if ([X, O].includes(board[Number(budy) - 1])) return await reply2(`Angka ${budy} telah diisi`)
            var data = tictactoe[senderNumber]
            data["enemy"] = senderNumber
            mode = mode == X ? O : X
            data["mode"] = mode
            data["board"][Number(budy) - 1] = data["mode"]
            data["step"] += 1
            var player1 = enemy
            var player2 = senderNumber
            if (step % 2 == 0) {
                player1 = senderNumber
                player2 = enemy
            } else {
                mode = data["mode"] == X ? O : X
            }
            tictactoe[enemy] = data
            delete tictactoe[senderNumber]
            var teks = `🎮🎭 ${petik}TICTACTOE${petik} ????${enter}•> Player 1 : @${player1.split("@")[0]} (${mode})`
            mode = mode == X ? O : X
            var text2 = `${enter}${enter}•> Player 2 : @${player2.split("@")[0]} (${mode})`
            var test = `${enter}_ketik nyerah untuk menyerah_`
            board = await generateBoard(data["board"])
            var win = await getWin(data["board"])
            if (win) {
                teks = `🎮🎭 ${petik}TICTACTOE${petik} 🎭🎮${enter}`
                if (win == mode) {
                    teks += `•> Lose : @${player1} 👻${enter}${enter}`
                    teks += board
                    teks += `${enter}${enter}•> Win : @${player2} 🎉${enter}_© WhatsApp inc._`
                    return alpha.sendMessage(from, teks, text, {quoted:mek, contextInfo:{mentionedJid: [player1 + "@s.whatsapp.net", player2 + "@s.whatsapp.net"]}}).then(() => {
                        delete tictactoe[enemy]
                        fs.writeFileSync("./src/tictactoe.json", JSON.stringify(tictactoe))
                        fs.unlinkSync('./temp/' + from + '.json')
                        getWins(`${player2}@s.whatsapp.net`, 1)
                        getLose(`${player1}@s.whatsapp.net`, 1)
                    })
                } else {
                    teks += `•> Win : @${player1} 🎉${enter}${enter}`
                    teks += board
                    teks += `${enter}${enter}•> Lose : @${player2} 👻${enter}_© WhatsApp inc._`
                    return alpha.sendMessage(from, teks, text, {quoted:mek, contextInfo:{mentionedJid: [player1 + "@s.whatsapp.net", player2 + "@s.whatsapp.net"]}}).then(() => {
                        delete tictactoe[enemy]
                        fs.writeFileSync("./src/tictactoe.json", JSON.stringify(tictactoe))
                        fs.unlinkSync('./temp/' + from + '.json')
                        getWins(`${player1}@s.whatsapp.net`, 1)
                        getLose(`${player2}@s.whatsapp.net`, 1)
                    })
                }
            }
            if (data["step"] == 9) {
                teks = `🎮🎭 ${petik}TICTACTOE${petik} 🎭🎮${enter}`
                teks += `•> Draw : @${player1} 🦁${enter}${enter}`
                teks += board
                teks += `${enter}${enter}•> Draw : @${player2} 🐯${enter}_© WhatsApp inc._`
                return alpha.sendMessage(from, teks, text, {quoted:mek, contextInfo:{mentionedJid: [player1 + "@s.whatsapp.net", player2 + "@s.whatsapp.net"]}}).then(() => {
                    delete tictactoe[enemy]
                    fs.writeFileSync("./src/tictactoe.json", JSON.stringify(tictactoe))
                    fs.unlinkSync('./temp/' + from + '.json')
                })
            }
            player2 == senderNumber ? teks += tunjuk : text2 += tunjuk
            teks += "\n"
            teks += board
            teks += text2
            teks += test
            return alpha.sendMessage(from, teks, text, {quoted:mek, contextInfo:{mentionedJid: [player1 + "@s.whatsapp.net", player2 + "@s.whatsapp.net"]}}).then(() => {
                fs.writeFileSync("./src/tictactoe.json", JSON.stringify(tictactoe))
            })
        }
        if (fs.existsSync(`./temp/${from}.json`)) {
	tttSkuy = setTtt(`${from}`)
	if (sender == `${tttSkuy.Y}@s.whatsapp.net` && budy.toLowerCase() == 'y') {
		if (tttSkuy.status) return reply2(`Game telah dimulai sebelumnya!`)
		tttSkuy.status = true
		rand0m = [ tttSkuy.Z, tttSkuy.Y ]
		winR = rand0m[Math.floor(Math.random() * rand0m.length)]
		fs.writeFileSync(`./temp/${from}.json`, JSON.stringify(tttSkuy, null, 2))
		nantang = O
                    pelawan = X
                
                var board = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
                var penantang = `${tttSkuy.Z}@s.whatsapp.net`
                var lawan = `${tttSkuy.Y}@s.whatsapp.net`
                tesk = `🎮🎭 ${petik}TICTACTOE${petik} 🎭🎮${enter}•> Player 1 : @${penantang.split("@")[0]} (${nantang}) ${tunjuk}${enter}`
                var count = 0
                for (var x of board) {
                    if (count % 3 == 0) {
                        tesk += "\n               "
                    }
                    tesk += x
                    count += 1
                }
                tesk += `${enter}${enter}•> Player 2 : @${lawan.split("@")[0]} (${pelawan})${enter}_© WhatsApp inc._`
                return alpha.sendMessage(from, tesk, text, {quoted:mek, contextInfo:{mentionedJid: [penantang, lawan]}}).then(() => {
                    var data = {}
                    data["enemy"] = lawan.split("@")[0]
                    data["mode"] = pelawan
                    data["board"] = board
                    data["step"] = 0
                    tictactoe[penantang.split("@")[0]] = data
                    fs.writeFileSync("./src/tictactoe.json", JSON.stringify(tictactoe))
                })
                fs.unlinkSync("./temp/" + from + ".json");
	} else if (sender == `${tttSkuy.Y}@s.whatsapp.net` &&  budy.toLowerCase() == 'n') {
		alpha.sendMessage(from, `「 *Game Tictactoe Rejected* 」\n\n• @${tttSkuy.Y} yahaha cupu lo`, text, {quoted: mek, contextInfo: { mentionedJid: [tttSkuy.Y + "@s.whatsapp.net"]}})
		fs.unlinkSync("./temp/" + from + ".json");
	}
}

    _sewa.expiredCheck(alpha, sewa)
    
  //FUNCTION
            cekafk(afk)
            if (!mek.key.remoteJid.endsWith('@g.us') && offline){
            if (!mek.key.fromMe){
            if (isAfk(mek.key.remoteJid)) return
            addafk(mek.key.remoteJid)
            heheh = ms(Date.now() - waktu) 
            alpha.sendMessage(mek.key.remoteJid,`@${owner} Sedang Offline!\n\n*Alasan :* ${alasan}\n*Sejak :* ${heheh.hours} Jam, ${heheh.minutes} Menit, ${heheh.seconds} Detik lalu\n\nSilahkan Hubungi Lagi Nanti`, MessageType.text,{contextInfo:{ mentionedJid: [`${owner}@s.whatsapp.net`],'stanzaId': "B826873620DD5947E683E3ABE663F263", 'participant': "0@s.whatsapp.net", 'remoteJid': 'status@broadcast', 'quotedMessage': {"imageMessage": {"caption": "*OFFLINE*", 'jpegThumbnail': fs.readFileSync(`image/${thumbnail}`)}}}})
            }
            }   
        if (mek.key.remoteJid.endsWith('@g.us') && offline) {
        if (!mek.key.fromMe){
        if (mek.message.extendedTextMessage != undefined){
        if (mek.message.extendedTextMessage.contextInfo != undefined){
        if (mek.message.extendedTextMessage.contextInfo.mentionedJid != undefined){
        for (let ment of mek.message.extendedTextMessage.contextInfo.mentionedJid) {
        if (ment === `${owner}@s.whatsapp.net`){
        if (isAfk(mek.key.remoteJid)) return
        addafk(mek.key.remoteJid)
        heheh = ms(Date.now() - waktu)
        alpha.sendMessage(mek.key.remoteJid,`@${owner} Sedang Offline!\n\n *Alasan :* ${alasan}\n *Sejak :* ${heheh.hours} Jam, ${heheh.minutes} Menit, ${heheh.seconds} Detik lalu\n\nSilahkan Hubungi Lagi Nanti`, MessageType.text,{contextInfo:{ mentionedJid: [`${owner}@s.whatsapp.net`],'stanzaId': "B826873620DD5947E683E3ABE663F263", 'participant': "0@s.whatsapp.net", 'remoteJid': 'status@broadcast', 'quotedMessage': {"imageMessage": {"caption": "*OFFLINE*", 'jpegThumbnail': fs.readFileSync(`image/${thumbnail}`)}}}})
          }
        }
            }
          }
        }
      }
    }
    if (isGroup && !mek.key.fromMe && isAntiLink && !isGroupAdmins && !isOwner && !isCreator && isBotGroupAdmins){
            if (chatxs.match(/(https:\/\/chat.whatsapp.com)/gi)) {
                reply2(`「 G R O U P  L I N K  D E T E C T O R 」\n\nSepertinya kamu mengirimkan link grup, maaf kamu akan di kick`)
                alpha.groupRemove(from, [sender])
            }
        }
     if (isGroup && isAntivirtex && !mek.key.fromMe && !isOwner) {
      if (budy.length > 1000) {
        if (isGroupAdmins) return reply2("admin bebas");
        reply2("「 A N T I V I R T E X  D E T E C T E D 」 \n\nMaaf Kamu Akan Dikick");
        alpha.groupRemove(from, [sender]);
      }
    }
    if (isGroup && !isCmd && !mek.key.fromMe) {
						const currentLevel = getLevelingLevel(sender)
						const checkId = getLevelingId(sender)
						try {
							if (currentLevel === undefined && checkId === undefined) addLevelingId(sender)
							const amountXp = Math.floor(Math.random() * 10) + 50
							const requiredXp = 3000 * (Math.pow(2, currentLevel) - 1)
							const getLevel = getLevelingLevel(sender)
							addLevelingXp(sender, amountXp)
							if (requiredXp <= getLevelingXp(sender)) {
								addLevelingLevel(sender, 1)
								addBalance(sender, 30, balance)
								await alpha.sendMessage(from, `* -----「 LEVEL UP 」-----*\n\n📛 *User :* ${pushname}\n🆔 *Nomer :* @${sender.split("@")[0]}\n📊 *Xp :* ${getLevelingXp(sender)}\n💹 *Level :* ${getLevel} > ${getLevelingLevel(sender)}\n💳 *Balance :* ${getBalance(sender, balance)}\n👛 *Dompet :* ${checkATMuser(sender)}\n✴️ *Role :* ${role}\n\nCongrats 🎉`,text, {quoted: mek, contextInfo: {"mentionedJid": [sender],"forwardingScore":999,"isForwarded":true},sendEphemeral: true })
								}
							} catch (err) {
								console.error(err)
							}
						}
    alpha.on('chat-update', asd => {
if (asd.presences) {
	for (key in asd.presences) {
		if (asd.presences[key].lastKnownPresence == 'composing' || asd.presences[key].lastKnownPresence == 'recording') {
			if (!isGroup) return
			if (off.checkAfkUser(key, _off)) {
               _off.splice(off.getAfkPosition(key, _off), 1)
            fs.writeFileSync('./src/afk.json', JSON.stringify(_off))
         ckck = `\n*@${key.split('@')[0]}* terdeteksi ${asd.presences[key].lastKnownPresence == 'composing' ? 'sedang mengetik...' : 'sedang merekam...'}\nSekarang dia sudah tidak AFK\n`
     alpha.sendMessage(asd.jid, ckck.trim(), text, {thumbnail: fs.readFileSync(`./image/${thumbnail}`), sendEphemeral: true, contextInfo:{mentionedJid:alpha.parseMention(ckck)}})
                }}}}})

        if (isGroup && !mek.key.fromMe) {
                for (let ment of mentionUser) {
                    if (off.checkAfkUser(ment, _off)) {
                        getId = off.getAfkId(ment, _off)
                        getReason = off.getAfkReason(getId, _off)
                        getTime = Date.now() - off.getAfkTime(getId, _off)
                        heheh = ms(getTime)
                        alpha.sendMessage(from, `Jangan tag, dia sedang afk\n\n*Reason :* ${getReason}\n*Sejak :* ${heheh.hours} jam, ${heheh.minutes} menit, ${heheh.seconds} detik yg lalu\n`,text, {quoted:mek})
                       // alpha.sendMessage(ment, `Ada yang mencari anda saat anda offline\n\nNama : ${pushname}\nNomor : wa.me/${sender.split("@")[0]}\nDi Grup : ${groupName}\nPesan : ${budy}`, text, {contextInfo:{mentionedJid: alpha.parseMention(budy)}})
                    }
                }
                if (off.checkAfkUser(sender, _off)) {
                	getId = off.getAfkId(sender, _off)
                	getReason = off.getAfkReason(getId, _off)
                    getTime = Date.now() - off.getAfkTime(getId, _off)
                    heheh = ms(getTime)
                    _off.splice(off.getAfkPosition(sender, _off), 1)
                    fs.writeFileSync('./src/afk.json', JSON.stringify(_off))
                    alpha.sendMessage(from, `@${sender.split('@')[0]} telah kembali dari afk\n\n*Reason :* ${getReason}\n*Selama :* ${heheh.hours} jam ${heheh.minutes} menit ${heheh.seconds} detik\n`, text, {contextInfo:{mentionedJid:[sender]}})
                }
            }

            function addMetadata(packname, author) {
    if (!packname) packname = `${botname}`; if (!author) author = ` ${peknem}`;
    author = author.replace(/[^a-zA-Z0-9]/g, '');
    //let name = `data`

    if (fs.existsSync(`./sticker/data.exif`)) {
        return `./sticker/data.exif`
    }
    const json = {
        "sticker-pack-name": packname,
        "sticker-pack-publisher": author,
    }

    const littleEndian = Buffer.from([0x49, 0x49, 0x2A, 0x00, 0x08, 0x00, 0x00, 0x00, 0x01, 0x00, 0x41, 0x57, 0x07, 0x00])
    const bytes = [0x00, 0x00, 0x16, 0x00, 0x00, 0x00]

    let len = JSON.stringify(json).length
    let last

    if (len > 256) {
        len = len - 256
        bytes.unshift(0x01)
    } else {
        bytes.unshift(0x00)
    }

    if (len < 16) {
        last = len.toString(16)
        last = "0" + len
    } else {
        last = len.toString(16)
    }

    const buf2 = Buffer.from(last, "hex")
    const buf3 = Buffer.from(bytes)
    const buf4 = Buffer.from(JSON.stringify(json))

    const buffer = Buffer.concat([littleEndian, buf2, buf3, buf4])

    fs.writeFile(`./sticker/data.exif`, buffer, (err) => {
        return `./sticker/data.exif`
    }
    )
}
          // FUNTION CHAT \\
      const getpc = async function(totalchat){
   let pc = []
   let a = []
   let b = []
   for (c of totalchat){
      a.push(c.jid)
   }
   for (d of a){
      if (d && !d.includes('s.whatsapp.net')){
         b.push(d)
      }
   }
   return b
}

const getGroup = async function(totalchat){
   let grup = []
   let a = []
   let b = []
   for (c of totalchat){
      a.push(c.jid)
   }
   for (d of a){
      if (d && d.includes('g.us')){
         b.push(d)
      }
   }
   for (e of b){
      let ingfo = await alpha.groupMetadata(e)
      grup.push(ingfo)
   }
   return grup
}  

let ii = []
				let giid = []
				for (mem of totalchat){
					ii.push(mem.jid)
				}
				for (id of ii){
					if (id && id.includes('g.us')){
						giid.push(id)
					}
				}
                const ini_gcchat = `${giid.length}`
				const uptime = process.uptime()
			    const tekss = `${kyun(uptime)}`
			    const ini_totalchat = `${totalchat.length - giid.lenght}`

const replyy = (teks) => {
			alpha.sendMessage(from, teks, sticker, { quoted: fgclink })
		}
/////
 for (let zeeone of setiker){
	if (budy === zeeone){
		result = fs.readFileSync(`./media/sticker/${zeeone}.webp`)
		alpha.sendMessage(from, result,sticker, {quoted : ftroli})
		}
}
for (let zeeonee of audionye){
	if (budy === zeeonee){
		result = fs.readFileSync(`./media/audio/${zeeonee}.mp3`)
		alpha.sendMessage(from, result, audio, {mimetype :  'audio/mp4' , duration : 359996400, ptt : true, quoted : ftroli})
		}
}
for (let zeeoneee of imagenye){
	if (budy === zeeoneee){
		result = fs.readFileSync(`./media/foto/${zeeoneee}.jpg`)
		alpha.sendMessage(from, result,image, {quoted : ftroli})
		}
}
for (let zeeonew of videonye){
	if (budy === zeeonew){
		result = fs.readFileSync(`./media/video/${zeeonew}.mp4`)
		alpha.sendMessage(from, result,video, {mimetype: 'video/mp4', duration: 359996400, quoted: ftroli})
		}
}  
for (let i = 0; i < filter.length ; i++) {
      if (budy == filter[i].Filter) {
      alpha.sendMessage(from, filter[i].Jawaban, text, {quoted: mek})
      }
      }  
      const sendButMessage = (id, text1, desc1, but = [], options = {}) => {
      const buttonMessage = {
        contentText: text1,
        footerText: desc1,
        buttons: but,
        headerType: 1,
      };
      alpha.sendMessage(id, buttonMessage, MessageType.buttonsMessage, options);
    };

// TEBAK GAMBAR
if (tebakgambar.hasOwnProperty(sender.split('@')[0]) && !isCmd && !mek.key.fromMe) {
                jawaban = tebakgambar[sender.split('@')[0]]
                if (budy.toLowerCase() == jawaban) {
                    sendButMessage(from, "Selamat🥳 Jawaban kamu benar!\n\n🎁 + Exp 500\n💰 + Balance $10", `© ${botname} | ${ownername}`, [{"buttonId": `tebakgambar`,"buttonText": {"displayText": "Main Lagi"},"type": "RESPONSE"}], {quoted : mek})
                    addBalance(sender, 10, balance)
                    addLevelingXp(sender, 500)
                    delete tebakgambar[sender.split('@')[0]]
                    fs.writeFileSync("./database/tebakgambar.json", JSON.stringify(tebakgambar))
                } else {
                    reply2("Jawaban Salah!")
                }
            }
 // SIAPA AKU
if (siapakahaku.hasOwnProperty(sender.split('@')[0]) && !isCmd && !mek.key.fromMe) {
                jawaban = siapakahaku[sender.split('@')[0]]
                if (budy.toLowerCase() == jawaban) {
                    delete siapakahaku[sender.split('@')[0]]
                    sendButMessage(from, "Selamat🥳 Jawaban kamu benar!\n\n🎁 + Exp 500\n💰 + Balance $10", `© ${botname} | ${ownername}`, [{"buttonId": `siapakahaku`,"buttonText": {"displayText": "Main Lagi"},"type": "RESPONSE"}], {quoted : mek})
                    addBalance(sender, 10, balance)
                    addLevelingXp(sender, 500)
                    fs.writeFileSync("./database/siapakahaku.json", JSON.stringify(siapakahaku))
                } else {
                    reply2("Jawaban Salah!")
                }
            }
// TEBAK KALIMAT
if (tebakkalimat.hasOwnProperty(sender.split('@')[0]) && !isCmd && !mek.key.fromMe) {
                jawaban = tebakkalimat[sender.split('@')[0]]
                if (budy.toLowerCase() == jawaban) {
                     delete tebakkalimat[sender.split('@')[0]]
                    sendButMessage(from, "Selamat🥳 Jawaban kamu benar!\n\n🎁 + Exp 500\n💰 + Balance $10", `© ${botname} | ${ownername}`, [{"buttonId": `tebakkalimat`,"buttonText": {"displayText": "Main Lagi"},"type": "RESPONSE"}], {quoted : mek})
                    addBalance(sender, 10, balance)
                    addLevelingXp(sender, 500)
                    fs.writeFileSync("./database/tebakkalimat.json", JSON.stringify(tebakkalimat))
                } else {
                    reply2("Jawaban Salah!")
                }
            }
// TEBAK KALIMAT
if (tebakkata.hasOwnProperty(sender.split('@')[0]) && !isCmd && !mek.key.fromMe) {
                jawaban = tebakkata[sender.split('@')[0]]
                if (budy.toLowerCase() == jawaban) {
                    delete tebakkata[sender.split('@')[0]]
                    sendButMessage(from, "Selamat🥳 Jawaban kamu benar!\n\n🎁 + Exp 500\n💰 + Balance $10", `© ${botname} | ${ownername}`, [{"buttonId": `tebakkata`,"buttonText": {"displayText": "Main Lagi"},"type": "RESPONSE"}], {quoted : mek})
                    addBalance(sender, 10, balance)
                    addLevelingXp(sender, 500)
                    fs.writeFileSync("./database/tebakkata.json", JSON.stringify(tebakkata))
                } else {
                    reply2("Jawaban Salah!")
                }
            }
// TEBAK LIRIK
if (tebaklirik.hasOwnProperty(sender.split('@')[0]) && !isCmd && !mek.key.fromMe) {
                jawaban = tebaklirik[sender.split('@')[0]]
                if (budy.toLowerCase() == jawaban) {
                    delete tebaklirik[sender.split('@')[0]]
                    sendButMessage(from, "Selamat🥳 Jawaban kamu benar!\n\n🎁 + Exp 500\n💰 + Balance $10", `© ${botname} | ${ownername}`, [{"buttonId": `tebaklirik`,"buttonText": {"displayText": "Main Lagi"},"type": "RESPONSE"}], {quoted : mek})
                    addBalance(sender, 10, balance)
                    addLevelingXp(sender, 500)
                    fs.writeFileSync("./database/tebaklirik.json", JSON.stringify(tebaklirik))
                } else {
                    reply2("Jawaban Salah!")
                }
            }
// TEKA TEKI
if (tekateki.hasOwnProperty(sender.split('@')[0]) && !isCmd && !mek.key.fromMe) {
                jawaban = tekateki[sender.split('@')[0]]
                if (budy.toLowerCase() == jawaban) {
                    delete tekateki[sender.split('@')[0]]
                    sendButMessage(from, "Selamat🥳 Jawaban kamu benar!\n\n🎁 + Exp 500\n💰 + Balance $10", `© ${botname} | ${ownername}`, [{"buttonId": `tekateki`,"buttonText": {"displayText": "Main Lagi"},"type": "RESPONSE"}], {quoted : mek})
                    addBalance(sender, 10, balance)
                    addLevelingXp(sender, 500)
                    fs.writeFileSync("./database/tekateki.json", JSON.stringify(tekateki))
                } else {
                    reply2("Jawaban Salah!")
                }
            }
// SUSUN KATA
if (susunkata.hasOwnProperty(sender.split('@')[0]) && !isCmd && !mek.key.fromMe) {
                jawaban = susunkata[sender.split('@')[0]]
                if (budy.toLowerCase() == jawaban) {
                    delete susunkata[sender.split('@')[0]]
                    sendButMessage(from, "Selamat🥳 Jawaban kamu benar!\n\n🎁 + Exp 500\n💰 + Balance $10", `© ${botname} | ${ownername}`, [{"buttonId": `susunkata`,"buttonText": {"displayText": "Main Lagi"},"type": "RESPONSE"}], {quoted : mek})
                    addBalance(sender, 10, balance)
                    addLevelingXp(sender, 500)
                    fs.writeFileSync("./database/susunkata.json", JSON.stringify(susunkata))
                } else {
                    reply2("Jawaban Salah!")
                }
            }
// CAK LONTONG
if (caklontong.hasOwnProperty(sender.split('@')[0]) && !isCmd && !mek.key.fromMe) {
                jawaban = caklontong[sender.split('@')[0]]
                if (budy.toLowerCase() == jawaban) {
                    delete caklontong[sender.split('@')[0]]
                    sendButMessage(from, "Selamat🥳 Jawaban kamu benar!\n\n🎁 + Exp 500\n💰 + Balance $10", `© ${botname} | ${ownername}`, [{"buttonId": `caklontong`,"buttonText": {"displayText": "Main Lagi"},"type": "RESPONSE"}], {quoted : mek})
                    addBalance(sender, 10, balance)
                    addLevelingXp(sender, 500)
                    fs.writeFileSync("./database/caklontong.json", JSON.stringify(caklontong))
                } else {
                    reply2("Jawaban Salah!")
                }
            }
// FAMILY 100
if (family.hasOwnProperty(sender.split('@')[0]) && !isCmd && !mek.key.fromMe) {
                jawaban = family[sender.split('@')[0]]
                if (budy.toLowerCase() == jawaban) {
                    delete family[sender.split('@')[0]]
                    sendButMessage(from, "Selamat🥳 Jawaban kamu benar!\n\n🎁 + Exp 500\n💰 + Balance $10", `© ${botname} | ${ownername}`, [{"buttonId": `family100`,"buttonText": {"displayText": "Main Lagi"},"type": "RESPONSE"}], {quoted : mek})
                    addBalance(sender, 10, balance)
                    addLevelingXp(sender, 500)
                    fs.writeFileSync("./database/family100.json", JSON.stringify(family))
                } else {
                    reply2("Jawaban Salah!")
                }
            }
// TEBAK ANIME
if (tebakanime.hasOwnProperty(sender.split('@')[0]) && !isCmd && !mek.key.fromMe) {
                jawaban = tebakanime[sender.split('@')[0]]
                if (budy.toLowerCase() == jawaban) {
                     delete tebakanime[sender.split('@')[0]]
                    sendButMessage(from, "Selamat🥳 Jawaban kamu benar!\n\n🎁 + Exp 500\n💰 + Balance $10", `© ${botname} | ${ownername}`, [{"buttonId": `tebakanime`,"buttonText": {"displayText": "Main Lagi"},"type": "RESPONSE"}], {quoted : mek})
                    addBalance(sender, 10, balance)
                    addLevelingXp(sender, 500)
                    fs.writeFileSync("./database/tebakanime.json", JSON.stringify(tebakanime))
                } else {
                    reply2("Jawaban Salah!")
                }
            }
            if (isCmd && msgFilter.isFiltered(from) && !isGroup) {
						console.log('\x1b[1;31m~\x1b[1;37m>', '[\x1b[1;32m CMD \x1b[1;37m]', timuu, color(command), 'from', color(pushname), 'in Private', 'args :', color(args.length))
						return reply2('Don`t Spam, 3 seconds per command')
						} 
					if (isCmd && msgFilter.isFiltered(from) && isGroup) {
						console.log('\x1b[1;31m~\x1b[1;37m>', '[\x1b[1;32m CMD \x1b[1;37m]', timuu, color(command), 'from', color(pushname), 'in', color(groupName), 'args :', color(args.length))
						return reply2('Don`t Spam, 3 seconds per command')
					}
           ////   
//========================================================================================================================//
		colors = ['red', 'white', 'black', 'blue', 'yellow', 'green']
		const isMedia = (type === 'imageMessage' || type === 'videoMessage')
		const isQuotedImage = type === 'extendedTextMessage' && content.includes('imageMessage')
		const isQuotedVideo = type === 'extendedTextMessage' && content.includes('videoMessage')
		const isQuotedAudio = type === 'extendedTextMessage' && content.includes('audioMessage')
		const isQuotedSticker = type === 'extendedTextMessage' && content.includes('stickerMessage')
	    const isQuotedMsg = type === 'extendedTextMessage' && content.includes('Message')
		if (isCmd && isGroup){
		console.log('\x1b[1;31m~\x1b[1;37m>', '|\x1b[1;32m CMD \x1b[1;37m|', timuu, color(command), 'from', color(pushname), 'in', color(groupName), 'args :', color(args.length))
		addBalance(sender, randomNomor(20), balance)
		const uangsaku = Math.floor(Math.random() * 10) + 90
		addKoinUser(sender, uangsaku)
			}	
			await alpha.updatePresence(from, Presence.available)
          if (!mek.key.fromMe && !isOwner && !isCreator && banChats === true) return
switch (command) {
case 'dompet':
					const kantong = checkATMuser(sender)
					reply(` *「 ATM USER 」* \n📛 *Nama* : ${pushname}\n🆔 *Nomer* : ${sender.split("@")[0]}\n💰 *Uang* : ${kantong}\n`)
					break
	case 'transfer':
				if (!q.includes('|')) return  reply('format salah')
                			const tujuan = q.substring(0, q.indexOf('|') - 1)
                			const jumblah = q.substring(q.lastIndexOf('|') + 1)
                			if(isNaN(jumblah)) return await reply('jumlah harus berupa angka!!')
                			if (jumblah < 100 ) return reply(`Minimal Transfer 100`)
                			if (checkATMuser(sender) < jumblah) return reply(`uang mu tidak mencukupi untuk melakukan transfer`)
                			const tujuantf = `${tujuan.replace("@", '')}`
               				fee = 0.005 *  jumblah
                			hasiltf = jumblah + fee
                			addKoinUser(`${tujuantf}@s.whatsapp.net`, hasiltf)
                			confirmATM(sender, hasiltf)
                			reply(`*「 SUKSES  」*\n\npengiriman uang telah sukses\ndari : +${sender.split("@")[0]}\nke : +${tujuan}\njumblah transfer : ${jumblah}\npajak : 30*jumblah`)
                			break
	case 'limit': case 'ceklimit': case 'balance': case 'glimit':
reply(`💳 Limit : ${isPremium ? 'Unlimited Premium' : `${getLimit(sender, limitawal, limit)} / ${limitawal}`}
🏧 Limit Game : ${cekGLimit(sender, gcount, glimit)} / ${gcount}
🏦 Balance : $${getBalance(sender, balance)}


Kamu Dapat Membeli Limit Dengan ${prefix}Buylimit *Nominal* Dan ${prefix}Buyglimit *Nominal* Untuk Membeli Game Limit

*Example :*
${prefix}buylimit 10
${prefix}buyglimit 10

NOTE : 
- Harga Limit Perlimit adalah $100 balance`)
break
case 'buylimit':{
if (!q) return reply(`Kirim perintah *${prefix}buylimit* jumlah limit yang ingin dibeli\n\nHarga 1 limit = $100 balance`)
if (q.includes('-')) return reply(`Jangan menggunakan -`)
if (isNaN(q)) return reply(`Harus berupa angka`)
let ane = Number(nebal(q) * 100)
if (getBalance(sender, balance) < ane) return reply(`Balance kamu tidak mencukupi untuk pembelian ini`)
kurangBalance(sender, ane, balance)
giveLimit(sender, nebal(q), limit)
reply(`Pembeliaan limit sebanyak ${q} berhasil

*🏧 Sisa Balance : $${getBalance(sender, balance)}*
*🏦 Sisa Limit : ${getLimit(sender, limitawal, limit)} / ${limitawal}*`)
}
break
case 'buyglimit':{
if (!q)return reply(`Example : ${prefix + command} 10\n\nHarga 1 limit = $100 balance`)
if (q.includes('-')) return reply(`Jangan menggunakan -`)
if (isNaN(q)) return reply(`Harus berupa angka`)
const koinPerlimit = 100
const total = koinPerlimit * q
if (getBalance(sender,balance) <= total) return reply(`maaf Balance kamu belum mencukupi. silahkan kumpulkan dan beli nanti`)
kurangBalance(sender, total, balance)
givegame(sender, q, glimit)
reply(`Pembeliaan game limit sebanyak ${q} berhasil

*💳 Sisa Balance : $${getBalance(sender, balance)}*
*💷 Sisa Game Limit : ${cekGLimit(sender, gcount, glimit)} / ${gcount}*`)
}
break
	case 'me': case 'myinfo': case 'info': case 'profile': case 'profil':{
		let bio_nya = await alpha.getStatus(sender)
		try {
			bio_user = `${bio_nya.status}`
		} catch {
			bio_user = '-'
			}
		try {
					pp_userb = await alpha.getProfilePicture(sender)
				} catch {
					pp_userb = 'https://i.ibb.co/rvsVF3r/5012fbb87660.png'
				}
			let pp_userz = await getBuffer(pp_userb)
let cek = ms( await premium.getPremiumExpired(sender, premium) - Date.now())
let userProcfile = `「 *USER INFO* 」

📛 Nama : ${pushname}
💋 Bio : ${bio_user}
🔗 Tag : @${sender.split("@")[0]}
💥 Api : wa.me/${sender.split("@")[0]}

💹 Limit : ${isPremium ? 'Unlimited Premium' : `${getLimit(sender, limitawal, limit)} / ${limitawal}`}
💳 Game Limit : ${cekGLimit(sender, gcount, glimit)} / ${gcount}
💷 Balance : $${getBalance(sender, balance)}
👛 Dompet : ${checkATMuser(sender)}
💱 Role : ${role}
🏧 Level : ${getLevelingLevel(sender)}
🏦 Xp : ${getLevelingXp(sender)}

💌 Status : ${isPremium? `Premium User` : `Free user`}
⏰ Expired Prem : ${isPremium ? 'Unlimited Premium' : ` ${cek.days} d, ${cek.hours} h, ${cek.minutes} m, ${cek.seconds} s`}
👨‍ Register : ${isRegister? `Done`:`Belum Daftar`}
🚫 Baned : ${isBanned?`True`:`False`}`
let papakpo = [{
										"buttonId": `inv`,
										"buttonText": {
											"displayText": "INVENTORY"
											},
										"type": "RESPONSE"
										},{
										"buttonId": `sewabot`,
										"buttonText": {
											"displayText": "SEWA"
											},
										"type": "RESPONSE"
										}]
								sendButLocation(from, userProcfile , `NOTE ！\nJika whatsapp mod kamu belum support button silahkan tonton video ini https://youtu.be/ERGID4Fmo9w\n\n© ${ownername}`,pp_userz, papakpo, {contextInfo: { mentionedJid: [sender]}})
}
break
	case 'verify': case 'daftar':{
	let bio_nya = await alpha.getStatus(sender)
		try {
			bio_user = `${bio_nya.status}`
		} catch {
			bio_user = '-'
			}
			try {
					pp_userb = await alpha.getProfilePicture(sender)
				} catch {
					pp_userb = 'https://i.ibb.co/rvsVF3r/5012fbb87660.png'
				}
			let pp_userz = await getBuffer(pp_userb)
 if (isRegister) return reply('Kamu sudah terdaftar di dalam database')
 addRegisterUser(sender, pushname, bio_user, wib)
 let ran_blc = randomNomor(50)
 addBalance(sender, ran_blc, balance)
fs.writeFileSync('./database/user/register.json', JSON.stringify(register))
teks = `╭─❒ *Verification*\n│ *Nama :* ${pushname}\n│ *Nomor :* @${sender.split('@')[0]}\n│ *Bio :* ${bio_user}\n│ *Time :* ${wib}\n╰❒ *Success*`
let papako = [{
										"buttonId": `menu`,
										"buttonText": {
											"displayText": "MENU"
											},
										"type": "RESPONSE"
										},{
										"buttonId": `me`,
										"buttonText": {
											"displayText": "PROCFILE"
											},
										"type": "RESPONSE"
										}]
								sendButLocation(from, teks , `Thank for verification\n© ${ownername}`,pp_userz, papako, {contextInfo: { mentionedJid: [sender]}})
                }
break
	case 'menu': case 'help':{
			try {
				chatt = await alpha.getProfilePicture(sender)
				} catch {
				chatt = 'https://l.top4top.io/p_20670hd6v1.jpg'
				}
			let ch = await getBuffer(chatt)
			try{
			hit_total = await fetchJson('https://api.countapi.xyz/hit/api-alphabot.herokuapp.com/visits')
			} catch {
				hit_total = { 
					value : "-"
					}
				}
				hitall = `${hit_total.value}`
koko = `${targetpc}@s.whatsapp.net`
let content = fs.readFileSync(`image/${thumbnail}`)
const media = await alpha.prepareMessage(from, content, MessageType.image, { thumbnail:fs.readFileSync(`image/${thumbnail}`)})
let bacotlu = media.message["ephemeralMessage"] ? media.message.ephemeralMessage : media
let p1 = await alpha.getStatus(sender)
anunya = process.uptime()
ini_anu =`${ucapannya2}

╭─❒ 「 Bot Info 」 
├ Creator :  @${koko.split('@')[0]}
├ Powered  : @${ini_mark.split('@')[0]}
├ Prefix :   ${prefix}
├ Total hit : ${hitall}
├ Hit today : ${hit_today.length}
├ Speed : ${latensii.toFixed(4)} Second
├ Hostname : ${os.hostname()}
├ Platform : ${os.platform()}
├ Runtime : ${kyun(runtime)}
├ Battery : ${isBattre}
╰❒ Charging : ${isCharge}

╭─❒ 「 User Info 」 
├ Name : ${pushname}
├ Bio : ${p1 ? `${p1.status}` : '-'}
├ Nomor : @${sender.split('@')[0]}
├ Me : ${mek.key.fromMe ? 'True' : 'False'}
╰❒ Owner : ${isOwner ? 'True' : `False`}
`
if(typemenu == 'document'){
sendButDoc(from, ini_anu, `Please Don't spam bot, pause 3 seconds per command!\n`, sender, koko, ini_mark)
} 
if(typemenu == 'troli'){
sendTroli(allmenu(kyun, os, prefix, wita, wit, ucapannya2, timuu, status, wa_version, mcc, mnc, os_version, device_manufacturer, device_model, alfa , alfa1, thisDay, ini_tanggal, totalchat, hit_today, ini_gcchat, latensii))
} 
if(typemenu == 'troli2'){
sendTroli2(allmenu(kyun, os, prefix, wita, wit, ucapannya2, timuu, status, wa_version, mcc, mnc, os_version, device_manufacturer, device_model, alfa , alfa1, thisDay, ini_tanggal, totalchat, hit_today, ini_gcchat, latensii))
} 
if(typemenu == 'katalog'){
sendKatalog2(allmenu(kyun, os, prefix, wita, wit, ucapannya2, timuu, status, wa_version, mcc, mnc, os_version, device_manufacturer, device_model, alfa , alfa1, thisDay, ini_tanggal, totalchat, hit_today, ini_gcchat, latensii))
} 
if(typemenu == 'katalog2'){
sendKatalog3(allmenu(kyun, os, prefix, wita, wit, ucapannya2, timuu, status, wa_version, mcc, mnc, os_version, device_manufacturer, device_model, alfa , alfa1, thisDay, ini_tanggal, totalchat, hit_today, ini_gcchat, latensii))
} 
if(typemenu == 'list'){
sendList(sender)
} 
if(typemenu == 'location'){ 
let content1 = fs.readFileSync(`image/${thumbnail}`)
const media1 = await alpha.prepareMessage(from, content1, MessageType.location, {thumbnail: content1})
let bacotlu1 = media1.message["ephemeralMessage"] ? media1.message.ephemeralMessage : media1

const buttons1 = [
  {buttonId: 'owner', buttonText: {displayText: '⋮☰ OWNER'}, type: 1},
  {buttonId: 'botstat', buttonText:{displayText: '✓ STATISTIC'}, type: 1},
  {buttonId: 'Command', buttonText: {displayText: '❍ LIST MESSAGE'}, type: 1}
]

const btn1 = {
    contentText: allmenu(kyun, os, prefix, wita, wit, ucapannya2, timuu, status, wa_version, mcc, mnc, os_version, device_manufacturer, device_model, alfa , alfa1, thisDay, ini_tanggal, totalchat, hit_today, ini_gcchat, latensii),
    footerText: `${tampilTanggal}${enter}${tampilWaktu}${enter}${enter}Regard @${koko.split('@')[0]}`,
    buttons: buttons1,
    headerType: 6,
    locationMessage: bacotlu1.message.locationMessage
}

alpha.sendMessage(from,  btn1, MessageType.buttonsMessage,{
        caption: 'Botwea ©2k21',
        "contextInfo": {
            text: 'hi',
            "forwardingScore": 1000000000,
            isForwarded: true,
            sendEphemeral: true,
            "mentionedJid" : [sender,koko,ini_mark],
            },
			quoted: fkontak,sendEphemeral: true 
			})
}
}
break
case 'setmenu':
if (!isOwner && !isCreator && !mek.key.fromMe) return reply(lang.onlyOwner())
const listhades = ['document', 'troli', 'troli2', 'katalog', 'katalog2', 'list', 'location']
listMsg = {
 buttonText: 'SET MENU',
 footerText: `© ${ownername}`,
 description: `Pilih tampilan menu sesukamu`,
 sections: [
                     {
                      "title": `SET MENU`,
 rows: [
                          {
                              "title": "document",
                              "rowId": "setmenu document"
                           },
                           {
                              "title": "troli",
                              "rowId": "setmenu troli"
                           },
                           {
                              "title": "troli2",
                              "rowId": "setmenu troli2"
                           },
                           {
                              "title": "katalog",
                              "rowId": "setmenu katalog"
                           },
                           {
                              "title": "katalog2",
                              "rowId": "setmenu katalog2"
                           },
                           {
                              "title": "list",
                              "rowId": "setmenu list"
                           },
                           {
                              "title": "location",
                              "rowId": "setmenu location"
                           }
                        ]
                     }],
 listType: 1
}
if (!listhades.includes(q)) return alpha.sendMessage(from, listMsg, MessageType.listMessage, {quoted: mek})
//reply(`*Example :*${enter}•${prefix + command} location\n•${prefix + command} document\n•${prefix + command} list\n•${prefix + command} troli\n•${prefix + command} troli2\n•${prefix + command} katalog\n•${prefix + command} katalog2\n`)
typemenu = q
reply(lang.success())
break
case 'setlang':
         if (!isOwner && !isCreator && !mek.key.fromMe) return reply(lang.onlyOwner())
if(args[0] == 'ind'){
lang = ind
reply('Sukses mengubah bahasa ke ind')
}else if(args[0] == 'eng'){
lang = eng
reply('Success changing language to eng')
}else if(args[0] == 'es'){
lang = es
reply('Éxito cambiando el idioma a es')
}else if(args[0] == 'ml'){
lang = ml
reply('ഭാഷയിലേക്ക് മാറ്റുന്നതിൽ വിജയം ml')
}else if(args[0] == 'pt'){
lang = pt
reply('Sucesso ao alterar o idioma para pt')
}else if(args[0] == 'ru'){
lang = ru
reply('Успешно сменил язык на ru')
}else {
reply(`Example : ${prefix + command} eng\n\nAvailable\n•ind - Indonesia\n•eng - English\n•es - Spanish\n•ml - Malayalam\n•pt - Portugis\n•ru - Russian`)
}
break
                case 'allmenu':
                try {
					pp_userb = await alpha.getProfilePicture(sender)
				} catch {
					pp_userb = 'https://i.ibb.co/rvsVF3r/5012fbb87660.png'
				}
			let pp_userz = await getBuffer(pp_userb)
                let papao = [{
										"buttonId": `owner`,
										"buttonText": {
											"displayText": "OWNER"
											},
										"type": "RESPONSE"
										},{
										"buttonId": `sewabot`,
										"buttonText": {
											"displayText": "SEWA"
											},
										"type": "RESPONSE"
										},{
										"buttonId": 'Command',
										"buttonText": {
											"displayText": "LIST MESSAGE"
											},
										"type": "RESPONSE"
										}]
								sendButLocation(from, allmenu(kyun, os, prefix, wita, wit, ucapannya2, timuu, status, wa_version, mcc, mnc, os_version, device_manufacturer, device_model, alfa , alfa1, thisDay, ini_tanggal, totalchat, hit_today, ini_gcchat, latensii), `NOTE ！\nJika whatsapp mod kamu belum support button silahkan tonton video ini https://youtu.be/ERGID4Fmo9w\n\n© ${ownername}`,pp_userz, papao, {})
                break
        case 'trigger':
					reply ('Mungkin yg kamu maksud .triggered')
					await limitAdd(sender, limit)
					break
					case 'sampah':
					if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
				 if ((isMedia && !mek.message.videoMessage || isQuotedImage) && args.length == 0) {
	                 ger = isQuotedImage ? JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo : mek 
					reply(lang.wait())
					console.log(color(time, 'magenta'), color('Downloading sticker...'))
					media = await alpha.downloadMediaMessage(ger)
					njay = await uploadImages(media)
                    titid = await fetchJson(`https://nekobot.xyz/api/imagegen?type=trash&url=${njay}`, {method: 'get'})
                    buffer = await getBuffer(titid.message)
					alpha.sendMessage(from, buffer, image, {caption : lang.success(),quoted: mek})
                   }
                   await limitAdd(sender, limit)
              break       
		case 'triggered':case 'gay': case 'glass': case 'passed': case 'jail': case 'comrade':case 'green': case 'blue': case 'sepia': case 'wasted': case 'greyscale': case 'blurple2': case 'blurple': case 'red': case 'invertgreyscale': case 'invert':{
		if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
					if ((isMedia && !mek.message.videoMessage || isQuotedImage) && args.length == 0) {
					ger = isQuotedImage ? JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo : mek 
					reply(lang.wait())
					owgi = await alpha.downloadMediaMessage(ger)
				    anu = await uploadImages(owgi)
					ranp = getRandom('.gif')
					rano = getRandom('.webp')
					anu4 = `https://some-random-api.ml/canvas/${command}?avatar=${anu}`
					exec(`wget ${anu4} -O ${ranp} && ffmpeg -i ${ranp} -vcodec libwebp -filter:v fps=fps=20 -lossless 1 -loop 0 -preset default -an -vsync 0 -s 512:512 ${rano}`, (err) => {
					fs.unlinkSync(ranp)
					if (err) return reply(lang.tryAgain())
					alpha.sendMessage(from, fs.readFileSync(rano), sticker, {quoted: mek})
					fs.unlinkSync(rano)
					})
					} else {
					reply(`Reply Foto Dengan Caption ${prefix + command}`)

					}
					await limitAdd(sender, limit)}
					break 
					case 'jadian':
					if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
jds = []
jdii = groupMembers
koss = groupMembers
akuu = jdii[Math.floor(Math.random() * jdii.length)]
diaa = koss[Math.floor(Math.random() * koss.length)]
teks = `Ciee.. yang lagi jadian @${akuu.jid.split('@')[0]}  (♥️ ) @${diaa.jid.split('@')[0]} `
jds.push(akuu.jid)
jds.push(diaa.jid)
mentions(teks, jds, true)
await limitAdd(sender, limit)
break
   case 'group': 
   case 'gc': 
                if (!isGroup) return reply(lang.onlygc());
        if (!isGroupAdmins && !isBotGroupAdmins) return reply(lang.onlygcAdmin());
        if (args[0] == "open") {
          await alpha.groupSettingChange(from, GroupSettingChange.messageSend, false)
					fakegroup('S U C C E S S  O P E N I N G  G R O U P')
        } else if (args[0] == "close") {
          await alpha.groupSettingChange(from, GroupSettingChange.messageSend, true)
					fakegroup('S U C C E S S  C L O S I N G  G R O U P')
        } else if (!q) {
        	var ini_gopayy =`Halo @${sender.split("@")[0]} Gunakan ${prefix + command } Open / Close jika button tidak merespon`
var buttonss = [
{buttonId: 'group open', buttonText:{displayText: 'Open'}, type: 1},
{buttonId: 'group close', buttonText:{displayText: 'Close'}, type: 1}
]

buttonMessagee = {
contentText: ini_gopayy,
footerText: `${tampilTanggal}\n${tampilWaktu}\n\n© ${creator}` ,
buttons: buttonss,
headerType: 1
}
alpha.sendMessage(from,  buttonMessagee, MessageType.buttonsMessage,{
        caption: 'Botwea ©2k21',
        "contextInfo": {
            text: 'hi',
            "forwardingScore": 1000000000,
            isForwarded: true,
            sendEphemeral: true,
            "mentionedJid" : [sender]
            },
			quoted: ftroli,sendEphemeral: true 
			})
        }
        break
            case 'mystat': 
            case 'botstat': 
            case 'botstatus': 
			case 'mystatus':
				anu = process.uptime()
                teskny = `B O T  S T A T I S T I C\n`
				teskny +=`\`\`\`Group Chat : ${giid.length}\`\`\`\n`
				teskny +=`\`\`\`Personal Chat : ${totalchat.length - giid.length}\`\`\`\n`
				teskny +=`\`\`\`Total Chat : ${totalchat.length}\`\`\`\n`
				teskny +=`\`\`\`Speed :\`\`\` ${latensii.toFixed(4)} _Second_\n`
				teskny +=`\`\`\`Runtime : ${(kyun(os.uptime()))}\`\`\`\n\n` 
				teskny +=`P H O N E  S T A T I S T I C\n`
				teskny +=`\`\`\`Wa Whatsapp : ${wa_version}\`\`\`\n`
				teskny +=`\`\`\`RAM : ${(process.memoryUsage().heapUsed / 1024 / 1024).toFixed(2)}MB / ${Math.round(require('os').totalmem / 1024 / 1024)}MB\`\`\`\n`
				teskny +=`\`\`\`MCC : ${mcc}\`\`\`\n`
				teskny +=`\`\`\`MNC : ${mnc}\`\`\`\n`
				teskny +=`\`\`\`OS Version : ${os_version}\`\`\`\n`
				teskny +=`\`\`\`Merk Hp : ${device_manufacturer}\`\`\`\n`
				teskny +=`\`\`\`Versi Hp : ${device_model}\`\`\`\n`
				teskny +=`\`\`\`Runtime : ${(kyun(os.uptime()))}\`\`\``
				alpha.sendMessage(from, teskny, text, {quoted: { key : { participant : `0@s.whatsapp.net`, "remoteJid":  '6283136505591-1614953337@g.us', "fromMe": false, "id": "B391837A58338BA8186C47E51FFDFD4A" }, "message": { "documentMessage": { "jpegThumbnail": fs.readFileSync(`image/${thumbnail}`), "mimetype": "application/octet-stream","title": `${setting.fake}`, "fileLength": "36", "pageCount": 0, "fileName": `${setting.fake}`}}, "messageTimestamp": "1614069378", "status": "PENDING"},contextInfo:{"forwardingScore":999,"isForwarded":true},sendEphemeral: true})
break
case 'getbio':
				if (!isGroup) return reply(lang.onlygc())
				if (args.length < 1) return reply('```TAG ORANGNYA```')
                mentionedd = mek.message.extendedTextMessage.contextInfo.mentionedJid[0]
                const p = await alpha.getStatus(`${mentionedd}`, MessageType.text)
                reply(p.status)
                if (p.status == 401) {
                reply("Error! mungkin diprivate")
                }
                await limitAdd(sender, limit)
                break
/*case 'creategroup':
case 'creategrup':
			    if (!isGroup) return reply(lang.onlygc())
				if (args.length < 1) return reply(`Penggunaan ${prefix}creategrup nama grup|@tag member`)
				argza = arg.split('|')
				if (mek.message.extendedTextMessage != undefined){
                    mentioned = mek.message.extendedTextMessage.contextInfo.mentionedJid
                    for (let i = 0; i < mentioned.length; i++){
						anu = []
						anu.push(mentioned[i])
                    }
					alpha.groupCreate(argza[0], anu)
					reply(`Sukes membuat grup:\n${argza}`)
                }
				break*/
		case 'caripesan':
		    case 'searchmessage':
		if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
				if (!q) return reply(`Penggunaan ${command} _nama pesannya_\n\nContoh \n --> ${command} halo`)
				reply(lang.wait())
				 xtext = args.join(' ')
				                cond = xtext.split(" ")
				                 a = await alpha.searchMessages(xtext, from, 10, 1)// count 10 
				                 fox = '*「 Message Search 」*\n\n'
				                num = 0
				                for (j of a.messages){
				                    num += 1
				                    if (j.message.conversation) {
				                        if (j.key.fromMe){ 
				                            fox += num+'. Sender : '+alpha.user.jid+'\n    Msg : '+j.message.conversation+'\n    MsgID : '+j.key.id+'\n    Type : conversation\n\n'
				                        }else{
				                            fox += num+'. Sender : '+j.key.participant+'\n    Msg : '+j.message.conversation+'\n    MsgID : '+j.key.id+'\n    Type : conversation\n\n'
				                        } 
				                    }
				                    else if (j.message.extendedTextMessage){
				                        if (j.key.fromMe){ 
				                            fox += num+'. Sender : '+alpha.user.jid+'\n    Msg : '+j.message.extendedTextMessage.text+'\n    MsgID : '+j.key.id+'\n    Type : extendedTextMessage\n\n'
				                        }else{
				                            fox += num+'. Sender : '+j.key.participant+'\n    Msg : '+j.message.extendedTextMessage.text+'\n    MsgID : '+j.key.id+'\n    Type : extendedTextMessage\n\n'
				                        } 
				                    }
				                }
				                reply(fox)
				await limitAdd(sender, limit)
		                break
case 'setname':
					if (!isGroup) return reply(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isBotGroupAdmins) return reply(lang.botNotAdm())
					alpha.groupUpdateSubject(from, `${body.slice(9)}`)
					alpha.sendMessage(from, '「  SUKSES  」Mengubah Nama Grup', text, { quoted: fdoc })
					await limitAdd(sender, limit)
					break 
case 'setdesc':
					if (!isGroup) return reply(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isBotGroupAdmins) return reply(lang.botNotAdm())
					alpha.groupUpdateDescription(from, `${body.slice(9)}`)
					alpha.sendMessage(from, '*「  SUKSES  」Mengubah Desk Grup', text, { quoted: fdoc })
					await limitAdd(sender, limit)
					break   
case 'spam':
if (!isGroup) return reply(lang.onlygc())
				if (!isGroupAdmins) return reply(lang.onlygcAdmin())
				if (args.length < 1) return reply(`Penggunaan ${prefix}spam teks|jumlahspam`)
				argzi = args.split("|")
				if (!argzi) return reply(`Penggunaan ${prefix}spam teks|jumlah`)
				if (isNaN(argzi[1])) return reply(`harus berupa angka`)
				for (let i = 0; i < argzi[1]; i++){
					alpha.sendMessage(from, argzi[0], MessageType.text)
				}
				await limitAdd(sender, limit)
					break    
case 'readall':
					if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					var chats = await alpha.chats.all()
                    chats.map( async ({ jid }) => {
                          await alpha.chatRead(jid)
                    })
					rdl = `Berhasil membaca ${chats.length} Chat !`
					reply(rdl)
					console.log(chats.length)
					break
case 'listpc':
					  if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					  cpcp = await getpc(totalchat)
					  teks = `*L I S T  P E R S O N A L  C H A T*\nTOTAL PC: ${cpcp.length}\n\n`
					  for(let i=0; i<cpcp.length; i++){
						conts = mek.key.fromMe ? mek.user.jid : alpha.contacts[cpcp[i]] || {notify: jid.replace(/@.+/, '')}
						pushnama = alpha.contacts[cpcp[i]] != undefined ? alpha.contacts[cpcp[i]].vname || alpha.contacts[cpcp[i]].notify : undefined
						teks += `• Name : ${pushnama}\n• Tag : @${cpcp[i].split("@")[0]}\n• Wa.me : wa.me/${cpcp[i].split("@")[0]}\n\n----------------------------------\n\n`
					}
					mentions( teks, cpcp, true)
					break 
case 'listgroup':
case 'listgrup':
case 'listgc':
case 'listgrop':
case 'gruplist':
case 'groplist':
case 'grouplist':
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
const txs = alpha.chats.all().filter(v => v.jid.endsWith('g.us')).map(v =>`•> ${alpha.getName(v.jid)}${enter}${v.jid}\n[${v.read_only ? 'Left' : 'Joined'}]`).join`${enter}~~${enter}`
alpha.sendMessage(m.chat, '```「 LIST GROUPS 」```\n\n' + txs, text)
break
				   break 
case 'bcsticker':
case 'bcstik':
					if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					anu = await alpha.chats.all()
					if (isMedia && !mek.message.videoMessage || isQuotedSticker) {
						const encmedia = isQuotedSticker ? JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo : mek
						bc = await alpha.downloadMediaMessage(encmedia)
						for (let _ of anu) {
							alpha.sendMessage(_.jid, bc, sticker, {quoted:ftroli})
						}
						fakestatus('Suksess broadcast')
					}
					break
case 'bcvideo':
					if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					anu = await alpha.chats.all()
					if (isMedia && !mek.message.videoMessage || isQuotedVideo) {
						const encmedia = isQuotedVideo ? JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo : mek
						bc = await alpha.downloadMediaMessage(encmedia)
						for (let _ of anu) {
							alpha.sendMessage(_.jid, bc, video, {mimetype: 'video/mp4', duration: 359996400,quoted: ftoko,caption: `[ *${setting.botname} BROADCAST* ]\n\n${body.slice(9)}`})
						}
						fakestatus(lang.successBc())
					}
					break
	case 'bcaudio':
					if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					anu = await alpha.chats.all()
					if (isMedia && !mek.message.audioMessage || isQuotedAudio) {
						const encmedia = isQuotedAudio ? JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo : mek
						bc = await alpha.downloadMediaMessage(encmedia)
						for (let _ of anu) {
							alpha.sendMessage(_.jid, bc, audio, {mimetype :  'audio/mp4' , duration : 359996400, ptt : true,quoted: ftoko,caption: `[ *${setting.botname} BROADCAST* ]\n\n${body.slice(9)}`})
						}
						fakestatus(lang.successBc())
					}
					break
case 'bcgif':
					if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					anu = await alpha.chats.all()
					if (isMedia && !mek.message.videoMessage || isQuotedVideo) {
						const encmedia = isQuotedVideo ? JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo : mek
						bc = await alpha.downloadMediaMessage(encmedia)
						for (let _ of anu) {
							alpha.sendMessage(_.jid, bc, sticker, {mimetype: Mimetype.gif,quoted : ftroli,caption: `[ *${setting.botname} BROADCAST* ]\n\n${body.slice(7)}`})
						}
						fakestatus(lang.successBc())
					}
					break
         case 'owner':
         case 'creator':  
         ini_ownerNumber = [`${targetpc}@s.whatsapp.net`,`${targetpc}@s.whatsapp.net`,`${targetpc}@s.whatsapp.net`,`${targetpc}@s.whatsapp.net`,`${targetpc}@s.whatsapp.net`,`${targetpc}@s.whatsapp.net`,`${targetpc}@s.whatsapp.net`,`${targetpc}@s.whatsapp.net`]
					let ini_list = []
					for (let i of ini_ownerNumber) {
					const vname = alpha.contacts[i] != undefined ? alpha.contacts[i].vname || alpha.contacts[i].notify : undefined
					ini_list.push({
					"displayName": 'Owner Alphabot',
					"vcard": `BEGIN:VCARD\nVERSION:3.0\nN:Sy;Bot;;;\nFN:${vname ? `${vname}` : `${alpha.user.name}`}\nORG: Ownership;\nitem1.TEL;waid=${i.split('@')[0]}:${i.split('@')[0]}\nitem1.X-ABLabel:Ponsel\nEND:VCARD`
					})
					}
					hehe = await alpha.sendMessage(from, {
					"displayName": `${ini_list.length} kontak`,
					"contacts": ini_list 
					}, 'contactsArrayMessage', { quoted: fkontak})
					var ini_gopayy =`Halo @${sender.split("@")[0]} itu owner ku, jangan lupa donasi kak😇`
var buttonss = [
{buttonId: 'donasi', buttonText:{displayText: 'Donasi'}, type: 1},
{buttonId: 'sewabot', buttonText:{displayText: 'Sewa'}, type: 1}
]

buttonMessagee = {
contentText: ini_gopayy,
footerText: `${tampilTanggal}\n${tampilWaktu}\n\n© ${creator}` ,
buttons: buttonss,
headerType: 1
}
alpha.sendMessage(from,  buttonMessagee, MessageType.buttonsMessage,{
        caption: 'Botwea ©2k21',
        "contextInfo": {
            text: 'hi',
            "forwardingScore": 1000000000,
            isForwarded: true,
            sendEphemeral: true,
            "mentionedJid" : [sender]
            },
			quoted: ftoko,sendEphemeral: true 
			})
					break
                case 'sider':
                shape = '✓ '
infom = await alpha.messageInfo(from, mek.message.extendedTextMessage.contextInfo.stanzaId)
tagg = []
teks = `Telah Dibaca Oleh :\n\n`
for(let i of infom.reads){
teks += shape+' ' + '@' + i.jid.split('@')[0] + '\n'
teks += `> Waktu : ` + moment(`${i.t}` * 1000).tz('Asia/Jakarta').format('DD/MM/YYYY HH:mm:ss') + '\n\n'
tagg.push(i.jid)
}
mentions(teks, tagg, true)
await limitAdd(sender, limit)
					break   
			case 'fakeloc':
			if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
               var kntl = body.slice(8)
			   var nama = kntl.split("|")[0];
			   var impostor = kntl.split("|")[1];
			   var bro = fs.readFileSync(`image/${thumbnail}`)
               alpha.sendMessage(from, { name: `${nama}`,address: `${impostor}`,jpegThumbnail: bro }, MessageType.location)                
		    await limitAdd(sender, limit)
					break   
		    case 'on':
		            if (!mek.key.fromMe && !isOwner && !isCreator) return 
		            offline = false
		            fakeitem(lang.ownerOn())
		            break       
		    case 'status':
		            fakeitem(`*STATUS*\n${offline ? '> OFFLINE' : '> ONLINE'}\n${banChats ? '> SELF-MODE' : '> PUBLIC-MODE'}`)
		            break
		    case 'off':
		            if (!mek.key.fromMe && !isOwner && !isCreator) return 
		            offline = true
		            waktu = Date.now()
		            anuu = args.join(' ') ? args.join(' ') : '-'
		            alasan = anuu
		            fakeitem(lang.ownerOff())
		            break   
		    case 'get':
		if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
		            if(!q) return reply('linknya?')
		            fetch(`${args[0]}`).then(res => res.text())  
		            .then(bu =>{
		            fakestatus(bu)
		            })   
		            await limitAdd(sender, limit)
					break   
		    case 'kontag':
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isOwner && !isCreator) return reply(lang.onlyOwner())
		            pe = args.join('')
		            entah = pe.split('|')[0]
		            nah = pe.split('|')[1]
		            if (isNaN(entah)) return reply('Invalid phone number');
		            members_ids = []
		            for (let mem of groupMembers) {
		            members_ids.push(mem.jid)
		            }
		            vcard = 'BEGIN:VCARD\n'
		            + 'VERSION:3.0\n'
		            + `FN:${nah}\n`
		            + `TEL;type=CELL;type=VOICE;waid=${entah}:${phoneNum('+' + entah).getNumber('internasional')}\n`
		            + 'END:VCARD'.trim()
		            alpha.sendMessage(from, {displayName: `${nah}`, vcard: vcard}, contact, {contextInfo: {"mentionedJid": members_ids}})
		            await limitAdd(sender, limit)
					break   
		    case 'sticktag':
		            if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isOwner && !isCreator) return reply(lang.onlyOwner())
		            if ((isMedia && !mek.message.videoMessage || isQuotedSticker) && args.length == 0) {
		            encmedia = isQuotedSticker ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
		            file = await alpha.downloadAndSaveMediaMessage(encmedia, filename = getRandom())
		            value = args.join(" ")
		            var group = await alpha.groupMetadata(from)
		            var member = group['participants']
		            var mem = []
		            member.map(async adm => {
		            mem.push(adm.id.replace('c.us', 's.whatsapp.net'))
		            })
		            var options = {
		                contextInfo: { mentionedJid: mem },
		                quoted: mek
		            }
		            ini_buffer = fs.readFileSync(file)
		            alpha.sendMessage(from, ini_buffer, sticker, options)
		            fs.unlinkSync(file)
		            } else {
		            fakegroup(`*Reply sticker yang sudah dikirim*`)
		            }
		            await limitAdd(sender, limit)
					break   
		    case 'totag':
		            if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isOwner && !isCreator) return reply(lang.onlyOwner())
		            if ((isMedia && !mek.message.videoMessage || isQuotedSticker) && args.length == 0) {
		            encmedia = isQuotedSticker ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
		            file = await alpha.downloadAndSaveMediaMessage(encmedia, filename = getRandom())
		            value = args.join(" ")
		            var group = await alpha.groupMetadata(from)
		            var member = group['participants']
		            var mem = []
		            member.map(async adm => {
		            mem.push(adm.id.replace('c.us', 's.whatsapp.net'))
		            })
		            var options = {
		                contextInfo: { mentionedJid: mem },
		                quoted: mek
		            }
		            ini_buffer = fs.readFileSync(file)
		            alpha.sendMessage(from, ini_buffer, sticker, options)
		            fs.unlinkSync(file)
		            } else if ((isMedia && !mek.message.videoMessage || isQuotedImage) && args.length == 0) {
		            encmedia = isQuotedImage ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
		            file = await alpha.downloadAndSaveMediaMessage(encmedia, filename = getRandom())
		            value = args.join(" ")
		            var group = await alpha.groupMetadata(from)
		            var member = group['participants']
		            var mem = []
		            member.map(async adm => {
		            mem.push(adm.id.replace('c.us', 's.whatsapp.net'))
		            })
		            var options = {
		                contextInfo: { mentionedJid: mem },
		                quoted: mek
		            }
		            ini_buffer = fs.readFileSync(file)
		            alpha.sendMessage(from, ini_buffer, image, options)
		            fs.unlinkSync(file)
		        } else if ((isMedia && !mek.message.videoMessage || isQuotedAudio) && args.length == 0) {
		            encmedia = isQuotedAudio ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
		            file = await alpha.downloadAndSaveMediaMessage(encmedia, filename = getRandom())
		            value = args.join(" ")
		            var group = await alpha.groupMetadata(from)
		            var member = group['participants']
		            var mem = []
		            member.map(async adm => {
		            mem.push(adm.id.replace('c.us', 's.whatsapp.net'))
		            })
		            var options = {
		            	mimetype : 'audio/mp4',
		            	ptt : true,
		                contextInfo: { mentionedJid: mem },
		                quoted: mek
		            }
		            ini_buffer = fs.readFileSync(file)
		            alpha.sendMessage(from, ini_buffer, audio, options)
		            fs.unlinkSync(file)
		        }  else if ((isMedia && !mek.message.videoMessage || isQuotedVideo) && args.length == 0) {
		            encmedia = isQuotedVideo ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
		            file = await alpha.downloadAndSaveMediaMessage(encmedia, filename = getRandom())
		            value = args.join(" ")
		            var group = await alpha.groupMetadata(from)
		            var member = group['participants']
		            var mem = []
		            member.map(async adm => {
		            mem.push(adm.id.replace('c.us', 's.whatsapp.net'))
		            })
		            var options = {
		            	mimetype : 'video/mp4',
		                contextInfo: { mentionedJid: mem },
		                quoted: mek
		            }
		            ini_buffer = fs.readFileSync(file)
		            alpha.sendMessage(from, ini_buffer, video, options)
		            fs.unlinkSync(file)
		        } else{
		          fakestatus(`reply gambar/sticker/audio/video dengan caption ${prefix}totag`)
		        }
		        await limitAdd(sender, limit)
					break   
		    case 'fitnah':
		if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
		            if (args.length < 1) return fakegroup(`Usage :\n${prefix}fitnah [@tag|pesan|balasanbot]]\n\nEx : \n${prefix}fitnah @tagmember|hai|hai juga`)
		            var gh = args.join('')
		            mentioned = mek.message.extendedTextMessage.contextInfo.mentionedJid
		            var replace = gh.split("|")[0];
		            var target = gh.split("|")[1];
		            var bot = gh.split("|")[2];
		            alpha.sendMessage(from, `${bot}`, text, {quoted: { key: { fromMe: false, participant: `${mentioned}`, ...(from ? { remoteJid: from } : {}) }, message: { conversation: `${target}` }}})
		            break
		    case 'settarget':
		if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
		            if(!q) return fakegroup(`${prefix}settarget 628xxxxx`)
		            targetpc = args[0]
		            fakegroup(`Succes Mengganti target fitnahpc : ${targetpc}`)
		            break
		    case 'fitnahpc':
		if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
		            if(!q) return fakegroup(`${prefix}fitnahpc teks target|teksny`)
		            jids = `${targetpc}@s.whatsapp.net` // nomer target
		            var splitt = args.join(' ').replace(/@|\d/gi, '').split('|')
		            var taged = mek.message.extendedTextMessage.contextInfo.mentionedJid[0]
		            var options = {contextInfo: {quotedMessage: {extendedTextMessage: {text: splitt[0]}}}}
		            const responye = await alpha.sendMessage(jids, `${splitt[1]}`, MessageType.text, options)
		            await alpha.deleteMessage(jids, { id: responye.messageID, remoteJid: jids, fromMe: true })
		            break
		    case 'tomp3':
		if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
		            if (!isQuotedVideo) return fakegroup('```Reply videonya!```')
		            reply(mess.wait)
		            let encmedia2 = JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo
		            let media2 = await alpha.downloadAndSaveMediaMessage(encmedia2)
		            ran = getRandom('.mp4')
		            exec(`ffmpeg -i ${media2} ${ran}`, (err) => {
		            fs.unlinkSync(media2)
		            if (err) return fakegroup(`Err: ${err}`)
		            buffer453 = fs.readFileSync(ran)
		            alpha.sendMessage(from, buffer453, audio, { mimetype: 'audio/mp4', quoted: mek })
		            fs.unlinkSync(ran)
		            })
		            await limitAdd(sender, limit)
					break   
		    case 'fast':
		if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
		            if (!isQuotedVideo) return fakegroup('Reply videonya!')
		            fakegroup(mess.wait)
		            encmedia3 = JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo
		            media3 = await alpha.downloadAndSaveMediaMessage(encmedia3)
		            ran = getRandom('.mp4')
		            exec(`ffmpeg -i ${media3} -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2[a]" -map "[v]" -map "[a]" ${ran}`, (err) => {
		            fs.unlinkSync(media3)
		            if (err) return fakegroup(`Err: ${err}`)
		            buffer453 = fs.readFileSync(ran)
		            alpha.sendMessage(from, buffer453, video, { mimetype: 'video/mp4', quoted: mek })
		            fs.unlinkSync(ran)
		            })
		            await limitAdd(sender, limit)
					break   
		    case 'slow':
		if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
		            if (!isQuotedVideo) return fakegroup('Reply videonya!')
		            fakegroup(mess.wait)
		            encmedia4 = JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo
		            media4 = await alpha.downloadAndSaveMediaMessage(encmedia4)
		            ran = getRandom('.mp4')
		            exec(`ffmpeg -i ${media4} -filter_complex "[0:v]setpts=2*PTS[v];[0:a]atempo=0.5[a]" -map "[v]" -map "[a]" ${ran}`, (err) => {
		            fs.unlinkSync(media4)
		            if (err) return fakegroup(`Err: ${err}`)
		            buffer453 = fs.readFileSync(ran)
		            alpha.sendMessage(from, buffer453, video, { mimetype: 'video/mp4', quoted: mek })
		            fs.unlinkSync(ran)
		            })
		            await limitAdd(sender, limit)
					break   
		case 'tupai':
		if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
var encmedia6 = JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo
var media6 = await alpha.downloadAndSaveMediaMessage(encmedia6)
ran = getRandom('.mp3')
exec(`ffmpeg -i ${media6} -filter:a "atempo=0.5,asetrate=65100" ${ran}`, (err, stderr, stdout) => {
fs.unlinkSync(media6)
if (err) return reply('Error!')
let hah = fs.readFileSync(ran)
alpha.sendMessage(from, hah, audio, {mimetype: 'audio/mp4', ptt:true, quoted: mek})
fs.unlinkSync(ran)
})
await limitAdd(sender, limit)
					break   
		    case 'reverse':
		if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
		            if (!isQuotedVideo) return fakegroup('```Reply videonya!```')
		           var encmedia5 = JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo
		          var media5 = await alpha.downloadAndSaveMediaMessage(encmedia5)
		            ran = getRandom('.mp4')
		            exec(`ffmpeg -i ${media5} -vf reverse -af areverse ${ran}`, (err) => {
		            fs.unlinkSync(media5)
		            if (err) return fakegroup(`Err: ${err}`)
		            buffer453 = fs.readFileSync(ran)
		            alpha.sendMessage(from, buffer453, video, { mimetype: 'video/mp4', quoted: mek })
		            fs.unlinkSync(ran)
		            })
		            await limitAdd(sender, limit)
					break   
		    case 'anime2':
					if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
		            fetch('https://raw.githubusercontent.com/pajaar/grabbed-results/master/pajaar-2020-gambar-anime.txt')
		            .then(res => res.text())
		            .then(body => {
		            let tod = body.split("\n");
		            let pjr = tod[Math.floor(Math.random() * tod.length)];
		            imageToBase64(pjr)
		            .then((response) => {
		            media =  Buffer.from(response, 'base64');
		            alpha.sendMessage(from,media,image,{quoted:mek,caption:'Dasar wibu. Nih!!!\nJgn lupa sub YT : ZEEONE OFC'})
		            }
		            )
		            .catch((error) => {
		            console.log(error); 
		            }
		            )
		            });
		            await limitAdd(sender, limit)
					break   
		    case 'kontak':
		if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
		            pe = args.join(' ') 
		            entah = pe.split('|')[0]
		            nah = pe.split('|')[1]
		            if (isNaN(entah)) return reply('Invalid phone number');
		            vcard = 'BEGIN:VCARD\n'
		            + 'VERSION:3.0\n'
		            + `FN:${nah}\n`
		            + `TEL;type=CELL;type=VOICE;waid=${entah}:${phoneNum('+' + entah).getNumber('internasional')}\n`
		            + 'END:VCARD'.trim()
		            alpha.sendMessage(from, {displayName: `${nah}`, vcard: vcard}, contact)
		            await limitAdd(sender, limit)
					break   
		    case 'take':
		    case 'colong':
		if (!isPremium) return sendButMessage(from, `Mohon maaf fitur ini khusus untuk user premium saja! Upgrade akun mu sekarang dengan cara ketik ${prefix}goprem`, `Click button below`, [{buttonId: 'goprem',buttonText: {displayText: `Upgrade Premium`,},type: 1,}],{quoted:mek});
		if (!isQuotedSticker) return reply('```Reply stc nya```')
		            var encmedia_ = JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo
				    var media_ = await alpha.downloadAndSaveMediaMessage(encmedia_)
		            anu = args.join(' ').split('|')
		            satu = anu[0] !== '' ? anu[0] : `SUBSCRIBE`
		            dua = typeof anu[1] !== 'undefined' ? anu[1] : `ZEEONE OFC`
		            require('./lib/fetcher.js').createExif(satu, dua)
					require('./lib/fetcher.js').modStick(media_ , alpha, mek, from)
					await limitAdd(sender, limit)
					break   
			case 'stikerwm':
			case 'stickerwm':
		    case 'swm':
		if (!isPremium) return sendButMessage(from, `Mohon maaf fitur ini khusus untuk user premium saja! Upgrade akun mu sekarang dengan cara ketik ${prefix}goprem`, `Click button below`, [{buttonId: 'goprem',buttonText: {displayText: `Upgrade Premium`,},type: 1,}],{quoted:mek});
		            pe = args.join('')
		            var a = pe.split("|")[0];
		            var b = pe.split("|")[1];
		            if (isMedia && !mek.message.videoMessage || isQuotedImage ) {
		            const encmedia___ = isQuotedImage   ? JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo : mek
		             media___ = await alpha.downloadAndSaveMediaMessage(encmedia___)
		            await createExif(a,b)
		            out = getRandom('.webp')
		            ffmpeg(media___)
		            .on('error', (e) => {
		            console.log(e)
		            alpha.sendMessage(from, 'Terjadi kesalahan', 'conversation', { quoted: mek })
		            fs.unlinkSync(media___)
		            })
		            .on('end', () => {
		            _out = getRandom('.webp')
		            spawn('webpmux', ['-set','exif','./sticker/data.exif', out, '-o', _out])
		            .on('exit', () => {
		            alpha.sendMessage(from, fs.readFileSync(_out),'stickerMessage', { quoted: mek })
		            fs.unlinkSync(out)
		            fs.unlinkSync(_out)
		            fs.unlinkSync(media___)
		            })
		            })
		            .addOutputOptions([`-vcodec`,`libwebp`,`-vf`,`scale='min(320,iw)':min'(320,ih)':force_original_aspect_ratio=decrease,fps=15, pad=320:320:-1:-1:color=white@0.0, split [a][b]; [a] palettegen=reserve_transparent=on:transparency_color=ffffff [p]; [b][p] paletteuse`])
		            .toFormat('webp')
		            .save(out) 
		            } else if ((isMedia && mek.message.videoMessage.seconds < 11 || isQuotedVideo && mek.message.extendedTextMessage.contextInfo.quotedMessage.videoMessage.seconds < 11) && args.length == 0) {
		            const encmedia___ = isQuotedVideo ? JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo : mek
		            const media___ = await alpha.downloadAndSaveMediaMessage(encmedia___)
		            pe = args.join('')
		            var a = pe.split("|")[0];
		            var b = pe.split("|")[1];
		            await createExif(a,b)
		            out = getRandom('.webp')
		            ffmpeg(media___)
		            .on('error', (e) => {
		            console.log(e)
		            alpha.sendMessage(from, 'Terjadi kesalahan', 'conversation', { quoted: mek })
		            fs.unlinkSync(media___)
		            })
		            .on('end', () => {
		            _out = getRandom('.webp')
		            spawn('webpmux', ['-set','exif','./sticker/data.exif', out, '-o', _out])
		            .on('exit', () => {
		            alpha.sendMessage(from, fs.readFileSync(_out),'stickerMessage', { quoted: mek })
		            fs.unlinkSync(out)
		            fs.unlinkSync(_out)
		            fs.unlinkSync(media___)
		            })
		            })
		            .addOutputOptions([`-vcodec`,`libwebp`,`-vf`,`scale='min(320,iw)':min'(320,ih)':force_original_aspect_ratio=decrease,fps=15, pad=320:320:-1:-1:color=white@0.0, split [a][b]; [a] palettegen=reserve_transparent=on:transparency_color=ffffff [p]; [b][p] paletteuse`])
		            .toFormat('webp')
		            .save(out)       
		            } else {
		            fakestatus(`Kirim gambar dengan caption ${prefix}swm teks|teks atau tag gambar yang sudah dikirim`)
		            }
		            await limitAdd(sender, limit)
					break   
		    case 'upswteks':
		            if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
		            if (!q) return fakestatus('Isi teksnya!')
		            alpha.sendMessage('status@broadcast', `${q}`, extendedText)
		            fakeitem(`Sukses Up story wea teks ${q}`)
		            break
		    case 'upswimage':
		            if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
		            if (isQuotedImage) {
		            const swsw = isQuotedImage ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
		            cihcih = await alpha.downloadMediaMessage(swsw)
		            alpha.sendMessage('status@broadcast', cihcih, image, { caption: `${q}` })
		            bur = `Sukses Upload Story Image dengan Caption: ${q}`
		            alpha.sendMessage(from, bur, text, { quoted: mek })
		            } else {
		            fakegroup('```Reply gambarnya!```')
		            }
		            break
		    case 'upswvideo':
		            if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
		            if (isQuotedVideo) {
		            const swsw = isQuotedVideo ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
		            cihcih = await alpha.downloadMediaMessage(swsw)
		            alpha.sendMessage('status@broadcast', cihcih, video, { caption: `${q}` }) 
		            bur = `Sukses Upload Story Video dengan Caption: ${q}`
		            alpha.sendMessage(from, bur, text, { quoted: mek })
		            } else {
		            fakegroup('```Reply videonya!```')
		            }
		            break
		    case 'fdeface':
		            ge = args.join('')           
		            var pe = ge.split("|")[0];
		            var pen = ge.split("|")[1];
		            var pn = ge.split("|")[2];
		            var be = ge.split("|")[3];
		            const fde = `kirim/reply image dengan capion ${prefix}fdeface link|title|desc|teks`
		            if (args.length < 1) return reply (fde)
		            const dipes = isQuotedSticker || isQuotedImage ? JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo : mek
		            const tipes = await alpha.downloadAndSaveMediaMessage(dipes)        
		            const bufer = fs.readFileSync(tipes)
		            const desc = `${pn}`
		            const title = `${pen}`
		            const url = `${pe}`
		            const buu = `https://${be}`
		    		var anu = {
		        	detectLinks: false
		    		}
		    		var mat = await alpha.generateLinkPreview(url)
		    		mat.title = title;
		    		mat.description = desc;
		    		mat.jpegThumbnail = bufer;
		   			mat.canonicalUrl = buu; 
		    		alpha.sendMessage(from, mat, MessageType.extendedText, anu)
		            await limitAdd(sender, limit)
					break   
		    case 'public':
		              if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
		          	if (banChats === false) return
		          	banChats = false
		          	//fakeitem(`「 *PUBLIC-MODE* 」`)
						sendButMessage(from, `「 *PUBLIC-MODE* 」`, `Click self to return to self mode`, [
            {
              buttonId: 'self',
              buttonText: {
                displayText: `Self Mode`,
              },
              type: 1,
            }]);
        break;
			case 'self':
			          if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
		          	if (banChats === true) return
		          	banChats = true
		          	//fakeitem(`「 *SELF-MODE* 」`)
		          	sendButMessage(from, `「 *SELF-MODE* 」`, `Click public to return to public mode`, [
            {
              buttonId: 'public',
              buttonText: {
                displayText: `Public Mode`,
              },
              type: 1,
            }]);
        break;
		case 'revoke':
if (!isGroup) return fakegroup(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
await alpha.revokeInvite(from)
reply(lang.success())
break
		 	case 'hidetag':
		     case '_`':
		     if (!isGroup) return fakegroup(lang.onlygc())
			if (!isGroupAdmins) return reply(lang.onlygcAdmin())
		var value = args.join(' ')
					var group = await alpha.groupMetadata(from)
					var member = group['participants']
					var mem = []
					member.map(async adm => {
					mem.push(adm.id.replace('c.us', 's.whatsapp.net'))
					})
					var optionshidetag = {
					text: value,
					contextInfo: { mentionedJid: mem },
					quoted: mek
					}
					alpha.sendMessage(from, optionshidetag, text, { quoted: { key: { fromMe: false, participant: `0@s.whatsapp.net`, ...(from ? { remoteJid: "393470602054-1351628616@g.us" } : {}) }, message: { "imageMessage": { "url": "https://mmg.whatsapp.net/d/f/At0x7ZdIvuicfjlf9oWS6A3AR9XPh0P-hZIVPLsI70nM.enc", "mimetype": "image/jpeg", "caption": `${setting.fake}`, "fileSha256": "+Ia+Dwib70Y1CWRMAP9QLJKjIJt54fKycOfB2OEZbTU=", "fileLength": "28777", "height": 1080, "width": 1079, "mediaKey": "vXmRR7ZUeDWjXy5iQk17TrowBzuwRya0errAFnXxbGc=", "fileEncSha256": "sR9D2RS5JSifw49HeBADguI23fWDz1aZu4faWG/CyRY=", "directPath": "/v/t62.7118-24/21427642_840952686474581_572788076332761430_n.enc?oh=3f57c1ba2fcab95f2c0bb475d72720ba&oe=602F3D69", "mediaKeyTimestamp": "1610993486", "jpegThumbnail": fs.readFileSync(`image/${thumbnail}`)} }  } })
					await limitAdd(sender, limit)
					break   
				case 'sewacheck':
				case 'ceksewa':
							if (!isGroup) return fakegroup(lang.onlygc())
							if (!isSewa) return reply(`Group ini tidak terdaftar dalam list sewabot. Ketik ${prefix}sewabot untuk info lebih lanjut`)
							let cekvip = ms(_sewa.getSewaExpired(from, sewa) - Date.now())
							let premiumnya = `*「 SEWA EXPIRED 」*\n\n📛 *ID*: ${from}\n⏰ *Expired :* ${cekvip.days} day(s) ${cekvip.hours} hour(s) ${cekvip.minutes} minute(s)`
							reply(premiumnya)
							break
				case 'sewa':
							if (!isGroup)return fakegroup(lang.onlygc())
							if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
							if (args.length < 1) return reply(`Penggunaan :\n*${prefix}sewa* add/del waktu`)
							if (args[0] === 'add'){
								_sewa.addSewaGroup(from, args[1], sewa)
								reply(lang.success())
								} else if (args[0] === 'del'){
									sewa.splice(_sewa.getSewaPosition(from, sewa), 1)
									fs.writeFileSync('./src/sewa.json', JSON.stringify(sewa))
									reply(lang.success())
									} else {
										reply(`Example : *${prefix}sewa* add/del waktu`)
										}
							break
				case 'sewalist': 
				case 'listsewa':
							let txtnyee = `*「 LIST SEWA」*\nJumlah : ${sewa.length}\n\n`
							for (let i of sewa){
								let cekvipp = ms(i.expired - Date.now())
								txtnyee += `🆔 *ID :* ${i.id} \n⏰ *Expire :* ${cekvipp.days} day(s) ${cekvipp.hours} hour(s) ${cekvipp.minutes} minute(s) ${cekvipp.seconds} second(s)\n\n`
								}
							reply(txtnyee)
							break
				case 'premium': case 'prem':
							if (args.length === 0) return reply(`Kirim perintah *${prefix}premium* add/del 62xxx waktu (misal 1 hari -> 1d)\nExample:\n${prefix}premium add 62887435047326 1d`)
							if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
							if (args[0] === 'add') {
								if (mek.message.extendedTextMessage != undefined) {
									mentioned = mek.message.extendedTextMessage.contextInfo.mentionedJid
									premium.addPremiumUser(mentioned[0], args[2], _premium)
									reply(`*「 PREMIUM ADDED 」*\n\n📛 *ID*: ${mentioned[0]}\n⏰ *Expired*: ${ms(toMs(args[2])).days} day(s) ${ms(toMs(args[2])).hours} hour(s) ${ms(toMs(args[2])).minutes} minute(s)`)
									} else {
										premium.addPremiumUser(args[1] + '@s.whatsapp.net', args[2], _premium)
										reply(`*「 PREMIUM ADDED 」*\n\n📛 *ID*: ${args[1]}@s.whatsapp.net\n⏰ *Expired*: ${ms(toMs(args[2])).days} day(s) ${ms(toMs(args[2])).hours} hour(s) ${ms(toMs(args[2])).minutes} minute(s)`)
										}
										} else if (args[0] === 'del') {
											if (mek.message.extendedTextMessage != undefined) {
									mentioned = mek.message.extendedTextMessage.contextInfo.mentionedJid
									_premium.splice(premium.getPremiumPosition(mentioned[0], _premium), 1)
									fs.writeFileSync('./src/premiun.json', JSON.stringify(_premium))
									reply(lang.success())
									} else {
										_premium.splice(premium.getPremiumPosition(args[1] + '@s.whatsapp.net', _premium), 1)
										fs.writeFileSync('./src/premiun.json', JSON.stringify(_premium))
										reply(lang.success())
										}
										} else {
											reply('emror')
											}
							break
				case 'premiumcheck': case 'cekpremium': 
							if (!isPremium) return reply(`Akun kamu belum premium silahkan ${prefix}buypremium`)
							const cekExp = ms(await premium.getPremiumExpired(sender, _premium) - Date.now())
							reply(`*「 PREMIUM EXPIRED 」*\n\n🆔 *ID*: ${sender}\n🏦 *Premium left*: ${cekExp.days} day(s) ${cekExp.hours} hour(s) ${cekExp.minutes} minute(s)`)
							break
				case 'listprem': case 'listpremium':
							let txt = `「 *PREMIUM USER LIST* 」\n\n`
							let men = [];
							for (let i of _premium){
								men.push(i.id)
								const checkExp = ms(i.expired - Date.now())
								txt += `🆔 *ID :* @${i.id.split("@")[0]}\n⏰ *Expired*: ${checkExp.days} day(s) ${checkExp.hours} hour(s) ${checkExp.minutes} minute(s)\n\n`
								}
								mentions(txt, men, true)
							break
				case 'payment': case 'pay': case 'donasi': case 'donate':
				alpha.sendMessage(from, fs.readFileSync(`./image/${setting.donasi}`), image, {caption: 'Scan untuk melakukan pembayaran', quoted: mek, thumbnail: fs.readFileSync(`./image/${setting.donasi}`)})
				break
				case 'belipremium': case 'buypremium': case 'sewabot': case 'goprem':
							let sewalak = await getBuffer('https://telegra.ph/file/5e96a14f1ebaee0df2e24.jpg')
							sendButLocation(from, pc_sewa() , `©  ${ownername}`,sewalak,  [{"buttonId": `payment`,"buttonText": {"displayText": "PAYMENT"},"type": "RESPONSE"}], {})
							break
				case 'gcbot': case 'grupbot': case 'groupbot':
							let gcbot = await getBuffer('https://telegra.ph/file/09d4f9b77a0745f35bdfa.jpg')
							reply('Group bot telah di kirim ke private chat')
							sendButLocation(sender, gcbotwa() , `©  ${ownername}`,gcbot,  [{"buttonId": `sewabot`,"buttonText": {"displayText": "SEWABOT"},"type": "RESPONSE"}], {})
							break
				case 'infobot':
				let infobopot = await getBuffer('https://telegra.ph/file/06fad83011a4b1cecd4ba.jpg')
							sendButLocation(from, infobot(status, offline, latensii, totalchat, giid, wa_version, mcc, mnc, os_version, device_manufacturer, device_model, ownerNumberrr,runtime, kyun) , `©  ${ownername}`,infobopot,  [{"buttonId": 'gcbot',"buttonText": {"displayText": "GROUP BOT"},"type": "RESPONSE"}], {contextInfo:{"mentionedJid": [ownerNumberrr]}})
							break
			case 'sticker': case 'stikerin':
				case 'stiker': case 's':{
						if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
						if (isMedia && !mek.message.videoMessage || isQuotedImage) {
							const encmedia = isQuotedImage ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
							const media = await alpha.downloadAndSaveMediaMessage(encmedia, `./sticker/${sender}`)
							exif.create('Created By', 'ZeeoneOfc', `stickwm_${sender}`)
							//ran = getRandom('.webp')
                        await ffmpeg(`./${media}`)
                            .input(media)
                            .on('start', function (cmd) {
                                console.log(`Started : ${cmd}`)
                            })
                            .on('error', function (err) {
                                console.log(`Error : ${err}`)
                                fs.unlinkSync(media)
                                 })
                            .on('end', async function () {
                                console.log('Finish')
                                exec(`webpmux -set exif ./sticker/stickwm_${sender}.exif ./sticker/${sender}.webp -o ./sticker/${sender}.webp`, async (error) => {
								if (error) return reply(lang.tryAgain())
								await alpha.sendMessage(from, fs.readFileSync(`./sticker/${sender}.webp`), sticker, {quoted: fgif})
								fs.unlinkSync(media)	
									fs.unlinkSync(`./sticker/${sender}.webp`)	
                                    fs.unlinkSync(`./sticker/stickwm_${sender}.exif`)
								})
								})
                           .addOutputOptions([`-vcodec`,`libwebp`,`-vf`,`scale='min(320,iw)':min'(320,ih)':force_original_aspect_ratio=decrease,fps=15, pad=320:320:-1:-1:color=white@0.0, split [a][b]; [a] palettegen=reserve_transparent=on:transparency_color=ffffff [p]; [b][p] paletteuse`])
							.toFormat('webp')
							.save(`./sticker/${sender}.webp`)
                    } else if ((isMedia && mek.message.videoMessage.seconds < 11 || isQuotedVideo && mek.message.extendedTextMessage.contextInfo.quotedMessage.videoMessage.seconds < 11) && args.length == 0) {
                        const encmedia = isQuotedVideo ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
                        const media = await alpha.downloadAndSaveMediaMessage(encmedia)
                        exif.create('Created By', 'ZeeoneOfc', `stickwm_${sender}`)
                    //    ran = getRandom('.webp')
                        await ffmpeg(`./${media}`)
                            .inputFormat(media.split('.')[1])
                            .on('start', function (cmd) {
                                console.log(`Started : ${cmd}`)
                            })
                            .on('error', function (err) {
                                console.log(`Error : ${err}`)
                                fs.unlinkSync(media)
                                tipe = media.endsWith('.mp4') ? 'video' : 'gif'
                                reply(`❌ Gagal, pada saat mengkonversi ${tipe} ke stiker`)
                            })
                            .on('end', async function () {
                                console.log('Finish')
                                exec(`webpmux -set exif ./sticker/stickwm_${sender}.exif ./sticker/${sender}.webp -o ./sticker/${sender}.webp`, async (error) => {
						if (error) return reply(lang.tryAgain())
								await alpha.sendMessage(from, fs.readFileSync(`./sticker/${sender}.webp`), sticker, {quoted: fgif})
								fs.unlinkSync(media)	
									fs.unlinkSync(`./sticker/${sender}.webp`)	
                                    fs.unlinkSync(`./sticker/stickwm_${sender}.exif`)
								})
								})
								.addOutputOptions([`-vcodec`,`libwebp`,`-vf`,`scale='min(320,iw)':min'(320,ih)':force_original_aspect_ratio=decrease,fps=15, pad=320:320:-1:-1:color=white@0.0, split [a][b]; [a] palettegen=reserve_transparent=on:transparency_color=ffffff [p]; [b][p] paletteuse`])
							.toFormat('webp')
						.save(`./sticker/${sender}.webp`)
                    } else if ((isMedia || isQuotedImage) && args[0] == 'nobg') {
                        const encmedia = isQuotedImage ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
                        const media = await alpha.downloadAndSaveMediaMessage(encmedia)
                        ranw = getRandom('.webp')
                        ranp = getRandom('.png')
                        reply(mess.wait)
                        keyrmbg = 'bcAvZyjYAjKkp1cmK8ZgQvWH'
                        await removeBackgroundFromImageFile({ path: media, apiKey: keyrmbg, size: 'auto', type: 'auto', ranp }).then(res => {
                            fs.unlinkSync(media)
                            let bufferir9vn5 = Buffer.from(res.base64img, 'base64')
                            fs.writeFileSync(ranp, bufferir9vn5, (err) => {
                                if (err) return reply('Gagal, Terjadi kesalahan, silahkan coba beberapa saat lagi.')
                            })
                            exec(`ffmpeg -i ${ranp} -vcodec libwebp -filter:v fps=fps=20 -lossless 1 -loop 0 -preset default -an -vsync 0 -s 512:512 ${ranw}`, (err) => {
                                fs.unlinkSync(ranp)
                                if (err) return reply(lang.tryAgain())
                                alpha.sendMessage(from, fs.readFileSync(ranw), sticker, { quoted: mek })
                                    fs.unlinkSync(ranw)
                                })
                            })
                    } else {
                        reply(`Kirim gambar dengan caption ${prefix}sticker atau tag gambar yang sudah dikirim\nDurasi sticker video 1-9 detik...`)
                    }
                    await limitAdd(sender, limit)
				            }
           break
		case 'toimg':{
		if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
		if (!isQuotedSticker) return reply('Reply stc nya!')
					reply(lang.wait())
					encmediaa = JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo
					mediaa = await alpha.downloadAndSaveMediaMessage(encmediaa)
					ran = getRandom('.png')
					exec(`ffmpeg -i ${mediaa} ${ran}`, (err) => {
					fs.unlinkSync(mediaa)
					if (err) return reply('Yah gagal, coba ulangi ^_^')
					buffer = fs.readFileSync(ran)
					fakethumb(buffer,'Webp To Image')
					fs.unlinkSync(ran)
					})
					await limitAdd(sender, limit)}
					break   
			case 'ytsearch': case 'yts':
			if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
					if (args.length < 1) return reply('Tolong masukan query!')
					var srch = args.join(' ');
					try {
		        	var aramas = await yts(srch);
		   			} catch {
		        	return await alpha.sendMessage(from, 'Error!', MessageType.text, dload)
		    		}
		    		aramat = aramas.all 
		    		var tbuff = await getBuffer(aramat[0].image)
		    		var ytresult = '';
		    		ytresult += '「 *YOUTUBE SEARCH* 」'
		    		ytresult += '\n________________________\n\n'
		   			aramas.all.map((video) => {
		        	ytresult += '🐣 Title: ' + video.title + '\n'
		            ytresult += '📬 Link: ' + video.url + '\n'
		            ytresult += '⏰ Durasi: ' + video.timestamp + '\n'
					ytresult += '👁️ Views: ' + video.views + '\n'
		            ytresult += '🚀 Upload: ' + video.ago + '\n________________________\n\n'
		    		});
		    		ytresult += '*WHATSAPP-BOT*'
		    		await fakethumb(tbuff,ytresult)
					await limitAdd(sender, limit)
					break   
			case 'setreply':
			case 'setfake':
			        if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					if (!q) return fakegroup(mess.wrongFormat)
					fake = q
					fakegroup(`Succes Mengganti Conversation Fake : ${q}`)
					break
			case 'setprefix':
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
reply('Pke yg multi aja')
/*if (args.length < 1) return reply(`*Format Error!*\n\n*Example :*\n •${prefix + command} multi\n •${prefix + command} nopref\n •${prefix + command} #`)
if((args[0]) == 'multi'){
if(multi)return reply('_Sudah diaktifkan sebelumnya!_')
multi = true
nopref = false
single = false
reply(`_Succses mengganti Prefix ke Multiprefix!_`)
}else
if ((args[0]) == 'nopref'){
if(nopref)return reply('_Sudah diaktifkan sebelumnya!_')
multi = false
single = false
nopref = true
reply(`_Succses mengganti Prefix ke noprefix!_`)
}else
if((args[0]) == `${q}`){
multi = false
nopref = false
single = true
prefa = `${q}`
reply(`_Succses mengganti Prefix ke ${q}_`)
}*/
break
			case 'setfakeimg':
			        if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
		        	if ((isMedia && !mek.message.videoMessage || isQuotedImage || isQuotedSticker) && args.length == 0) {
		            boij = isQuotedImage || isQuotedSticker ? JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo : mek
					delb = await alpha.downloadMediaMessage(boij)
					fs.writeFileSync(`./image/${fthumb}`, delb)
					fakestatus('Sukses')
		        	} else {
		            fakeitem(`Kirim gambar dengan caption ${prefix}setfakeimg`)
		          	}
					break	
			case 'setthumb':
			        if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
			        if ((isMedia && !mek.message.videoMessage || isQuotedImage || isQuotedSticker) && args.length == 0) {
		          	boij = isQuotedImage || isQuotedSticker ? JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo : mek
					delb = await alpha.downloadMediaMessage(boij)
					fs.writeFileSync(`./image/${thumbnail}`, delb)
					fakestatus('Sukses')
		        	} else {
		            fakegroup(`Kirim gambar dengan caption ${prefix}sethumb`)
		          	}
					break	
			case 'image':
			if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
		            if (args.length < 1) return fakegroup('Masukan teks!')
		            const gimg = args.join('');
gis(gimg, async (error, result) => {
n = result
images = n[Math.floor(Math.random() * n.length)].url
cptg = `*-------「 GIMAGE SEARCH 」-------*
⛄ *Query* : ${gimg}
🔗 *Media Url* : ${images}`
var imgnya = await getBuffer(images)
sendButImage(from,  cptg , `© ${ownername}`,imgnya, [{"buttonId": `image ${q}`,"buttonText": {"displayText": "Next Image"},"type": "RESPONSE"}], {quoted: mek})
			})
					await limitAdd(sender, limit)
					break   
		    
		    case 'brainly':
		if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
					if (args.length < 1) return reply('Pertanyaan apa')
		          	brien = args.join(' ')
					brainly(`${brien}`).then(res => {
					teks = '❉───────────────────────❉\n'
					for (let Y of res.data) {
					teks += `\n*「 _BRAINLY_ 」*\n\n*➸ Pertanyaan:* ${Y.pertanyaan}\n\n*➸ Jawaban:* ${Y.jawaban[0].text}\n❉──────────────────❉\n`
					}
					alpha.sendMessage(from, teks, text,{quoted:mek,detectLinks: false})                        
		            }).catch(e => {
					reply('Terjadi kesalahan, coba beberapa saat lagi')
					})             
					await limitAdd(sender, limit)
					break       
    case 'playstore':
    if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
            if(!q) return reply('lu nyari apa?')
            let play = await hx.playstore(q)
            let store = '❉─────────────────────❉\n'
            for (let i of play){
            store += `\n*「 *PLAY STORE* 」*\n
- *Nama* : ${i.name}
- *Link* : ${i.link}\n
- *Dev* : ${i.developer}
- *Link Dev* : ${i.link_dev}\n❉─────────────────────❉`
            }
            reply(store)
            await limitAdd(sender, limit)
					break   
		case 'linkwa':
case 'grupwa':
case 'groupwa':
case 'gcwa':
if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
            if(!q) return reply('cari group apa?')
            hx.linkwa(q)
            .then(result => {
            let res = '「 *GC WA* 」\n\n'
            for (let i of result) {
            res += `*Nama*: *${i.nama}\n*Link*: ${i.link}\n\n`
            }
            reply(res)
            });
            await limitAdd(sender, limit)
			break    
case 'lirik':
if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
            if(!q) return reply('lagu apa?')
            let song = await hx.lirik(q)
            sendMediaURL(from,song.thumb,song.lirik)
            await limitAdd(sender, limit)
			break  
    case 'anime':
    if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
 if(!q) return reply('Judul animenya?')
 zee.Anime(`${q}`).then(async data => {
                    let txt = `*-------「 ANIME-SEARCH 」-------*\n\n`
                    for (let i of data) {
                        txt += `*📫 Title :* ${i.judul}\n`
                        txt += `*📚 Url :* ${i.link}\n-----------------------------------------------------\n`
                    }
                    await sendFileFromUrl(from,data[0].thumbnail,txt,mek)
                })
                .catch((err) => {
                    reply(lang.tryAgain())
                })
            break
    case 'otaku':
    if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
            if(!q) return reply('Judul animenya?')
            let anime = await hx.otakudesu(q)
            rem = `*Judul* : ${anime.judul}
*Jepang* : ${anime.jepang}
*Rating* : ${anime.rate}
*Produser* : ${anime.produser}
*Status* : ${anime.status}
*Episode* : ${anime.episode}
*Durasi* : ${anime.durasi}
*Rilis* : ${anime.rilis}
*Studio* : ${anime.studio}
*Genre* : ${anime.genre}\n
*Sinopsis* :
${anime.desc}\n\n*Link Batch* : ${anime.batch}\n*Link Download SD* : ${anime.batchSD}\n*Link Download HD* : ${anime.batchHD}`
           var ram = await getBuffer(anime.img)
            alpha.sendMessage(from,ram,image,{quoted:mek,caption:rem})
            await limitAdd(sender, limit)
			break   
    case 'komiku':
    if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return sendButMessage(from, lang.limit(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
            if(!q) return reply(`judulnya?\n${prefix}komiku mao gakuin`)
            let komik = await hx.komiku(q)
            result = `*Title* : ${komik.title}\n
*Title Indo* : ${komik.indo}\n
*Update* : ${komik.update}\n
*Desc* : ${komik.desc}\n
*Chapter Awal* : ${komik.chapter_awal}
*Chapter Akhir* : ${komik.chapter_akhir}`
            sendMediaURL(from, komik.image,result)
            await limitAdd(sender, limit)
					break     
			case 'term':
			
			        if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					if (!q) return fakegroup(mess.wrongFormat)
					exec(q, (err, stdout) => {
					if (err) return fakegroup(`ALPHABOT:~ ${err}`)
					if (stdout) {
					fakegroup(stdout)
					}
					})
				    break 
		    case 'join':
		            if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
		            try {
		            if (!isUrl(args[0]) && !args[0].includes('whatsapp.com')) return reply(lang.erorLink())
		            hen = args[0]
		            if (!q) return fakestatus('Masukan link group')
		            var codeInvite = hen.split('https://chat.whatsapp.com/')[1]
		            if (!codeInvite) return fakegroup ('pastikan link sudah benar!')
		            var response = await alpha.acceptInvite(codeInvite)
		            fakestatus('```SUKSES JOIN GRUP```')
		            } catch {
		            fakegroup('```LINK ERROR!```')
		            }
		            break
		    case 'twmp4': case 'twitter':
if (args.length < 1) return reply('Link?')
lin = args[0]
reply(lang.wait())
zee.Twitter(`${lin}`).then(async data => {
                    let txt = `*----「 TWITTER DOWNLOADER 」----*\n\n`
                    txt += `*📫 Title :* ${data.title}\n`
                    txt += `*📟 Quality :* ${data.medias[1].quality}\n`
                    txt += `*💾 Size :* ${data.medias[1].formattedSize}\n`
                    txt += `*📚 Url :* ${data.url}`
                    sendFileFromUrl(from,data.medias[1].url,txt,mek)
                })
                .catch((err) => {
                    reply(lang.err())
                })
await limitAdd(sender, limit)
					break   
case 'twmp3':
if (args.length < 1) return reply('Link?')
lin = args[0]
reply(lang.wait())
hx.twitter(lin).then(async (res) => {
console.log('[ TWITTER ] downloader')
Anu = res.SD
fto = fs.readFileSync(`./image/${thumbnail}`)
alpha.sendMessage(from, fto, image, {quoted:mek, caption:`*TWITTER MP3*${enter}${enter}•> Hd : ${res.HD}${enter}•> Sd : ${res.SD}${enter}•> Audio : ${res.audio}${enter}${enter}_Please wait, the media file is being sent it may take a few minutes_`, thumbnail:fs.readFileSync(`./image/${thumbnail}`), contextInfo:{forwardingScore: 989, isForwarded: true}})
khs = await getBuffer(Anu)
alpha.sendMessage(from, khs, audio, {mimetype:'audio/mp4', filename:'alphagan.mp3', quoted:mek, ptt:true})
})
await limitAdd(sender, limit)
					break   
		    case 'runtime':
		    case 'test':
		            run = process.uptime() 
		            teks = `${kyun(runtime)}`
		            reply(teks)
		            break  
			case 'speed':
			case 'ping':
			const timestamp = speed();
					const latensi = speed() - timestamp
					exec(`neofetch --stdout`, (error, stdout, stderr) => {
					const child = stdout.toString('utf-8')
					const teks = child.replace(/Memory:/, "Ram:")
					const pingnya = `\`\`\`${teks}Speed: ${latensi.toFixed(4)} Second\`\`\``
					fakegroup(pingnya)
					})
					break
               
		    case 'totag':
		if (!isGroupAdmins) return reply(lang.onlygcAdmin())
		if ((isMedia && !mek.message.videoMessage || isQuotedSticker) && args.length == 0) {
		            encmedia = isQuotedSticker ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
		            file = await alpha.downloadAndSaveMediaMessage(encmedia, filename = getRandom())
		            value = args.join(" ")
		            var group = await alpha.groupMetadata(from)
		            var member = group['participants']
		            var mem = []
		            member.map(async adm => {
		            mem.push(adm.id.replace('c.us', 's.whatsapp.net'))
		            })
		            var options = {
		                contextInfo: { mentionedJid: mem },
		                quoted: mek
		            }
		            ini_buffer = fs.readFileSync(file)
		            alpha.sendMessage(from, ini_buffer, sticker, options)
		            fs.unlinkSync(file)
		            } else if ((isMedia && !mek.message.videoMessage || isQuotedImage) && args.length == 0) {
		            encmedia = isQuotedImage ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
		            file = await alpha.downloadAndSaveMediaMessage(encmedia, filename = getRandom())
		            value = args.join(" ")
		            var group = await alpha.groupMetadata(from)
		            var member = group['participants']
		            var mem = []
		            member.map(async adm => {
		            mem.push(adm.id.replace('c.us', 's.whatsapp.net'))
		            })
		            var options = {
		                contextInfo: { mentionedJid: mem },
		                quoted: mek
		            }
		            ini_buffer = fs.readFileSync(file)
		            alpha.sendMessage(from, ini_buffer, image, options)
		            fs.unlinkSync(file)
		        } else if ((isMedia && !mek.message.videoMessage || isQuotedAudio) && args.length == 0) {
		            encmedia = isQuotedAudio ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
		            file = await alpha.downloadAndSaveMediaMessage(encmedia, filename = getRandom())
		            value = args.join(" ")
		            var group = await alpha.groupMetadata(from)
		            var member = group['participants']
		            var mem = []
		            member.map(async adm => {
		            mem.push(adm.id.replace('c.us', 's.whatsapp.net'))
		            })
		            var options = {
		                mimetype : 'audio/mp4',
		                ptt : true,
		                contextInfo: { mentionedJid: mem },
		                quoted: mek
		            }
		            ini_buffer = fs.readFileSync(file)
		            alpha.sendMessage(from, ini_buffer, audio, options)
		            fs.unlinkSync(file)
		        }  else if ((isMedia && !mek.message.videoMessage || isQuotedVideo) && args.length == 0) {
		            encmedia = isQuotedVideo ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
		            file = await alpha.downloadAndSaveMediaMessage(encmedia, filename = getRandom())
		            value = args.join(" ")
		            var group = await alpha.groupMetadata(from)
		            var member = group['participants']
		            var mem = []
		            member.map(async adm => {
		            mem.push(adm.id.replace('c.us', 's.whatsapp.net'))
		            })
		            var options = {
		                mimetype : 'video/mp4',
		                contextInfo: { mentionedJid: mem },
		                quoted: mek
		            }
		            ini_buffer = fs.readFileSync(file)
		            alpha.sendMessage(from, ini_buffer, video, options)
		            fs.unlinkSync(file)
		        } else{
		          fakegroup(`reply gambar/sticker/audio/video dengan caption ${prefix}totag`)
		        }
		        await limitAdd(sender, limit)
					break   
		    case 'tomp4':
		            if ((isMedia && !mek.message.videoMessage || isQuotedSticker) && args.length == 0) {
		            ger = isQuotedSticker ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
		            let owogi = await alpha.downloadAndSaveMediaMessage(ger)
		            webp2mp4File(owogi).then(res=>{
		            sendMediaURL(from,res.result,'Done')
		            })
		            }else {
		            fakegroup('reply stiker')
		            }
		            fs.unlinkSync(owogi)
		            await limitAdd(sender, limit)
					break   
			case 'togif':
		            if ((isMedia && !mek.message.videoMessage || isQuotedSticker) && args.length == 0) {
		            ger = isQuotedSticker ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
		            let owoogi = await alpha.downloadAndSaveMediaMessage(ger)
		            webp2mp4File(owoogi).then(async res=>{
					let ksksn = await getBuffer(res.result)
		            alpha.sendMessage(from, ksksn, MessageType.video, {mimetype: 'video/gif', gifPlayback: true, caption: lang.success(), quoted: fgif })
		            })
		            }else {
		            fakegroup('Reply stiker')
		            }
		            fs.unlinkSync(owoogi)
		            await limitAdd(sender, limit)
					break   
		    case 'tourl':
			case 'imgtourl':{
                if ((isMedia && !mek.message.videoMessage || isQuotedImage || isQuotedVideo ) && args.length == 0) {
 									 boij = isQuotedImage || isQuotedVideo ? JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo : mek
									 owgi = await alpha.downloadMediaMessage(boij)
									 res = await uploadImages(owgi)
									 reply(res)
										} else {
											reply('kirim/reply gambar/video')
										}
										}
											await limitAdd(sender, limit)
					break   
/*
]=====> NSFW MENU<=====[
*/

			case 'awoo':
					if (!isNsfw) return reply(lang.nsfwmo())
					reply(lang.wait())
					anu = await fetchJson(`https://waifu.pics/api/sfw/awoo`)
					buffer = await getBuffer(anu.url)
					anu  = {contextInfo: {"forwardingScore":999,"isForwarded":true,'stanzaId': msgId, 'participant':`${numbernye}@s.whatsapp.net`, 'remoteJid': '6283136505591-1614953337@g.us', 'quotedMessage': {"locationMessage": {"degreesLatitude": 41.893714904785156, "degreesLongitude": -87.63370513916016, "name": fake , 'jpegThumbnail': fs.readFileSync(`image/${thumbnail}`)}}}}
                    alpha.sendMessage(from, buffer, image, anu)
					await limitAdd(sender, limit)
					break   
			case 'blowjob2':
					if (!isNsfw) return reply(lang.nsfwmo())
					reply(lang.wait())
					anu = await fetchJson(`https://nekos.life/api/v2/img/blowjob`)
					buffer = await getBuffer(anu.url)
					anu  = {contextInfo: {"forwardingScore":999,"isForwarded":true,'stanzaId': msgId, 'participant':`${numbernye}@s.whatsapp.net`, 'remoteJid': '6283136505591-1614953337@g.us', 'quotedMessage': {"locationMessage": {"degreesLatitude": 41.893714904785156, "degreesLongitude": -87.63370513916016, "name": fake , 'jpegThumbnail': fs.readFileSync(`image/${thumbnail}`)}}}}
                    alpha.sendMessage(from, buffer, image, anu)
					await limitAdd(sender, limit)
					break   
			case 'megumin':
					if (!isNsfw) return reply(lang.nsfwmo())
					reply(lang.wait())
					anu = await fetchJson(`https://waifu.pics/api/sfw/megumin`)
					buffer = await getBuffer(anu.url)
					anu  = {contextInfo: {"forwardingScore":999,"isForwarded":true,'stanzaId': msgId, 'participant':`${numbernye}@s.whatsapp.net`, 'remoteJid': '6283136505591-1614953337@g.us', 'quotedMessage': {"locationMessage": {"degreesLatitude": 41.893714904785156, "degreesLongitude": -87.63370513916016, "name": fake , 'jpegThumbnail': fs.readFileSync(`image/${thumbnail}`)}}}}
                    alpha.sendMessage(from, buffer, image, anu)
					await limitAdd(sender, limit)
					break   
			case 'trapnime':
					if (!isNsfw) return reply(lang.nsfwmo())
					reply(lang.wait())
					anu = await fetchJson(`https://waifu.pics/api/nsfw/trap`)
					buffer = await getBuffer(anu.url)
					anu  = {contextInfo: {"forwardingScore":999,"isForwarded":true,'stanzaId': msgId, 'participant':`${numbernye}@s.whatsapp.net`, 'remoteJid': '6283136505591-1614953337@g.us', 'quotedMessage': {"locationMessage": {"degreesLatitude": 41.893714904785156, "degreesLongitude": -87.63370513916016, "name": fake , 'jpegThumbnail': fs.readFileSync(`image/${thumbnail}`)}}}}
                    alpha.sendMessage(from, buffer, image, anu)
					await limitAdd(sender, limit)
					break   

/*
]=====> GROUP MENU<=====[
*/
  
			case 'add':  
			if (!isGroup) return reply(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isBotGroupAdmins) return reply(lang.botNotAdm())
                    if (args.length < 1) return reply('Yang mau di add?')
					if (args[0].startsWith('08')) return reply('Gunakan kode negara mas')
					orang = args[0] + '@s.whatsapp.net'
response = await alpha.groupAdd(from, [orang])
o = response.participants[0]
let inv = (Object.values(o))
if(inv[0].code == 409) return reply('Orang yang anda add sudah ada didalam Group!')
else if(inv[0].code == 403){
alpha.sendMessage(from, `User private\n\nMengirim Undangan Group Ke @${q.split('@')[0]}`, MessageType.text, {quoted: mek, contextInfo: {mentionedJid: [orang]}})
alpha.sendMessage(from, orang, inv[0].invite_code, inv[0].invite_code_exp, groupMetadata.subject , `Salah Satu Admin Mengundang Anda Masuk Ke Sini Silahkan Klik Bergabung Untuk Masuk`)
}
					break 
					case 'radd': case 'addreply':
					if (!isGroup) return reply(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isBotGroupAdmins) return reply(lang.botNotAdm())
if (mek.message.extendedTextMessage === undefined || mek.message.extendedTextMessage === null) return reply('Reply pesan yg ingin di Add!')
mentioned = mek.message.extendedTextMessage.contextInfo.mentionedJid
mentions(`Perintah di terima, Add: @${mentioned[0].split('@')[0]}`, mentioned, true)
alpha.groupAdd(from, mentioned)
break

case 'kick':
if (!isGroup) return reply(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isBotGroupAdmins) return reply(lang.botNotAdm())
if(!q)return reply(`*Format salah!*\n\n*Example : ${prefix + command} @tag*`)
if (!isBotGroupAdmins) return reply(mess.only.Badmin)
yau = q.split('@')[1] + '@s.whatsapp.net'
alpha.groupRemove(from, [yau])
reply(`Succses kick target!`)
break

case 'rkick': case 'kickreply':
if (!isGroup) return reply(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isBotGroupAdmins) return reply(lang.botNotAdm())
if (mek.message.extendedTextMessage === undefined || mek.message.extendedTextMessage === null) return reply('Reply pesan yg ingin di Kick!')
mentioned = mek.message.extendedTextMessage.contextInfo.mentionedJid
mentions(`Perintah di terima, mengeluarkan : @${mentioned[0].split('@')[0]}`, mentioned, true)
alpha.groupRemove(from, mentioned)
break
			case 'antilink':
if (!isGroup) return reply(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isBotGroupAdmins) return reply(lang.botNotAdm())
              if (args[0] == 'on'){
              if (isAntiLink) return reply(lang.anjawaUdhOn(command))
              antilink.push(from)
              fs.writeFileSync('./src/antilink.json', JSON.stringify(antilink))
              reply(lang.anjawaOn(command))
              } else if (args[0] == 'off'){
              let anu = antilink.indexOf(from)
              antilink.splice(anu, 1)
              fs.writeFileSync('./src/antilink.json', JSON.stringify(antilink))
              reply(lang.anjawaOff(command))
              } else if (!q) {
          sendButMessage(from, `MODE ANTILINK`, `Choose one`, [
            {
              buttonId: 'antilink on',
              buttonText: {
                displayText: `On`,
              },
              type: 1,
            },
            {
              buttonId: 'antilink off',
              buttonText: {
                displayText: `Off`,
              },
              type: 1,
            },
          ]);
        }
        break;
       case 'event':
					if (!isGroup) return reply(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if ( !isOwner && !isCreator && !mek.key.fromMe) return reply("Khusus admin");
					if (args[0] == "on") {
						if (isEventon) return reply(lang.anjawaUdhOn(command))
						event.push(from)
						fs.writeFileSync('./src/event.json', JSON.stringify(event))
						reply(lang.anjawaOn(command))
					} else if (args[0] == "off") {
						event.splice(from, 1)
						fs.writeFileSync('./src/event.json', JSON.stringify(event))
						reply(lang.anjawaOff(command))
					} else if (!q) {
          sendButMessage(from, `MODE EVENT`, `Choose one`, [
            {
              buttonId: 'event on',
              buttonText: {
                displayText: `On`,
              },
              type: 1,
            },
            {
              buttonId: 'event off',
              buttonText: {
                displayText: `Off`,
              },
              type: 1,
            },
          ]);
        }
        break;
	case 'antivirtex':
 if (!isGroup) return reply(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isBotGroupAdmins) return reply(lang.botNotAdm())       
        if (args[0] == "on") {
          if (isAntivirtex) return reply(lang.anjawaUdhOn(command))
          antivirtex.push(from);
          fs.writeFileSync(
            "./src/antivirtex.json",
            JSON.stringify(antivirtex)
          );
          reply(lang.anjawaOn(command))
        } else if (args[0] == "off") {
          antivirtex.splice(from, 1);
          fs.writeFileSync("./src/antivirtex.json", JSON.stringify(ant));
          reply(lang.anjawaOff(command))
        } else if (!q) {
          sendButMessage(from, `MODE ANTIVIRTEX`, `Choose one`, [
            {
              buttonId: 'antivirtex on',
              buttonText: {
                displayText: `On`,
              },
              type: 1,
            },
            {
              buttonId: 'antivirtex off',
              buttonText: {
                displayText: `Off`,
              },
              type: 1,
            },
          ]);
        }
        break;
			case 'admin':
					if (!isGroup) return fakestatus('```KHUSUS GRUP BRO```')
					teks = `*DAFTAR ATASAN GROUP* _${groupMetadata.subject}_\n*TOTAL* : ${groupAdmins.length}\n\n`
					no = 0
					for (let admon of groupAdmins) {
					no += 1
					teks += `[${no.toString()}] @${admon.split('@')[0]}\n`
					}
					mentions(teks, groupAdmins, true)
					break
			
			case 'tagall':
			if (!isGroup) return reply(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					members_id = []
					teks = (args.length > 1) ? body.slice(8).trim() : ''
					teks += '\n\n'
					for (let mem of groupMembers) {
					teks += `@${mem.jid.split('@')[0]}\n`
					members_id.push(mem.jid)
					}
					mentions(teks, members_id, true)
					break

			case 'clearall':
			        if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
			        anu = await alpha.chats.all()
					alpha.setMaxListeners(10)
					for (let _ of anu) {
					alpha.deleteChat(_.jid)
					}
					reply(lang.success())
					break
            case 'out':
                    if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					setTimeout( () => {
					alpha.groupLeave (from) 
					}, 2000)
					setTimeout( () => {
					alpha.updatePresence(from, Presence.composing) 
					reply('```Byeee 👋```')
					}, 0)
					break     
		    case 'leave2':
                    if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					setTimeout( () => {
					alpha.groupLeave (q) 
					}, 2000)
					setTimeout( () => {
					alpha.updatePresence(from, Presence.composing) 
					fakestatus('```Ok gua out```')
					}, 0)
					break       
           case 'getpp':
				if (mek.message.extendedTextMessage != undefined){
					let mentioneddd = mek.message.extendedTextMessage.contextInfo.mentionedJid
					try {
						pic = await alpha.getProfilePicture(mentioneddd[0])
					} catch {
						pic = 'https://i.ibb.co/Tq7d7TZ/age-hananta-495-photo.png'
					}
					seeer = `Nama : *${pushname}`
					thumbb = await getBuffer(pic)
					anuu  = {contextInfo:{"forwardingScore":999,"isForwarded":true,'stanzaId': "B826873620DD5947E683E3ABE663F263", 'participant': `${numbernye}@s.whatsapp.net`, 'remoteJid': '6289523258649-1604595598@g.us', 'quotedMessage': {"imageMessage": {"caption": `「 Bot by zeeone 」`, 'jpegThumbnail': fs.readFileSync(`image/${thumbnail}`)}}}}
                    alpha.sendMessage(from, thumbb ,image, anuu)
				}
				await limitAdd(sender, limit)
					break   
	case 'inspect':
		            try {
		            if (!isUrl(args[0]) && !args[0].includes('whatsapp.com')) return reply(lang.erorLink())
		            if (!q) return reply('```Masukkan link groupnya```')
		            cos = args[0]
		            var net = cos.split('https://chat.whatsapp.com/')[1]
		            if (!net) return reply('pastikan itu link https://whatsapp.com/')
		            jids = []
		            let { id, owner, subject, subjectOwner, desc, descId, participants, size, descOwner, descTime, creation} = await alpha.query({ 
		            json: ["query", "invite",net],
		            expect200:true })
		            let par = `*Id* : ${id}
		${owner ? `*Owner* : @${owner.split('@')[0]}` : '*Owner* : -'}
		*Nama Gc* : ${subject}
		*Gc dibuat Tanggal* : ${formatDate(creation * 1000)}
		*Jumlah Member* : ${size}
		${desc ? `*Desc* : ${desc}` : '*Desc* : tidak ada'}
		*Id desc* : ${descId}
		${descOwner ? `*Desc diubah oleh* : @${descOwner.split('@')[0]}` : '*Desc diubah oleh* : -'}\n*Tanggal* : ${descTime ? `${formatDate(descTime * 1000)}` : '-'}\n\n*Kontak yang tersimpan*\n`
		           for ( let y of participants) {
		             par += `> @${y.id.split('@')[0]}\n*Admin* : ${y.isAdmin ? 'Ya' : 'Tidak'}\n`
		             jids.push(`${y.id.replace(/@c.us/g,'@s.whatsapp.net')}`)
		             }
		             jids.push(`${owner ? `${owner.replace(/@c.us/g,'@s.whatsapp.net')}` : '-'}`)
		             jids.push(`${descOwner ? `${descOwner.replace(/@c.us/g,'@s.whatsapp.net')}` : '-'}`)
		             alpha.sendMessage(from,par,text,{quoted:mek,contextInfo:{mentionedJid:jids}})
		             } catch {
		             reply(lang.erorLink())
		             }
		             await limitAdd(sender, limit)
					break   
			case 'return':
			case 'cek':
			case 'me':
			if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					return alpha.sendMessage(from, JSON.stringify(eval(args.join(' '))), text, { quoted: ftroli})
					break
			case 'bc':
			case 'broadcast':
			case 'bcimage':
					if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					if (args.length < 1) return reply('```TEXT?```')
					arg = args.join(' ');
					anu = await alpha.chats.all()
					if (isMedia && !mek.message.videoMessage || isQuotedImage) {
					const encmedia = isQuotedImage ? JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo : mek					
					bc = await alpha.downloadMediaMessage(encmedia)
					for (let _ of anu) {
					await alpha.sendMessage(_.jid, bc, image, {thumbnail: bc, quoted:fkontak ,caption: `「  *BROADCAST* 」\n\n${arg}`})
					}
					fakegroup(lang.successBc())
					} else {
					await alpha.sendMessage(_.jid, arg, MessageType.text, {})
					await alpha.sendMessage(_.jid, arg, MessageType.text, {})
					await alpha.sendMessage(_.jid, arg, MessageType.text, {})
					await alpha.sendMessage(_.jid, arg, MessageType.text, {})
					await alpha.sendMessage(_.jid, arg, MessageType.text, {})
					await alpha.sendMessage(_.jid, arg, MessageType.text, {})
					await alpha.sendMessage(_.jid, arg, MessageType.text, {})
					await alpha.sendMessage(_.jid, arg, MessageType.text, {})
					}
					break
			case 'bcgc':
					case 'bcgroup':
					case 'bcgrup':
					case 'broadcastgrup':
		if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
                    if (args.length < 1) return reply(`Untuk broadcast ke semua group ketik:\n${prefix}bcgroup [isi chat]`)
                    var group = await alpha.groupMetadata(from)
			ini_bc = args.join(' ')
		var groupz = await alpha.chats.all().filter(v => v.jid.endsWith('g.us'))
                    reply(`\`\`\`[ ! ]\`\`\` Broadcast in progress! Total: ${groupz.length} groups`)
                    await ini_bc_gc_bang(ini_bc)
					reply(`\`\`\`[ ✓ ] Success broadcast : ${groupz.length} groups\`\`\``)
					break
			case 'buggc':
			if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					await alpha.toggleDisappearingMessages(from, 0)
					break
			case 'infogc':
					alpha.updatePresence(from, Presence.composing)
					if (!isGroup) return reply(lang.onlygc())
					try {
					ppimg = await alpha.getProfilePicture(from)
					} catch {
						ppimg = 'https://i.ibb.co/NthF8ds/IMG-20201223-WA0740.jpg'
					}
					let buf = await getBuffer(ppimg)
					teks = (args.length > 1) ? body.slice(8).trim() : ''
					teks += `*Nama grup :* ${groupName}\n*Deskripsi :* ${groupDesc}\n*Jumlah Admin :* ${groupAdmins.length}\n*Jumlah Member :* ${groupMembers.length}`
					no = 0
					for (let admon of groupAdmins) {
						no += 1
						teks += `[${no.toString()}]`
					}
					alpha.sendMessage(from, buf, image, {quoted: mek, caption: teks})
					await limitAdd(sender, limit)
					break   
			
                case 'memegenerator': case 'memegen':
									if (!isPremium && !mek.key.fromMe) return reply(mess.only.prem)
									if (args.length < 1) return reply(`Kirim perintah *${prefix + command}* teks atas|teks bawah`)
									if (!q.includes('|')) return reply(`Kirim perintah *${prefix + command}* teks atas|teks bawah`)
									try {
										if (!isQuotedImage) return reply(`Reply Gambar!`)
										reply(lang.wait())
										var teks1 = q.split('|')[0] ? q.split('|')[0] : ''
										var teks2 = q.split('|')[1] ? q.split('|')[1] : ''
										var enmedia = isQuotedImage ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
									   var mediiia = await alpha.downloadMediaMessage(enmedia)
										var njay = await uploadImages(mediiia)
										var resu = await getBuffer(`https://api.memegen.link/images/custom/${teks1}/${teks2}.png?background=${njay}`)
										alpha.sendMessage(from, resu, image, {caption:'.stikerin bang', quoted: mek})
										fs.unlinkSync(media)
										} catch (e) {
											console.log(e)
										}
										limitAdd(sender, limit)
									break
					 	case 'stickermeme': case 'memesticker': case 'memestick': case 'stickmeme': case 'stcmeme': case 'smeme':
						if (args.length < 1) return reply(`Kirim perintah *${prefix + command}* Alphabot`)
									if (q.includes('|')) return reply(`Kirim perintah *${prefix + command}* Alphabot`)
									try {
										if (!isQuotedImage) return reply(`Reply Gambar!`)
										reply(lang.wait())
										var teks2 = args.join(' ')
										var enmedia = isQuotedImage ? JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo : mek
										var mediia = await alpha.downloadMediaMessage(enmedia)
										var njay = await uploadImages(mediia)
										var resu = await getBuffer(`https://api.memegen.link/images/custom/-/${teks2}.png?background=${njay}`)
										alpha.sendMessage(from, resu, image, {caption:'.stiker', quoted: mek})
										fs.unlinkSync(media)
										} catch (e) {
											console.log(e)
										}
										limitAdd(sender, limit)
									break
             case 'demoteall':
			if (!isGroup) return reply(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isBotGroupAdmins) return reply(lang.botNotAdm())
			                members_id = []
					for (let mem of groupMembers) {
				   	members_id.push(mem.jid)
				  	}
			                alpha.groupDemoteAdmin(from, members_id)
			                break
			case 'promoteall':
			if (!isGroup) return reply(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isBotGroupAdmins) return reply(lang.botNotAdm())
                members_id = []
					for (let mem of groupMembers) {
				   	members_id.push(mem.jid)
				  	}
                alpha.groupMakeAdmin(from, members_id)
                break
              case 'promote':
					if (!isGroup) return reply(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isBotGroupAdmins) return reply(lang.botNotAdm())
					if (mek.message.extendedTextMessage === undefined || mek.message.extendedTextMessage === null) return
					mentionede = mek.message.extendedTextMessage.contextInfo.participant
alpha.groupMakeAdmin(from, [mentionede])
teks = `Members @${mentionede.split('@')[0]} succes promote`
alpha.sendMessage(from, teks, text, {quoted:mek, contextInfo:{mentionedJid:[mentionede]}})
break
				case 'demote':
					if (!isGroup) return reply(lang.onlygc())
					if (!isGroupAdmins) return reply(lang.onlygcAdmin())
					if (!isBotGroupAdmins) return reply(lang.botNotAdm())
					if (mek.message.extendedTextMessage === undefined || mek.message.extendedTextMessage === null) return
					mentionede = mek.message.extendedTextMessage.contextInfo.participant
alpha.groupDemoteAdmin(from, [mentionede])
teks = `Members @${mentionede.split('@')[0]} succes demote`
alpha.sendMessage(from, teks, text, {quoted:mek, contextInfo:{mentionedJid:[mentionede]}})
break
                
                /*
                ]----------------------------------------------------------------> API ZEKS <----------------------------------------------------------------[
                */
case 'captain_as':case 'smoke':case 'tiktok2': case 'arcade':case 'battlefield':case 'pubg':
if (args.length < 1) return reply(lang.tahta(prefix, command))
var m = q
var m1 = m.split("|")[0];
var m2 = m.split("|")[1]; 
let photooxy = await getBuffer(`${alphaapi}/photooxy/${command}?apikey=${alphakey}&text=${m1}&text2=${m2}`)
sendButImage(from,  `Nih udah jadi kak, jgn lupa donasi untuk beli dyno 🐦 ` , `© ${ownername}`,photooxy, [{"buttonId": `owner`,"buttonText": {"displayText": "👨‍💻 Owner"},"type": "RESPONSE"},{"buttonId": `donasi`,"buttonText": {"displayText": "💰 Donate"},"type": "RESPONSE"}], {thumbnail: Buffer.alloc(0), quoted: mek})
await  limitAdd(sender, limit)
break                         
case 'shadow':case 'cname':case 'romantic':case 'burnpaper':case 'funnycup':case 'love':case 'undergrass':          case 'heart':case 'coffeecup':case 'wood':          case 'flower':         case 'wooden': case '3dsummer':case 'wolf_metal':case '3dnature':case 'underwater':          case 'goldenrose':case 'vector':case 'typography':case 'typography2': case 'underfall':  case 'smokyneon': case 'rainbow': case 'graffiti':case 'camouflage':case '3dglowing':          case 'vintage':case 'honey': case 'whitecube':case 'avatar': case 'glowrainbow':case 'nightsky':case 'fur':case 'flaming': case 'crisp':case 'embroidery':case 'bcake':          case '3dligth':case 'metallic': case 'striking':case 'watermelon':         case 'butterfly':case 'harry':case 'glowneon':case 'coffecup2':          case 'luxury': case 'cemetery':case 'woodblock':case 'sweet':case 'simple':case 'bevel':case 'underflower':         case 'underflower2':
if (args.length < 1) return reply(lang.noteks(prefix, command))
let photooxy2 = await getBuffer(`${alphaapi}/photooxy/${command}?apikey=${alphakey}&text=${q}`)
sendButImage(from,  `Nih udah jadi kak, jgn lupa donasi untuk beli dyno 🐦 ` , `© ${ownername}`,photooxy2, [{"buttonId": `owner`,"buttonText": {"displayText": "👨‍💻 Owner"},"type": "RESPONSE"},{"buttonId": `donasi`,"buttonText": {"displayText": "💰 Donate"},"type": "RESPONSE"}], {thumbnail: Buffer.alloc(0), quoted: mek})
await  limitAdd(sender, limit)
break         
case 'halloween2':case 'horror':case 'game8bit':case 'layered':case 'glitch2':case 'coolg':case 'coolwg':case 'realistic':case 'space3d':case 'gtiktok':case 'stone':case 'marvel':case 'marvel2':case 'pornhub':case 'avengers':case 'metalr':case 'metalg':case 'metalg2':case 'halloween2':case 'lion':case 'wolf_bw':case 'wolf_g':case 'ninja':case '3dsteel':case 'horror2':case 'lava':case 'bagel':
if (args.length < 1) return reply(lang.tahta(prefix, command))
var m = q
var m1 = m.split("|")[0];
var m2 = m.split("|")[1]; 
let textpro = await getBuffer(`${alphaapi}/textpro/${command}?apikey=${alphakey}&text=${m1}&text2=${m2}`)
sendButImage(from,  `Nih udah jadi kak, jgn lupa donasi untuk beli dyno 🐦 ` , `© ${ownername}`,textpro, [{"buttonId": `owner`,"buttonText": {"displayText": "👨‍💻 Owner"},"type": "RESPONSE"},{"buttonId": `donasi`,"buttonText": {"displayText": "💰 Donate"},"type": "RESPONSE"}], {thumbnail: Buffer.alloc(0), quoted: mek})
await  limitAdd(sender, limit)
break 
 case 'blackpink':case 'rainbow2':case 'water_pipe':case 'halloween':case 'sketch':case 'sircuit':case 'discovery':case 'metallic2':case 'fiction':case 'demon':case 'transformer':case 'berry':case 'thunder':case 'magma':case '3dstone':case 'neon':case 'glitch':case 'harry_potter':case 'embossed':case 'broken':case 'papercut':case 'gradient':case 'glossy':case 'watercolor':case 'multicolor':case 'neon_devil':case 'underwater':case 'bear':case 'wonderfulg':case 'christmas':case 'neon_light':case 'snow':case 'cloudsky':case 'luxury2':case 'gradient2':case 'summer':case 'writing':case 'engraved':case 'summery':case '3dglue':case 'metaldark':case 'neonlight':case 'oscar':case 'minion':case 'holographic':case 'purple':case 'glossyb':case 'deluxe2':case 'glossyc':case 'fabric':case 'neonc':case 'newyear':case 'newyear2':case 'metals':case 'xmas':case 'blood':case 'darkg':case 'joker':case 'wicker':case 'natural':case 'firework':case 'skeleton':case 'balloon':case 'balloon2':case 'balloon3':case 'balloon4':case 'balloon5':case 'balloon6':case 'balloon7':case 'steel':case 'gloss':case 'denim':case 'decorate':case 'decorate2':case 'peridot':case 'rock':case 'glass':case 'glass2':case 'glass3':case 'glass4':case 'glass5':case 'glass6':case 'glass7':case 'glass8':case 'captain_as2':case 'robot':case 'equalizer':case 'toxic':case 'sparkling':case 'sparkling2':case 'sparkling3':case 'sparkling4':case 'sparkling5':case 'sparkling6':case 'sparkling7':case 'decorative':case 'chocolate':case 'strawberry':case 'koifish':case 'bread':case 'matrix':case 'blood2':case 'neonligth2':case 'thunder2':case '3dbox':case 'neon2':case 'roadw':case 'bokeh':case 'gneon':case 'advanced':case 'dropwater':case 'wall':case 'chrismast':case 'honey':case 'drug':case 'marble':case 'marble2':case 'ice':case 'juice':case 'rusty':case 'abstra':case 'biscuit':case 'wood':case 'scifi':case 'metalr':case 'purpleg':case 'shiny': case 'jewelry':case 'jewelry2':case 'jewelry3':case 'jewelry4':case 'jewelry5':case 'jewelry6':case 'jewelry7':case 'jewelry8':case 'metalh':case 'golden':case 'glitter':case 'glitter2':case 'glitter3':case 'glitter4':case 'glitter5':case 'glitter6':case 'glitter7':case 'metale':case 'carbon':case 'candy':case 'metalb':case 'gemb':case '3dchrome':case 'metalb2':case 'metalg':
if (args.length < 1) return reply(lang.noteks(prefix, command))
let textpro2 = await getBuffer(`${alphaapi}/textpro/${command}?apikey=${alphakey}&text=${q}`)
sendButImage(from,  `Nih udah jadi kak, jgn lupa donasi untuk beli dyno 🐦 ` , `© ${ownername}`,textpro2, [{"buttonId": `owner`,"buttonText": {"displayText": "👨‍💻 Owner"},"type": "RESPONSE"},{"buttonId": `donasi`,"buttonText": {"displayText": "💰 Donate"},"type": "RESPONSE"}], {thumbnail: Buffer.alloc(0), quoted: mek})
await  limitAdd(sender, limit)
break  
case 'tahta':  
                   if (args.length < 1) return reply(lang.noteks(prefix, command))
                   F = q
                   reply(lang.wait())
                   tahta = await getBuffer(`${ApiZeks}/api/hartatahta?text=${F}&apikey=${zeksApikey}`)
                   tahtah = `${lang.success()}\n\nPlease Subscribe https://youtu.be/w4iQ4rwA0mo`
                   sendImageMaker(tahta, tahtah, sender)
                  await  limitAdd(sender, limit)
                  break
       case 'ytgold':  
                   if (args.length < 1) return reply(lang.noteks(prefix, command))
                   F = q
                   reply(lang.wait())
                   ytgold = await getBuffer(`${ApiZeks}/api/gplaybutton?text=${F}&apikey=${zeksApikey}`)
                   ytgoldp = `${lang.success()}\n\nPlease Subscribe https://youtu.be/w4iQ4rwA0mo`
                   sendImageMaker(ytgold, ytgoldp, sender)
                   await  limitAdd(sender, limit)
                   break  
       case 'ytsilver':  
                   if (args.length < 1) return reply(lang.noteks(prefix, command))
                   F = q
                   reply(lang.wait())
                   ytsilver = await getBuffer(`${ApiZeks}/api/splaybutton?text=${F}&apikey=${zeksApikey}`)
                   ytsilverp = `${lang.success()}\n\nPlease Subscribe https://youtu.be/w4iQ4rwA0mo`
                   sendImageMaker(ytsilver, ytsilverp, sender)
                   await  limitAdd(sender, limit)
                   break              
     case 'nulis':
									reply(`*Example*\n${prefix}nuliskiri\n${prefix}nuliskanan\n${prefix}foliokiri\n${prefix}foliokanan`)
									break
						case 'nuliskiri':{
									if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return reply (`Limit kamu sudah habis silahkan kirim ${prefix}limit untuk mengecek limit`)
									if (args.length < 1) return reply(`Kirim perintah *${prefix}nuliskiri* teks`)
									reply(mess.wait)
									const tulisan = q
									const splitText = tulisan.replace(/(\S+\s*){1,9}/g, '$&\n')
									const fixHeight = splitText.split('\n').slice(0, 31).join('\n')
									spawn('convert', [
									'./media/nulis/images/buku/sebelumkiri.jpg',
									'-font',
									'./media/nulis/font/Indie-Flower.ttf',
									'-size',
									'960x1280',
									'-pointsize',
									'22',
									'-interline-spacing',
									'2',
									'-annotate',
									'+140+153',
									fixHeight,
									'./media/nulis/images/buku/setelahkiri.jpg'
									])
									.on('error', () => reply(lang.tryAgain()))
									.on('exit', () => {
										alpha.sendMessage(from, fs.readFileSync('./media/nulis/images/buku/setelahkiri.jpg'), image, {thumbnail:Buffer.alloc(0),quoted: mek, caption: `Jangan Malas`})
										limitAdd(sender, limit)
										})
									}
									break
						case 'nuliskanan':{
									if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return reply (`Limit kamu sudah habis silahkan kirim ${prefix}limit untuk mengecek limit`)
									if (args.length < 1) return reply(`Kirim perintah *${prefix}nuliskanan* teks`)
									reply(mess.wait)
									const tulisan = q
									const splitText = tulisan.replace(/(\S+\s*){1,9}/g, '$&\n')
									const fixHeight = splitText.split('\n').slice(0, 31).join('\n')
									spawn('convert', [
									'./media/nulis/images/buku/sebelumkanan.jpg',
									'-font',
									'./media/nulis/font/Indie-Flower.ttf',
									'-size',
									'960x1280',
									'-pointsize',
									'23',
									'-interline-spacing',
									'2',
									'-annotate',
									'+128+129',
									fixHeight,
									'./media/nulis/images/buku/setelahkanan.jpg'
									])
									.on('error', () => reply(lang.tryAgain()))
									.on('exit', () => {
										alpha.sendMessage(from, fs.readFileSync('./media/nulis/images/buku/setelahkanan.jpg'), image, {thumbnail:Buffer.alloc(0),quoted: mek, caption: `Jangan Malas`})
										limitAdd(sender, limit)
										})
									}
									break
						case 'foliokiri':{
									if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return reply (`Limit kamu sudah habis silahkan kirim ${prefix}limit untuk mengecek limit`)
									if (args.length < 1) return reply(`Kirim perintah *${prefix}foliokiri* teks`)
									reply(mess.wait)
									const tulisan = q
									const splitText = tulisan.replace(/(\S+\s*){1,13}/g, '$&\n')
									const fixHeight = splitText.split('\n').slice(0, 38).join('\n')
									spawn('convert', [
									'./media/nulis/images/folio/sebelumkiri.jpg',
									'-font',
									'./media/nulis/font/Indie-Flower.ttf',
									'-size',
									'1720x1280',
									'-pointsize',
									'23',
									'-interline-spacing',
									'4',
									'-annotate',
									'+48+185',
									fixHeight,
									'./media/nulis/images/folio/setelahkiri.jpg'
									])
									.on('error', () => reply(lang.tryAgain()))
									.on('exit', () => {
										alpha.sendMessage(from, fs.readFileSync('./media/nulis/images/folio/setelahkiri.jpg'), image, {thumbnail:Buffer.alloc(0),quoted: mek, caption: `Jangan Malas`})
										limitAdd(sender, limit)
										})
									}
									break
						case 'foliokanan':{
									if (isLimit(sender, isPremium, isCreator, isOwner, limitawal, limit)) return reply (`Limit kamu sudah habis silahkan kirim ${prefix}limit untuk mengecek limit`)
									if (args.length < 1) return reply(`Kirim perintah *${prefix}foliokanan* teks`)
									reply(mess.wait)
									const tulisan = q
									const splitText = tulisan.replace(/(\S+\s*){1,13}/g, '$&\n')
									const fixHeight = splitText.split('\n').slice(0, 38).join('\n')
									spawn('convert', [
									'./media/nulis/images/folio/sebelumkanan.jpg',
									'-font',
									'./media/nulis/font/Indie-Flower.ttf',
									'-size',
									'960x1280',
									'-pointsize',
									'23',
									'-interline-spacing',
									'3',
									'-annotate',
									'+89+190',
									fixHeight,
									'./media/nulis/images/folio/setelahkanan.jpg'
									])
									.on('error', () => reply(mess.error))
									.on('exit', () => {
										alpha.sendMessage(from, fs.readFileSync('./media/nulis/images/folio/setelahkanan.jpg'), image, {thumbnail:Buffer.alloc(0),quoted: mek, caption: `Jangan Malas`})
										limitAdd(sender, limit)
									})
									}
									break      
       case 'ttp':  
                    if (args.length < 1) return reply(lang.noteks(prefix, command))
                    ttp = args.join(' ')
                    anu1 = await getBuffer(`https://api.xteam.xyz/ttp?file&text=${ttp}`)
                    alpha.sendMessage(from, anu1, image, {quoted: mek, caption : '.stikerin'})
					.catch(e =>{
					reply(lang.tryAgain())})
					 await limitAdd(sender, limit)
					break   
         case 'attp':  
                    if (args.length < 1) return reply(lang.noteks(prefix, command))
                    hhhh = q
                    anu1 = await getBuffer(`https://api.xteam.xyz/attp?file&text=${hhhh}`)
                    alpha.sendMessage(from, anu1, sticker, {quoted: mek})
					.catch(e =>{
					reply(lang.tryAgain())})
                    await limitAdd(sender, limit)
					break   
             case 'ktpmaker': case 'ktp':
                    if (args.length == 0) return reply(`Usage: ${prefix + command} nik|provinsi|kabupaten|nama|tempat, tanggal lahir|jenis kelamin|jalan|rt/rw|kelurahan|kecamatan|agama|status nikah|pekerjaan|warga negara|berlaku sampai|url_image\n\nExample: ${prefix + command} 456127893132123|bumipertiwi|fatamorgana|LoL Human|mars, 99-99-9999|belum ditemukan|jl wardoyo|999/999|turese|imtuni|alhamdulillah islam|jomblo kack|mikirin dia|indo ori no kw|hari kiamat|https://i.ibb.co/Xb2pZ88/test.jpg`)
                    get_args = args.join(" ").split("|")
                    nik = get_args[0]
                    prov = get_args[1]
                    kabu = get_args[2]
                    name = get_args[3]
                    ttl = get_args[4]
                    jk = get_args[5]
                    jl = get_args[6]
                    rtrw = get_args[7]
                    lurah = get_args[8]
                    camat = get_args[9]
                    agama = get_args[10]
                    nikah = get_args[11]
                    kerja = get_args[12]
                    warga = get_args[13]
                    until = get_args[14]
                    img = get_args[15]
                    reply('waitt')
                    bikin = (`https://ferdiz-afk.my.id//api/maker/ktp?nik=${nik}&nama=${name}&ttl=${ttl}&jk=${jk}&gdarah=-&almt=${jl}&rt-rw=${rtrw}&kel=${lurah}&kcmtn=${camat}&agma=${agama}&status=${nikah}&kerja=${kerja}&negara=${warga}&berlaku=${until}&prov=${prov}&kab=${kabu}&picurl=${img}`)
                      console.log(bikin)
                    imge = await getBuffer(bikin)
                    await alpha.sendMessage(from, imge, image, { thumbnail: Buffer.alloc(0), quoted: mek });
                    await limitAdd(sender, limit)
					break 
        case 'nulis2':
if (args.length < 1) return reply(`*Usage*: ${prefix + command} nama&kelas&nomor&kata\n*Example*: ${prefix + command} udin&20&17&blablabla`)
var bodi = args.join(" ")
var nama = bodi.split("&")[0];
var kelas = bodi.split("&")[1];
var no = bodi.split("&")[2];
var aksarane = bodi.split("&")[3];
reply('membuat bos...')
                 rakz = await getBuffer(`https://ferdiz-afk.my.id//api/tulis?nama=${nama}&no=${no}&kelas=${kelas}&text=${aksarane}`)
                 alpha.sendMessage(from, rakz, image, { quoted: mek ,thumbnail: Buffer.alloc(0) });
await limitAdd(sender, limit)
					break   
              /*
              ]----------------------------------------------------------------> STORAGE <----------------------------------------------------------------[
              */
	        case 'addstik':
	if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					if (!isQuotedSticker) return fakestatus('Reply stiker')
					nm = body.slice(9)
					if (!nm) return reply('Nama sticker nya apa?')
					boij = JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo
					delb = await alpha.downloadMediaMessage(boij)
					setiker.push(`${nm}`)
					fs.writeFileSync(`./media/sticker/${nm}.webp`, delb)
					fs.writeFileSync('./temp/stik.json', JSON.stringify(setiker))
					fakegroup(`Sukses Menambahkan Sticker\nCek dengan cara ${prefix}liststik`)
					break
	      case 'liststik':
	      case 'liststiker':
	      case 'liststc':
					teks = '*Sticker list :*\n\n'
					for (let awokwkwk of setiker) {
						teks += `- ${awokwkwk}\n`
					}
					teks += `\n*Total : ${setiker.length}*\n\n_Untuk mengambil sticker silahkan reply pesan ini dengan caption nama sticker_`
					alpha.sendMessage(from, teks.trim(), extendedText, { quoted: mek, contextInfo: { "mentionedJid": setiker } })
					break
					
			case 'addimg':
			if(!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					if (!isQuotedImage) return fakegroup('```Reply imagenya```')
					clara = body.slice(8)
					if (!clara) return fakegroup('```Nama imagenya apa```')
					keya = JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo
					delb = await alpha.downloadMediaMessage(keya)
					imagenye.push(`${svst}`)
					fs.writeFileSync(`./media/foto/${svst}.jpg`, delb)
					fs.writeFileSync('./temp/image.json', JSON.stringify(imagenye))
					fakegroup(`Sukses Menambahkan image\nCek dengan cara ${prefix}listimg`)
					break
			case 'listimg':
					teks = '*Image list :*\n\n'
					for (let awokwkwk of imagenye) {
						teks += `- ${awokwkwk}\n`
					}
					teks += `\n*Total : ${imagenye.length}*\n\n_Untuk mengambil sticker silahkan reply pesan ini dengan caption nama foto/image_`
					fakegroup(from, teks.trim(), extendedText, { quoted: mek, contextInfo: { "mentionedJid": setiker } })
					break
			case 'addvid':
			if(!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					if (!isQuotedVideo) return fakegroup('```Reply vidionya```')
					svst = body.slice(8)
					if (!svst) return fakegroup('```Nama vidionya apa```')
					keya = JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo
					delb = await alpha.downloadMediaMessage(keya)
					imagenye.push(`${svst}`)
					fs.writeFileSync(`./media/video/${svst}.mp4`, delb)
					fs.writeFileSync('./temp/video.json', JSON.stringify(imagenye))
					fakegroup(`Sukses Menambahkan video\nCek dengan cara ${prefix}listvideo`)
					break
	        case 'listvid':
					teks = '*List Video :*\n\n'
					for (let awokwkwk of videonye) {
						teks += `- ${awokwkwk}\n`
					}
					teks += `\n*Total : ${videonye.length}* \n\n_Untuk mengambil sticker silahkan reply pesan ini dengan caption nama video_`
					alpha.sendMessage(from, teks.trim(), extendedText, { quoted: mek, contextInfo: { "mentionedJid": imagenye } })
					break
			
			case 'addvn':
			if(!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					if (!isQuotedAudio) return fakegroup('```Reply vnnya```')
					svst = body.slice(7)
					if (!svst) return reply('```Nama audionya apa```')
					keya = JSON.parse(JSON.stringify(mek).replace('quotedM', 'm')).message.extendedTextMessage.contextInfo
					delb = await alpha.downloadMediaMessage(keya)
					audionye.push(`${svst}`)
					fs.writeFileSync(`./media/audio/${svst}.mp3`, delb)
					fs.writeFileSync('./temp/vn.json', JSON.stringify(audionye))
					fakegroup( `Sukses Menambahkan Audio\nCek dengan cara ${prefix}listvn`)
					break
           
			case 'listvn':
					teks = '*List Vn:*\n\n'
					for (let awokwkwk of audionye) {
						teks += `- ${awokwkwk}\n`
					}
					teks += `\n*Total : ${audionye.length}*\n\n_Untuk mengambil sticker silahkan reply pesan ini dengan caption nama audio_`
					alpha.sendMessage(from, teks.trim(), extendedText, { quoted: mek, contextInfo: { "mentionedJid": audionye } })
					break
			case 'addrespon':
			if(!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					if(!q) return reply(`ketik perintah ${prefix + command} filter|jawab!`)
					fltr = q.split('|')[0]
					jwb = q.split('|')[1]
					if(!jwb) return reply('Format salah!')
					for(let i of filter){
					  if(fltr.includes(i.Filter)) return reply(`Filter ${fltr} sudah ada didatabase`)
					}
					const chat = {
					Filter : fltr,
					Jawaban : jwb
					}
					filter.push(chat)
					fs.writeFileSync('./src/filter.json', JSON.stringify(filter))
					reply(`Sukses menambahkan filter ${fltr}\nCek dengan cara ${prefix}listchatrespon`)
					break
					
			case 'delrespon':
			if(!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
					for(let i=0; i<filter.length; i++){
					if(q.includes(filter[i].Filter)){
					   obj = {
					      txt: filter[i].text,
					      balesan: filter[i].balesan
					   }
					   let del = filter.indexOf(filter[i])
					   filter.splice(del, 1)
					   fs.writeFileSync('./src/filter.json', JSON.stringify(filter))
					   reply(`Sukses Menghapus Respon ${q}`)
					}
					}
					break
case 'listrespon':
   teks = 'List Respon:\n'
   for (let i of filter) {
   teks += `• Filter : ${i.Filter}\n• Jawab : ${i.Jawaban}\n---------------------------\n`
   }
   teks += `Total : ${filter.length}`
   alpha.sendMessage(from, teks.trim(), extendedText, {quoted: mek})
   break
		case 'caripesan2':
            if(!q)return reply('Masukkan pesan yg mau di cari')
            let v = await alpha.searchMessages(q,from,10,1)
            let s = v.messages
            let el = s.filter(v => v.message)
            el.shift()
            try {
            if(el[0].message.conversation == undefined) return
            reply(`Ditemukan ${el.length} pesan`)
            await sleep(3000)
            for(let i = 0; i < el.length; i++) {
            await alpha.sendMessage(from,'Nih pesannya',text,{quoted:el[i]})
            }
            } catch(e){
            reply('Pesan tidak ditemukan!')
            }           
            await limitAdd(sender, limit)
					break   
     case 'searchmsg':  
             if (args.length < 1) return reply(`Pesan Yang Mau Dicari Apaan?\nContoh : ${command} halo|10`)
             teks = arg
             if (teks.includes("|")) { 
             try {
             var ve = teks.split("|")[0]
             var za = teks.split("|")[1]
             sampai = `${za}`
             if (isNaN(sampai)) return reply('Harus berupa Angka!')
             batas = parseInt(sampai) + 1
             if (batas > 20) return reply('Maks 20!')
             reply(lang.wait())
             cok = await nino.searchMessages(`${ve}`, from, batas,1) 
             if (cok.messages.length < 2) return reply('Tidak Ditemukan Pesan') 
             if (cok.messages.length < parseInt(batas)) reply(`Hanya Ditemukan ${cok.messages.length - 1} Pesan`)
             for (i=1;i < cok.messages.length;i++) {
             if (cok.messages[i].message) {
             alpha.sendMessage(from, `Ditemukan!`, text, {sendEphemeral: true, quoted: cok.messages[i]}) 
			}
			}
             } catch (e) {
             return reply(String(e))}
             } else {
             reply(`Format salah, format yang benar : ${command} halo|10`)}
             await limitAdd(sender, limit)
					break   
    case 'hash':
                try {
                if (!isQuotedSticker) return reply('Reply Sticker!')
                const encmeds = JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo
                const mediastick = await alpha.downloadMediaMessage(encmeds)
                var crypto = require('crypto')
                hash = crypto.createHash('sha256').update(mediastick).digest('base64');
                console.log(hash)
                reply (hash)
                } catch {
                	reply(`reply stiker dengan command ${prefix}hash`)
	}
            await limitAdd(sender, limit)
					break   
    case 'delvote':
            if(!isGroupAdmins && !mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlygcAdmin())
            if(isVote) return reply(lang.noSesiVote())
            delVote(from)
            reply(lang.suksesDelVot())
            break
    case 'voting':
            if(!isGroupAdmins && !mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlygcAdmin())
            if(!isGroup) return reply(lang.onlygc())
            if (isVote) return reply(lang.adaVoting())
            if(!q) return reply(lang.caraVoting())
            if (mek.message.extendedTextMessage.contextInfo.mentionedJid.length > 0 || mek.message.extendedTextMessage.contextInfo == null) {
            let id = mek.message.extendedTextMessage.contextInfo.mentionedJid[0]
            split = args.join(' ').replace('@', '').split('|')
            if(!Number(split[2])) return reply(lang.caraVot(prefix, command))
            await mentions('Vote ' +'@'+ id.split('@')[0]+' Di Mulai' +'\n\n' + `vote = ✅\ndevote = ❌\n\nAlasan: ${split[1]}`,[id],true)
            addVote(from,split[1],split[0],split[2],reply)
            }
            await limitAdd(sender, limit)
					break   
		case 'stopjadibot':
			    if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
			    stopjadibot(reply)
			    break
		case 'listbot':
			    let tekss = '「 *LIST JADIBOT* 」\n'
			    for(let i of listjadibot) {
			    tekss += `*Number* : ${i.jid.split('@')[0]}
*Name* : ${i.name}
*Device* : ${i.phone.device_manufacturer}
*Model* : ${i.phone.device_model}\n\n`
			    }
			    reply(tekss)
		case 'addcmd': 
       case 'setcmd':
              if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
              if (isQuotedSticker) {
              if (!q) return reply(`Penggunaan : ${command} cmdnya dan tag stickernya`)
              var kodenya = mek.message.extendedTextMessage.contextInfo.quotedMessage.stickerMessage.fileSha256.toString('base64')
              addCmd(kodenya, q)
              reply(lang.success())
              } else {
              reply('Reply stickenya')
}
              break
       case 'delcmd':
              if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
              if (!isQuotedSticker) return reply(`Penggunaan : ${command} tagsticker`)
              var kodenya = mek.message.extendedTextMessage.contextInfo.quotedMessage.stickerMessage.fileSha256.toString('base64')
            scommand.splice(getCommandPosition(kodenya), 1)
              fs.writeFileSync('./lib/scommand.json', JSON.stringify(scommand))
              reply(lang.success())
              break
       case 'listcmd':
              let teksnyee = `「 *LIST STICKER CMD* 」`
              let cemde = [];
              for (let i of scommand) {
              cemde.push(i.id)
              teksnyee += `\n\n📍 *ID :* ${i.id}\n📍 *Cmd* : ${i.chats}`
}
              mentions(teksnyee, cemde, true)
              break
      case 'delttt':
case 'delttc':
               if (!isGroup) return reply(lang.onlygc())
              // if (!isTTT) return reply('Tidak Ada Permainan Di Grub Ini')
               delete tictactoe[senderNumber]
fs.writeFileSync("./src/tictactoe.json", JSON.stringify(tictactoe))                        
if (fs.existsSync('./temp/' + from + '.json')) {
fs.unlinkSync('./temp/' + from + '.json')
reply(lang.suksesDelTtt())
}
               break
        case 'cekhistory':
reply(` S T A T U S  T I C T A C T O E ${enter}•> Win : ${checkWin(sender)}${enter}•> Lose : ${checkLose(sender)}`)
break
case 'delsesi':
if (!isGroupAdmins && !mek.key.fromMe && !isOwner) return reply('Hanya bisa didelete oleh admin group dan owner bot')
if (args[0] === 'ttt') {
delete tictactoe[senderNumber]
fs.writeFileSync("./src/tictactoe.json", JSON.stringify(tictactoe))                        
if (fs.existsSync('./temp/' + from + '.json')) {
fs.unlinkSync('./temp/' + from + '.json')
reply(lang.noSesiTtt())
}
} else if (args[0] === 'vote') {
if(isVote) return reply(lang.noSesiVote())
            delVote(from)
            reply(lang.sukseDelVot())
} else {
	reply(`${prefix + command}delsesi ttt atau vote`)
}
break

case 'tictactoe':
case 'ttt':
if (!isGroup)return reply('*Khusus group*')
if (mek.message.extendedTextMessage.contextInfo.mentionedJid > 1) return reply('Hanya bisa dengan 1 orang')
if (!mek.message.extendedTextMessage.contextInfo.mentionedJid[0]) return
if (fs.existsSync(`./temp/${from}.json`)) return reply(`Sedang Ada Sesi, tidak dapat dijalankan secara bersamaan${enter}Ketik *${prefix}delsesi ttt*, untuk menghapus sesi`)
if (args.length === 0) return reply(`Tag Lawan Yang Ingin Diajak Bermain Game`)
tttSkuy = setTtt(`${from}`)
tttSkuy.status = false
tttSkuy.Z = sender.replace("@s.whatsapp.net", "")
tttSkuy.Y = args[0].replace("@", "");
fs.writeFileSync(`./temp/${from}.json`, JSON.stringify(tttSkuy, null, 2))
starGame = `「 *MEMULAI GAME TICTACTOE* 」${enter}${enter}•@${sender.replace("@s.whatsapp.net", "")} Menantang Bermain Tictactoe ${enter}[ ${args[0]} ] Ketik Y/N untuk menerima atau menolak permainan${enter}${enter}`
alpha.sendMessage(from, starGame, text, {quoted: mek, contextInfo: { mentionedJid: [sender, args[0].replace("@", "") + "@s.whatsapp.net"],}})
await limitAdd(sender, limit)
					break   
             case 'size':
if (args.length < 1) return reply('Masukan angkanya')
filsize = args[0]
costick = await alpha.prepareMessageFromContent(from,{
"stickerMessage": {
"url": m.quoted.url,
"fileSha256": m.quoted.fileSha256.toString('base64'),
"fileEncSha256": m.quoted.fileEncSha256.toString('base64'),
"mediaKey": m.quoted.mediaKey.toString('base64'),
"mimetype": m.quoted.mimetype,
"height": m.quoted.height,
"width": m.quoted.width,
"directPath": m.quoted.directPath,
"fileLength": filsize,
"mediaKeyTimestamp": m.quoted.mediaKeyTimestamp.low,
"isAnimated": m.quoted.isAnimated
}
}, {quoted:mek})
alpha.relayWAMessage(costick)
await limitAdd(sender, limit)
					break   
case "colongsw": 
        if (!mek.key.fromMe) return
        if ((isMedia && !mek.message.videoMessage) || isQuotedImage) {
          ger = isQuotedImage
            ? JSON.parse(JSON.stringify(mek).replace("quotedM", "m")).message
                .extendedTextMessage.contextInfo
            : mek;
          owgi = await alpha.downloadAndSaveMediaMessage(ger);
          alpha.sendMessage(sender, fs.readFileSync(owgi), "imageMessage", {
            caption: q,
          });
          reply("Sukses");
          fs.unlinkSync(owgi);
        } else if ((isMedia && !mek.message.videoMessage) || isQuotedVideo) {
          ger = isQuotedVideo
            ? JSON.parse(JSON.stringify(mek).replace("quotedM", "m")).message
                .extendedTextMessage.contextInfo
            : mek;
          owgi = await alpha.downloadAndSaveMediaMessage(ger);
          alpha.sendMessage(sender, fs.readFileSync(owgi), "videoMessage", {
            caption: q,
          });
          reply("Sukses");
          fs.unlinkSync(owgi);
        } else {
          reply("Reply sw foto / video yg mau dicolong")
        }
        break
       case "listonline": 
        let id = args && /\d+\-\d+@g.us/.test(args[0]) ? args[0] : m.chat;
        try {
          let online = [
            ...Object.keys(alpha.chats.get(id).presences),
            alpha.user.jid,
          ];
          alpha.reply(
            m.chat,
            "「 L I S T   O N L I N E  」\n" +
              online.map((v) => "├ @" + v.replace(/@.+/, "")).join`\n` +
              "\n",
            m,
            {
              contextInfo: { mentionedJid: online },
            }
          );
        } catch (e) {
          m.reply("");
        }
        break;
        case 'getname':
 try {
getnem = alpha.getName(mek.quoted.sender)
reply(`${getnem}`)
} catch {
	reply ('Reply pesan @user')
	}
await limitAdd(sender, limit)
					break   
case 'linkgrup':
case 'linkgroup':
				case 'linkgc':
				    if (!isGroup) return reply(lang.onlygc())
				    if (!isBotGroupAdmins) return reply('Only admin')
				    linkgc = await alpha.groupInviteCode (from)
				    yeh = `https://chat.whatsapp.com/${linkgc}\n\nlink Group *${groupName}*`
				    alpha.sendMessage(from, yeh, text, {quoted: mek})
			        await limitAdd(sender, limit)
					break   
		case 'unpin':
                if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
                alpha.modifyChat(from, ChatModification.unpin)
                reply('*succes unpin this chat*')
                console.log('unpin chat = ' + from)
                break
        case 'pin':
                if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
                alpha.modifyChat(from, ChatModification.pin)
                reply('*succes pin this chat*')
                console.log('pinned chat = ' + from)
                break
         case 'unreadall':
                if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
                var chats = await alpha.chats.all()
                chats.map( async ({ jid }) => {
                await alpha.chatRead(jid, 'unread')
                    })
		    reply(`\`\`\`Successfully unread ${chats.length} chats !\`\`\``)
		    console.log(chats.length)
	        break
	        
            case 'readall':
                if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
                var chats = await alpha.chats.all()
                chats.map( async ({ jid }) => {
                await alpha.chatRead(jid)
                })
		reply(`\`\`\`Successfully read ${chats.length} chats !\`\`\``)
	      console.log(chats.length)
		break
		case 'unarchiveall':
                if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
                reply('*succes unarchive all chat*')
                console.log('succes unarchive chat = ' + from)
                anu = await alpha.chats.all()
                for (let _ of anu) {
                alpha.modifyChat(_.jid, ChatModification.unarchive)
                }
                break
                
            case 'archive':
                if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
                reply(lang.wait())
                console.log('succes archive chat = ' + from)
                await sleep(3000)
                alpha.modifyChat(from, ChatModification.archive)
                break
           case 'delthischat':
                if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
                console.log('succes delete chat = ' + from)
                await sleep(4000)
                await alpha.modifyChat(from, ChatModification.delete)
                reply('*succes delete this chat*')
                break
            case 'ssweb':
            case 'ss':
                if (args.length < 1) return reply('Urlnya mana om')
					teks = q
					anu = await fetchJson(`https://shot.screenshotapi.net/screenshot?&url=${teks}`)
					buff = await getBuffer(anu.screenshot)
					alpha.sendMessage(from, buff, image, {quoted: mek, caption : teks})
					await limitAdd(sender, limit)
					break   
			case 'artinama':
                if (args.length < 1) return reply('Apa yang mau dicari um?')
                teks = q
					anu = await fetchJson(`https://mnazria.herokuapp.com/api/arti?nama=${teks}`, {method: 'get'})
					reply(`Arti Nama ${teks}\n\n`+anu.result)
				await limitAdd(sender, limit)
					break   
			case 'halah': case 'hilih': case 'huluh': case 'heleh': case 'holoh':
ter = command[1].toLowerCase()
  tex = m.quoted ? m.quoted.text ? m.quoted.text : q ? q : m.text : q ? q : m.text
 reply(tex.replace(/[aiueo]/g, ter).replace(/[AIUEO]/g, ter.toUpperCase()))
 await limitAdd(sender, limit)
					break   
 case 'getexif':
try {
    if (!m.quoted) return reply('Tag stikernya!')
    cok = { message: { [m.quoted.mtype]: m.quoted } }
    if (/sticker/.test(m.quoted.mtype)) {
        let img = new webp.Image()
        await img.loadBuffer(await m.quoted.download())
        reply(util.format(JSON.parse(img.exif.slice(22).toString())))
    }
    } catch (e) {
    	throw e
    reply(String(e))
    }
    await limitAdd(sender, limit)
					break   
		case 'afk':
			if (!isGroup) return reply(lang.onlygc())
            if (isAfkOn) return 
                reason = q ? q : 'Nothing'
                off.addAfkUser(sender, Date.now(), reason, _off)
               papa =  `*${pushname}* Sekarang sedang Afk\n*Reason :* ${reason}\n`
                alpha.sendMessage(from,papa, text,{quoted : mek})
            break
        case 'autoread':
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
if (args.length < 1) return reply(`Example:\n${prefix}autoread gc on`)
if (args[0] === "gc") {
if (args.length < 2) return reply(`Example:\n${prefix}autoread gc on`)
if (args[1] === "on") {
if (readGc === true) return reply(lang.anjawaUdhOn(command))
readGc = true
reply(`Succes mengaktifkan autoread group`)
} else if (args[1] === "off") {
if (readGc === false) return
readGc = false
reply(`Succes mematikan autoread group`)
} else {
reply(`Pilih on atau off`)
}
} else if (args[0] === "pc") {
if (args.length < 2) return reply(`Example:\n${prefix}autoread pc on`)
if (args[1] === "on") {
if (readPc === true) return reply(lang.anjawaUdhOn(command))
readPc = true
reply(`Succes mengaktifkan autoread pc`)
} else if (args[1] === "off") {
if (readPc === false) return
readPc = false
reply(`Succes mematikan autoread pc`)
} else {
reply(`Pilih on atau off`)
}
} else {
reply(`*List Auto Read*\n•> gc\n•> pc`)
}
break
case 'nsfw':
					    if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
						if (!isGroup) return reply(lang.onlygc()) 
						if (args.length < 1) return reply(lang.anjawaUdhOon(command))
						if (args[0] === 'on') {
						if (isNsfw) return reply(lang.anjawaUdhOn(command))
						_nsfw.push(from)
						fs.writeFileSync('./src/nsfw.json', JSON.stringify(_nsfw))
						reply(lang.anjawaOn(command))
						} else if (args[0] === 'off') {
						_nsfw.splice(from, 1)
						fs.writeFileSync('./src/nsfw.json', JSON.stringify(_nsfw))
						reply(lang.anjawaOff(command))
						} else if (!q) {
          sendButMessage(from, `MODE NSFW`, `Choose one`, [
            {
              buttonId: 'nsfw on',
              buttonText: {
                displayText: `On`,
              },
              type: 1,
            },
            {
              buttonId: 'nsfw off',
              buttonText: {
                displayText: `Off`,
              },
              type: 1,
            },
          ]);
        }
        break;
case 'antibug':
          if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
          if (args[0] === 'on') {
          if (bugc === true) return reply(lang.anjawaUdhOn(command))
          bugc = true
          antitrol = true
          reply(lang.anjawaOn(command))
          } else if (args[0] === 'off') {
          if (bugc === false) return
          bugc = false
          antitrol = false
          reply(lang.anjawaOff(command))
          } else if (!q) {
          sendButMessage(from, `MODE ANTIBUG`, `Choose one`, [
            {
              buttonId: 'antibug on',
              buttonText: {
                displayText: `On`,
              },
              type: 1,
            },
            {
              buttonId: 'antibug off',
              buttonText: {
                displayText: `Off`,
              },
              type: 1,
            },
          ]);
        }
        break;
          case 'antidelete':
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
if (args[0] === "on") {
if (antidel === true) return reply(lang.anjawaUdhOn(command))
antidel = true
reply(lang.anjawaOn(command))
} else if (args[0] === "off") {
if (antidel === false) return
antidel = false
reply(lang.anjawaOff(command))
} else if (!q) {
          sendButMessage(from, `MODE ANTI DELETE`, `Choose one`, [
            {
              buttonId: 'antidelete on',
              buttonText: {
                displayText: `On`,
              },
              type: 1,
            },
            {
              buttonId: 'antidelete off',
              buttonText: {
                displayText: `Off`,
              },
              type: 1,
            },
          ]);
        }
        break;
        case 'welcome':
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
if (args[0] === "on") {
if (welcome === true) return reply(lang.anjawaUdhOn(command))
welcome = true
leave = true
reply(lang.anjawaOn(command))
} else if (args[0] === "off") {
if (welcome === false) return
welcome = false
leave = false
reply(lang.anjawaOff(command))
} else if (!q) {
          sendButMessage(from, `MODE AUTO WELCOME`, `Choose one`, [
            {
              buttonId: 'welcome on',
              buttonText: {
                displayText: `On`,
              },
              type: 1,
            },
            {
              buttonId: 'welcome off',
              buttonText: {
                displayText: `Off`,
              },
              type: 1,
            },
          ]);
        }
        break;
case 'anticall':
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
if (args.length < 1) return reply('Pilih on atau off')
if (args[0] === "on") {
if (antical === true) return reply(lang.anjawaUdhOn(command))
antical = true
reply(lang.anjawaOn(command))
} else if (args[0] === "off") {
if (antical === false) return
antical = false
reply(lang.anjawaOff(command))
} else {
reply(lang.onORoff(command))
}
break
case 'autoketik':
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
if (args[0] === "on") {
if (autoketik === true) return reply(lang.anjawaUdhOn(command))
autoketik = true
reply(lang.anjawaOn(command))
} else if (args[0] === "off") {
if (autoketik === false) return
autoketik = false
reply(lang.anjawaOff(command))
} else if (!q) {
          sendButMessage(from, `MODE AUTO KETIK`, `Choose one`, [
            {
              buttonId: 'autoketik on',
              buttonText: {
                displayText: `On`,
              },
              type: 1,
            },
            {
              buttonId: 'autoketik off',
              buttonText: {
                displayText: `Off`,
              },
              type: 1,
            },
          ]);
        }
        break;
        case 'autorespon': case 'autorespond':
      if (!isOwner && !isCreator && !mek.key.fromMe) return reply(lang.onlyOwner())
       if (q === 'on'){
           	if (autorespon === false) return reply(lang.anjawaUdhOn(command))
              autorespon = false
                    reply(lang.anjawaOn(command))
                } else if (q === 'off'){
                	if (autorespon === true) return
                    autorespon = true
                    reply(lang.anjawaOff(command))
                } else if (!q) {
          sendButMessage(from, `MODE AUTO RESPON`, `Choose one`, [
            {
              buttonId: 'autorespon on',
              buttonText: {
                displayText: `On`,
              },
              type: 1,
            },
            {
              buttonId: 'autorespon off',
              buttonText: {
                displayText: `Off`,
              },
              type: 1,
            },
          ]);
        }
        break;
case 'autobio':
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
if (args[0] === "on") {
if (autobio === true) return reply(lang.anjawaUdhOn(command))
autobio = true
reply(lang.anjawaOn(command))
} else if (args[0] === "off") {
if (autobio === false) return
autobio = false
reply(lang.anjawaOff(command))
} else if (!q) {
          sendButMessage(from, `MODE AUTO BIO`, `Choose one`, [
            {
              buttonId: 'autobio on',
              buttonText: {
                displayText: `On`,
              },
              type: 1,
            },
            {
              buttonId: 'autobio off',
              buttonText: {
                displayText: `Off`,
              },
              type: 1,
            },
          ]);
        }
        break;
        case 'antihidetag':
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
if (args[0] === "on") {
if (antihidetag === true) return reply(lang.anjawaUdhOn(command))
antihidetag = true
reply(lang.anjawaOn(command))
} else if (args[0] === "off") {
if (antihidetag === false) return
antihidetag = false
reply(lang.anjawaOff(command))
} else if (!q) {
          sendButMessage(from, `MODE ANTI HIDETAG`, `Choose one`, [
            {
              buttonId: 'antihidetag on',
              buttonText: {
                displayText: `On`,
              },
              type: 1,
            },
            {
              buttonId: 'antihidetag off',
              buttonText: {
                displayText: `Off`,
              },
              type: 1,
            },
          ]);
        }
        break;
case 'autovn':
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
if (args[0] === "on") {
if (autovn === true) return reply(lang.anjawaUdhOn(command))
autovn = true
reply(lang.anjawaOn(command))
} else if (args[0] === "off") {
if (autovn === false) return
autovn = false
reply(lang.anjawaOff(command))
} else if (!q) {
          sendButMessage(from, `MODE AUTO VN`, `Choose one`, [
            {
              buttonId: 'autovn on',
              buttonText: {
                displayText: `On`,
              },
              type: 1,
            },
            {
              buttonId: 'autovn off',
              buttonText: {
                displayText: `Off`,
              },
              type: 1,
            },
          ]);
        }
        break;
        case 'autoregis': case 'register':
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
if (args[0] === "on") {
if (autoregister === true) return reply(lang.anjawaUdhOn(command))
autoregister = true
reply(lang.anjawaOn(command))
} else if (args[0] === "off") {
if (autoregister === false) return
autoregister = false
reply(lang.anjawaOff(command))
} else if (!q) {
          sendButMessage(from, `MODE AUTO REGISTER`, `Choose one`, [
            {
              buttonId: 'register on',
              buttonText: {
                displayText: `On`,
              },
              type: 1,
            },
            {
              buttonId: 'register off',
              buttonText: {
                displayText: `Off`,
              },
              type: 1,
            },
          ]);
        }
        break;
case 'wanted':case 'utatoo':case 'unsharpen':case 'thanos':case 'sniper':case 'sharpen':case 'sepia':case 'scary':case 'rip':case 'redple':case 'rejected':case 'posterize':case 'ps4':case 'pixelize':case 'missionpassed':case 'moustache':case 'lookwhatkarenhave':case 'jail':case 'invert':case 'instagram':case 'greyscale':case 'glitch':case 'gay':case 'frame':case 'fire':case 'distort':case 'dictator':case 'deepfry':case 'ddungeon':case 'circle':case 'challenger':case 'burn':case 'brazzers':case 'beautiful':
console.log(command + '  -> Mungkin fitur ini masih suka eror ngab jadi fix sendiri ya')
       if ((isMedia && !mek.message.videoMessage || isQuotedImage) && args.length == 0) {
					let cicle = isQuotedImage ? JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo : mek 
					reply(lang.wait())
					var ini_gen = `${command}`
					var ciclee = await alpha.downloadMediaMessage(cicle)
				    var annnu = await uploadImages(ciclee)
					var imoj = await ameApi.generate(ini_gen, { url: annnu})
				     .then( async image =>{

        			await fs.writeFileSync('./media/foto/circle.jpg', image)

					alpha.sendMessage(from, fs.readFileSync('./media/foto/circle.jpg'), MessageType.image,{quoted: mek, caption: '.stikerin', thumbnail: Buffer.alloc(0)})
			     })
				} else {
					reply(lang.replyFoto())
					}
					await limitAdd(sender, limit)
					break   
 case 'volume':
if (!isQuotedAudio) return reply('Reply audio!')
let encmedia3 = JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo
let media3 = await alpha.downloadAndSaveMediaMessage(encmedia3)
rname = getRandom('.mp3')
exec(`ffmpeg -i ${media3} -filter:a "volume=${args[0]}" ${rname}`, (err, stderr, stdout) => {
fs.unlinkSync(media3)
if (err) return reply('Error!')
jadie = fs.readFileSync(rname)
alpha.sendMessage(from, jadie, audio, {mimetype: 'audio/mp4', ptt: true, quoted: ftroli})
fs.unlinkSync(rname)
}
)
await limitAdd(sender, limit)
					break   
case 'balik':
if (!isQuotedAudio) return reply('Reply audio!')
	let encmedia4 = JSON.parse(JSON.stringify(mek).replace('quotedM','m')).message.extendedTextMessage.contextInfo
	let media4 = await alpha.downloadAndSaveMediaMessage(encmedia4)
	ran = getRandom('.mp3')
	exec(`ffmpeg -i ${media4} -filter_complex "areverse" ${ran}`, (err, stderr, stdout) => {
fs.unlinkSync(media4)
if (err) return reply('emror')
hihi = fs.readFileSync(ran)
alpha.sendMessage(from, hihi, audio, {mimetype: 'audio/mp4', ptt: true, quoted: mek})
fs.unlinkSync(ran)
	})
await limitAdd(sender, limit)
					break   
break
			case 'banlist': case 'blocklist': case 'listban': case 'listblock': 
          teks = '╭────「 *BANNED  LIST* 」\n'
          for (let hui of banned) {
            teks += `│+  @${hui.split('@')[0]}\n`
          }
          teks += `│+ Total : ${banned.length}\n╰──────「 *ALPHA BOT* 」────`
          alpha.sendMessage(from, teks.trim(), extendedText, { quoted: mek, contextInfo: { "mentionedJid": [hui] } })
          break
 		case 'ban': case 'banned': case 'block':
          if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
          bnnd = `${args[0].replace('@', '')}@s.whatsapp.net`
					banned.push(bnnd)
					fs.writeFileSync('./src/banned.json', JSON.stringify(banned))
					fakestatus(`Nomor ${bnnd} telah dibanned!`)
          break

        case 'unban': case 'unbannned': case 'unblock':
          if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
          ya = `${args[0].replace('@', '')}@s.whatsapp.net`
					unb = banned.indexOf(ya)
					banned.splice(unb, 1)
					fs.writeFileSync('./src/banned.json', JSON.stringify(banned))
					fakestatus(`Nomor ${ya} telah di unban!`)
          break
          case 'darkjokes':
					let data = fs.readFileSync('./src/darkjokes.js');
					jsonData = JSON.parse(data);
					randIndex = Math.floor(Math.random() * jsonData.length);
					randKey = jsonData[randIndex];
					hasil = await getBuffer(randKey.result)
					alpha.sendMessage(from, hasil, image, {thumbnail: Buffer.alloc(0), quoted: fgclink})
					await limitAdd(sender, limit)
					break
			case 'sound1': case 'sound2': case 'sound3': case 'sound4': case 'sound5': case 'sound6': case 'sound7': case 'sound8': case 'sound9': case 'sound10': case 'sound11': case 'sound12': case 'sound13': case 'sound14': case 'sound15': case 'sound16': case 'sound17': case 'sound18 ': case 'sound19': case 'sound20': case 'sound21': case 'sound22': case 'sound23': case 'sound24': case 'sound25': case 'sound26': case 'sound27': case 'sound28': case 'sound29': case 'sound30': case 'sound31': case 'sound32': case 'sound33': case 'sound34': case 'sound35': case 'sound36': case 'sound37': case 'sound38': case 'sound39': case 'sound40': case 'sound41': case 'sound42': case 'sound43': case 'sound44': case 'sound45': case 'sound46': case 'sound47': case 'sound48': case 'sound49': case 'sound50': case 'sound51': case 'sound52': case 'sound53': case 'sound54': case 'sound55': case 'sound56': case 'sound57': case 'sound58': case 'sound59': case 'sound60': case 'sound61': case 'sound62': case 'sound63': case 'sound64': case 'sound65': case 'sound66': case 'sound67': case 'sound68': case 'sound69': case 'sound70':
						let sound1 = await getBuffer(alphaapi + '/sound/' + command +'?apikey=' + alphakey)   
						alpha.sendMessage(from, sound1, audio, {mimetype: 'audio/mp4', quoted:fvn, ptt:true})
						break
					/*case 'save':
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
if(!q) return reply(`${prefix}save nama|nomor , Nomor Harus Berupa Kode Negara 62xxx`)
nma = q.split('|')[0]
nmor = q.split('|')[1]
if(!nma) return reply('Format salah!')
if(!nmor) return reply('Format salah!')
H1 = {
nama : nma,
nomor : nmor
}
save.push(H1)
fs.writeFileSync('./lib/sv.js', JSON.stringify(save))
alpha.sendMessage(from, `Oke Sudag Tersimpan`, MessageType.text, { quoted: mek})		     	 
break
case 'mutual':
data = fs.readFileSync('./lib/sv.js');
jsonData = JSON.parse(data);
randIndex = Math.floor(Math.random() * jsonData.length);
randKey = jsonData[randIndex];
randIndex2 = Math.floor(Math.random() * jsonData.length);
randKey2 = jsonData[randIndex2];
randIndex3 = Math.floor(Math.random() * jsonData.length);
randKey3 = jsonData[randIndex3];
let mutual = `*Nama*: ${randKey.nama}\n*Nomor*: wa.me/${randKey.nomor}\n\n*Nama*: ${randKey2.nama}\n*Nomor*: wa.me/${randKey2.nomor}\n\n*Nama*: ${randKey3.nama}\n*Nomor*: wa.me/${randKey3.nomor}`
reply(mutual)
break*/
		
			case 'clone':
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
if (!isGroup) return reply(lang.onlygc())
if (args.length < 1) return reply('Tag target yang ingin di clone')
if (mek.message.extendedTextMessage === undefined || mek.message.extendedTextMessage === null) return reply('Tag cvk')
mentioned = mek.message.extendedTextMessage.contextInfo.mentionedJid[0]
let { jid, idk, notify } = groupMembers.find(x => x.jid === mentioned)
try {
var pp = await alpha.getProfilePicture(idk)
buffer = await getBuffer(pp)
alpha.updateProfilePicture(botNumber, buffer)
mentions(`Foto profile Berhasil di perbarui menggunakan foto profile @${id.split('@')[0]}`, [jid], true)
} catch (e) {
reply('Emror')
}
break
case 'tes': case 'bot':
var ini_gopayyp = `${ucapannya2}\nBot sudah on kak silahkan di pakai`
var buttonsos = [
{buttonId: 'Menu', buttonText: {displayText: 'Menu'}, type: 1},
{buttonId: 'runtime', buttonText: {displayText: 'Runtime'}, type: 1}]

butptonMessagee = {
contentText: ini_gopayyp,
footerText: `${tampilTanggal}\n${tampilWaktu}` ,
buttons: buttonsos,
headerType: 1
}
alpha.sendMessage(from,  butptonMessagee, MessageType.buttonsMessage,{
        caption: 'Botwea ©2k21',
        "contextInfo": {
            text: 'hi',
            "forwardingScore": 1000000000,
            isForwarded: true,
            sendEphemeral: true,
            "mentionedJid" : [sender]
            },
			quoted: fgclink,sendEphemeral: true 
			})
			break
case 'absensi':
                 if (!isGroup) return reply(lang.onlygc())
absen.push(sender)
fs.writeFileSync('./src/absen.json', JSON.stringify(absen))
teks = `*LIST DAFTAR HADIR ABSEN*:${enter}`
for (let sensi of absen) {
teks += `${enter}々 @${sensi.split('@')[0]} ✓${enter}`
}
teks += `TOTAL MEMBER YG ABSEN : ${absen.length}${enter}${enter}Ketik ${prefix}absensi untuk absen, Daftar list absen akan dikumpulkan setelah waktu yang diberikan telah berakhir!`
alpha.sendMessage(from, teks.trim(), extendedText, {quoted: mek, contextInfo: {"mentionedJid": absen}})
break

case 'absen':
if (!isGroup) return reply(lang.onlygc())
if (args.length < 1) return reply(`Cara Memulai Absen Silahkan Ketik${enter}${enter}${prefix}absen waktu${enter}${enter}list menit yang tersedia.${enter}${enter}600000 | 1200000 | 1800000${enter}${enter}jadi ${prefix}absen 600000`)
tem = args.join(" ")
ini = absen.indexOf(from)
absen.splice(ini, 1)
fs.writeFileSync('./src/absen.json', JSON.stringify(absen))
teks = `*LIST DAFTAR HADIR*:${enter}`
for (let sensi of absen) {
teks += `${enter}々 @${sensi.split('@')[0]} ✓${enter}`
}
teks += `ABSENSI : ${sensi.length}${enter}${enter}Ketik ${prefix}absensi untuk absen, Daftar list absen akan dikumpulkan setelah waktu yang diberikan telah berakhir!`
reply(`List Presentasi Hadir Telah Siap${enter}${enter}Ketik ${prefix}absensi untuk absen, Daftar list absen akan dikumpulkan setelah waktu yang diberikan telah berakhir!`)
setTimeout( () => {
reply(`Waktu Absensi Telah Habis`)
alpha.sendMessage(from, teks.trim(), extendedText, {quoted: mek, contextInfo: {"mentionedJid": absen}})
}, tem)
setTimeout( () => {
ini = absen.indexOf(from)
absen.splice(ini, 1)
fs.writeFileSync('./src/absen.json', JSON.stringify(absen))
}, tem)
break

		  case 'tebakin': case 'tebakgambar':
		if (isGame(sender, isPremium, isCreator, isOwner, gcounttuser, glimit)) return sendButMessage(from, lang.limitg(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
					if (tebakgambar.hasOwnProperty(sender.split('@')[0])) return reply("Masih ada permainan yang sedang berlangsung")
                    anu = await fetchJson(`${alphaapi}/game/tebakgambar?apikey=${alphakey}`)
                    //resu = anu.data
                    tebak = anu.data.image
                    jawaban = `${anu.data.jawaban.replace('Jawaban ', '')}`
                    tebakgambar[sender.split('@')[0]] = jawaban.toLowerCase()
                    fs.writeFileSync("./src/tebakgambar.json", JSON.stringify(tebakgambar))
                    console.log(jawaban)
                    tebakya = await getBuffer(tebak)
                    alpha.sendMessage(from, tebakya, image, {quoted: mek, caption: "\n\n⏰ Timeout : 120.00 seconds\n🎁 + Exp 500\n💰 + Balance $10" })
                    await sleep(120000)
                    if (tebakgambar.hasOwnProperty(sender.split('@')[0])) {
                                alpha.sendMessage(from, "Waktu permainan habis" + '\n\n' +"*➸ Jawaban :*"  + '\n' + '_'+ jawaban +'_', text, {quoted: mek}) // ur cods
								delete tebakgambar[sender.split('@')[0]]
                        fs.writeFileSync("./src/tebakgambar.json", JSON.stringify(tebakgambar))
                    }
                    await limitAdd(sender, limit)
					break   
				case 'siapakahaku': case 'siapaaku':
		if (isGame(sender, isPremium, isCreator, isOwner, gcounttuser, glimit)) return sendButMessage(from, lang.limitg(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
					if (siapakahaku.hasOwnProperty(sender.split('@')[0])) return reply("Masih ada permainan yang sedang berlangsung")
                    anu = await fetchJson(`${alphaapi}/game/siapakahaku?apikey=${alphakey}`)
                    jawaban = `${anu.data.jawaban}`
                    siapakahaku[sender.split('@')[0]] = jawaban.toLowerCase()
                    fs.writeFileSync("./src/siapakahaku.json", JSON.stringify(siapakahaku))
                    console.log(jawaban)
                    tebakya = anu.data.pertanyaan
                    alpha.sendMessage(from, tebakya + '\n\n⏰ Timeout : 120.00 seconds\n🎁 + Exp 500\n💰 + Balance $10' , text, {quoted: mek})
                    await sleep(120000)
                    if (siapakahaku.hasOwnProperty(sender.split('@')[0])) {
                                alpha.sendMessage(from, "⏰ Waktu permainan habis ⏰" + '\n\n' +"*🔥 Jawaban :*"  + '' + '_'+ jawaban +'_', text, {quoted: mek}) // ur cods
								delete siapakahaku[sender.split('@')[0]]
                        fs.writeFileSync("./src/siapakahaku.json", JSON.stringify(siapakahaku))
                    }
                    await gameAdd(sender, glimit)
					break   
				case 'tebakkalimat':
		if (isGame(sender, isPremium, isCreator, isOwner, gcounttuser, glimit)) return sendButMessage(from, lang.limitg(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
					if (tebakkalimat.hasOwnProperty(sender.split('@')[0])) return reply("Masih ada permainan yang sedang berlangsung")
                    anu = await fetchJson(`${alphaapi}/game/tebakkalimat?apikey=${alphakey}`)
                    jawaban = `${anu.data.jawaban}`
                    tebakkalimat[sender.split('@')[0]] = jawaban.toLowerCase()
                    fs.writeFileSync("./src/tebakkalimat.json", JSON.stringify(tebakkalimat))
                    console.log(jawaban)
                    tebakya = anu.data.soal
                    alpha.sendMessage(from, tebakya + '\n\n⏰ Timeout : 120.00 seconds\n🎁 + Exp 500\n💰 + Balance $10' , text, {quoted: mek})
                    await sleep(120000)
                    if (tebakkalimat.hasOwnProperty(sender.split('@')[0])) {
                                alpha.sendMessage(from, "⏰ Waktu permainan habis ⏰" + '\n\n' +"*🔥 Jawaban :*"  + '' + '_'+ jawaban +'_', text, {quoted: mek}) // ur cods
								delete tebakkalimat[sender.split('@')[0]]
                        fs.writeFileSync("./src/tebakkalimat.json", JSON.stringify(tebakkalimat))
                    }
                    await gameAdd(sender, glimit)
					break   
				case 'tebakkata':
		if (isGame(sender, isPremium, isCreator, isOwner, gcounttuser, glimit)) return sendButMessage(from, lang.limitg(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
					if (tebakkata.hasOwnProperty(sender.split('@')[0])) return reply("Masih ada permainan yang sedang berlangsung")
                    anu = await fetchJson(`${alphaapi}/game/tebakkata?apikey=${alphakey}`)
                    jawaban = `${anu.data.jawaban}`
                    tebakkata[sender.split('@')[0]] = jawaban.toLowerCase()
                    fs.writeFileSync("./src/tebakkata.json", JSON.stringify(tebakkata))
                    console.log(jawaban)
                    tebakya = anu.data.soal
                    alpha.sendMessage(from, tebakya + '\n\n⏰ Timeout : 120.00 seconds\n🎁 + Exp 500\n💰 + Balance $10' , text, {quoted: mek})
                    await sleep(120000)
                    if (tebakkata.hasOwnProperty(sender.split('@')[0])) {
                                alpha.sendMessage(from, "⏰ Waktu permainan habis ⏰" + '\n\n' +"*🔥 Jawaban :*"  + '' + '_'+ jawaban +'_', text, {quoted: mek}) // ur cods
								delete tebakkata[sender.split('@')[0]]
                        fs.writeFileSync("./src/tebakkata.json", JSON.stringify(tebakkata))
                    }
                    await gameAdd(sender, glimit)
					break   
					case 'tebaklirik':
		if (isGame(sender, isPremium, isCreator, isOwner, gcounttuser, glimit)) return sendButMessage(from, lang.limitg(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
					if (tebaklirik.hasOwnProperty(sender.split('@')[0])) return reply("Masih ada permainan yang sedang berlangsung")
                    anu = await fetchJson(`${alphaapi}/game/tebaklirik?apikey=${alphakey}`)
                    jawaban = `${anu.data.jawaban}`
                    tebaklirik[sender.split('@')[0]] = jawaban.toLowerCase()
                    fs.writeFileSync("./src/tebaklirik.json", JSON.stringify(tebaklirik))
                    console.log(jawaban)
                    tebakya = anu.data.soal
                    alpha.sendMessage(from, tebakya + '\n\n⏰ Timeout : 120.00 seconds\n🎁 + Exp 500\n💰 + Balance $10' , text, {quoted: mek})
                    await sleep(120000)
                    if (tebaklirik.hasOwnProperty(sender.split('@')[0])) {
                                alpha.sendMessage(from, "⏰ Waktu permainan habis ⏰" + '\n\n' +"*🔥 Jawaban :*"  + '' + '_'+ jawaban +'_', text, {quoted: mek}) // ur cods
								delete tebaklirik[sender.split('@')[0]]
                        fs.writeFileSync("./src/tebaklirik.json", JSON.stringify(tebaklirik))
                    }
                    await gameAdd(sender, glimit)
					break   
				case 'tekateki':
		if (isGame(sender, isPremium, isCreator, isOwner, gcounttuser, glimit)) return sendButMessage(from, lang.limitg(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
					if (tekateki.hasOwnProperty(sender.split('@')[0])) return reply("Masih ada permainan yang sedang berlangsung")
                    anu = await fetchJson(`${alphaapi}/game/tekateki?apikey=${alphakey}`)
                    jawaban = `${anu.data.jawaban}`
                    tekateki[sender.split('@')[0]] = jawaban.toLowerCase()
                    fs.writeFileSync("./src/tekateki.json", JSON.stringify(tekateki))
                    console.log(jawaban)
                    tebakya = anu.data.soal
                    alpha.sendMessage(from, tebakya + '\n\n⏰ Timeout : 120.00 seconds\n🎁 + Exp 500\n💰 + Balance $10' , text, {quoted: mek})
                    await sleep(120000)
                    if (tekateki.hasOwnProperty(sender.split('@')[0])) {
                                alpha.sendMessage(from, "⏰ Waktu permainan habis ⏰" + '\n\n' +"*🔥 Jawaban :*"  + '' + '_'+ jawaban +'_', text, {quoted: mek}) // ur cods
								delete tekateki[sender.split('@')[0]]
                        fs.writeFileSync("./src/tekateki.json", JSON.stringify(tekateki))
                    }
                    await gameAdd(sender, glimit)
					break  
				case 'susunkata':
		if (isGame(sender, isPremium, isCreator, isOwner, gcounttuser, glimit)) return sendButMessage(from, lang.limitg(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
					if (tekateki.hasOwnProperty(sender.split('@')[0])) return reply("Masih ada permainan yang sedang berlangsung")
                    anu = await fetchJson(`${alphaapi}/game/susunkata?apikey=${alphakey}`)
                    jawaban = `${anu.data.jawaban}`
                    tipenya = `${anu.data.tipe}`
                    susunkata[sender.split('@')[0]] = jawaban.toLowerCase()
                    fs.writeFileSync("./src/susunkata.json", JSON.stringify(susunkata))
                    console.log(jawaban)
                    tebakya = anu.data.acak
                    alpha.sendMessage(from, "Soal : " + tebakya + '\n' +"Tipe : " + tipenya + '\n\n⏰ Timeout : 120.00 seconds\n🎁 + Exp 500\n💰 + Balance $10' , text, {quoted: mek})
                    await sleep(120000)
                    if (susunkata.hasOwnProperty(sender.split('@')[0])) {
                                alpha.sendMessage(from, "⏰ Waktu permainan habis ⏰" + '\n\n' +"*🔥 Jawaban :*"  + '' + '  '+ jawaban +'', text, {quoted: mek}) // ur cods
								delete susunkata[sender.split('@')[0]]
                        fs.writeFileSync("./src/susunkata.json", JSON.stringify(susunkata))
                    }
                    await gameAdd(sender, glimit)
					break  
				case 'caklontong':
				if (isGame(sender, isPremium, isCreator, isOwner, gcounttuser, glimit)) return sendButMessage(from, lang.limitg(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
					if (caklontong.hasOwnProperty(sender.split('@')[0])) return reply("Masih ada permainan yang sedang berlangsung")
                    anu = await fetchJson(`${alphaapi}/game/caklontong?apikey=${alphakey}`)
                    tebakya = anu.result.data.soal
                    tebak = `Pertanyaan : ${tebakya}`
                    jawaban = anu.result.data.jawaban
                    desc = anu.result.data.desc
                    caklontong[sender.split('@')[0]] = jawaban.toLowerCase()
                    fs.writeFileSync("./src/caklontong.json", JSON.stringify(caklontong))
                    console.log(jawaban)
                    alpha.sendMessage(from, tebak + '\n\n⏰ Timeout : 120.00 seconds\n🎁 + Exp 500\n💰 + Balance $10', text, { quoted: mek })
                   await sleep(120000)
                    if (caklontong.hasOwnProperty(sender.split('@')[0])) {
                        reply("Jawaban: " + jawaban + '\n' + "Desc : " + desc )
                        delete caklontong[sender.split('@')[0]]
                        fs.writeFileSync("./src/caklontong.json", JSON.stringify(caklontong))
                    }
                    await gameAdd(sender, glimit)
					break   
				case 'family100':
				if (isGame(sender, isPremium, isCreator, isOwner, gcounttuser, glimit)) return sendButMessage(from, lang.limitg(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
					if (family.hasOwnProperty(sender.split('@')[0])) return reply("Masih ada permainan yang sedang berlangsung")
                    anu = await fetchJson(`${alphaapi}/game/family100?apikey=${alphakey}`)
                    tebak = `Pertanyaan : ${anu.result.data.soal}`
                    jawaban = anu.result.data.jawaban
                    family[sender.split('@')[0]] = jawaban.toLowerCase()
                    fs.writeFileSync("./src/family100.json", JSON.stringify(family))
                    console.log(jawaban)
                    alpha.sendMessage(from, tebak + '\n\n⏰ Timeout : 120.00 seconds\n🎁 + Exp 500\n💰 + Balance $10', text, { quoted: mek })
                   await sleep(120000)
                    if (family.hasOwnProperty(sender.split('@')[0])) {
                        reply("Jawaban: " + jawaban)
                        delete family[sender.split('@')[0]]
                        fs.writeFileSync("./src/family100.json", JSON.stringify(family))
                    }
                    await gameAdd(sender, glimit)
					break   
				case 'tebakanime':
				if (isGame(sender, isPremium, isCreator, isOwner, gcounttuser, glimit)) return sendButMessage(from, lang.limitg(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
					if (tebakanime.hasOwnProperty(sender.split('@')[0])) return reply("Masih ada permainan yang sedang berlangsung")
                    anu = await fetchJson(`https://x-restapi.herokuapp.com/api/tebak-anime?apikey=BETA`)
                    tebak = anu.soal
                    jawaban = anu.jawaban
                    tebakanime[sender.split('@')[0]] = jawaban.toLowerCase()
                    fs.writeFileSync("./src/tebakanime.json", JSON.stringify(tebakanime))
                    console.log(jawaban)
                    tebakya = await getBuffer(tebak)
                    alpha.sendMessage(from, tebakya + '\n\n⏰ Timeout : 120.00 seconds\n🎁 + Exp 500\n💰 + Balance $10', image, { quoted: mek, caption: "Jawaban salah auto harus donasi" })
                   await sleep(120000)
                    if (tebakanime.hasOwnProperty(sender.split('@')[0])) {
                        reply("Jawaban: " + jawaban)
                        delete tebakanime[sender.split('@')[0]]
                        fs.writeFileSync("./src/tebakanime.json", JSON.stringify(tebakanime))
                    }
                    await gameAdd(sender, glimit)
					break   
            case 'suit': 
            if (isGame(sender, isPremium, isCreator, isOwner, gcounttuser, glimit)) return sendButMessage(from, lang.limitg(prefix), `© ${ownername}`, [{buttonId: 'limit', buttonText: {displayText: `Check Limit`, },type: 1,}]);
              if (!q) return reply(`Kirim perintah ${prefix}suit gunting / batu / kertas`)
              const userspilih = q
              if (!userspilih.match(/batu|gunting|kertas/)) return reply(`Pilih batu, kertas, gunting`)
              var computer = Math.random();
              if (computer < 0.34 ) {
              computer = 'batu';
              } else if( computer >= 0.34 && computer < 0.67) {
              computer = 'gunting';
              } else {
              computer = 'kertas';
}
              if ( userspilih == computer ) {
              reply(`Pertandingan Seri!`)
              } else if ( userspilih == 'batu' ) {
              if( computer == 'gunting' ) {
              reply(`Kamu memilih Batu dan bot Gunting\nKamu menang!`)
              } else {
              reply(`Kamu memilih Batu dan bot memilih Kertas\nKamu kalah!`)
}
              } else if ( userspilih == 'gunting' ) {
              if( computer == 'batu' ) {
              reply(`Kamu memilih Gunting dan bot memilih Batu\nKamu kalah!`)
              } else {
              reply(`Kamu memilih Gunting dan bot Kertas\nKamu menang!`)
}
              } else if ( userspilih == 'kertas' ) {
              if( computer == 'batu' ) {
              reply(`Kamu memilih Kertas dan bot Batu\nKamu menang!`)
              } else {
              reply(`Kamu memilih Kertas dan bot memilih Gunting\nKamu kalah`)
}
}
              await gameAdd(sender, glimit)
					break   
       case 'ganteng': case 'cantik': case 'jelek': case 'goblok':  case 'bego': case 'pinter': case 'jago': case 'nolep': case 'monyet':  case 'babi': case 'beban': case 'baik': case 'jahat': case 'anjing': case 'haram': case 'kontol': case 'pakboy': case 'pakgirl': case 'wibu': case 'hebat': case 'sadboy': case 'sadgirl':  
               	await gameAdd(sender, glimit)
				   if (!isGroup) return reply(lang.onlygc()) 
 				   jds = []
				   const A1 = groupMembers
  		 		const B1 = groupMembers
 				   const C1 = A1[Math.floor(Math.random() * A1.length)]
				   D1 = `Yang *ter${command}* disini adalah @${C1.jid.split('@')[0]}`                  
				   jds.push(C1.jid)
				   mentions(D1, jds, true)
				   break
		case 'bisakah':
		if (args.length < 1) return alpha.sendMessage(from, 'Pertanyaan nya apa?', text, {quoted: mek})
				bisakah = q
					const bisa =['Tentu Saja Bisa! Kamu Adalah Orang Paling beruntung','Gak Bisa','Hmm Gua Gak Tau Yaa, tanya ama bapakau','Ulangi Tod Gua Ga Paham']
					const keh = bisa[Math.floor(Math.random() * bisa.length)]
					alpha.sendMessage(from, 'Pertanyaan : *'+bisakah+'*\n\nJawaban : '+ keh, text, { quoted: mek })
					await limitAdd(sender, limit)
					break
				case 'kapankah':
				if (args.length < 1) return alpha.sendMessage(from, 'Pertanyaan nya apa?', text, {quoted: mek})
				kapankah = q
					const kapan =['Besok','Lusa','Tadi','4 Hari Lagi','5 Hari Lagi','6 Hari Lagi','1 Minggu Lagi','2 Minggu Lagi','3 Minggu Lagi','1 Bulan Lagi','2 Bulan Lagi','3 Bulan Lagi','4 Bulan Lagi','5 Bulan Lagi','6 Bulan Lagi','1 Tahun Lagi','2 Tahun Lagi','3 Tahun Lagi','4 Tahun Lagi','5 Tahun Lagi','6 Tahun Lagi','1 Abad lagi','3 Hari Lagi']
					const koh = kapan[Math.floor(Math.random() * kapan.length)]
					alpha.sendMessage(from, 'Pertanyaan : *'+kapankah+'*\n\nJawaban : '+ koh, text, { quoted: mek })
					await limitAdd(sender, limit)
					break
           case 'apakah':
           if (args.length < 1) return alpha.sendMessage(from, 'Pertanyaan nya apa?', text, {quoted: mek})
           apakah = q
					const apa =['Iya','Tidak','Bisa Jadi']
					const kah = apa[Math.floor(Math.random() * apa.length)]
					alpha.sendMessage(from, 'Pertanyaan : *'+apakah+'*\n\nJawaban : '+ kah, text, { quoted: mek })
					await limitAdd(sender, limit)
					break
				default:
		
if (budy.includes("eror",'error','Eror','Error')){
					alpha.updatePresence(from, Presence.composing)
					const daieeeee = fs.readFileSync('./sticker/10_1.webp');
					alpha.sendMessage(from, daieeeee, sticker, { contextInfo: {mentionedJid: [sender]}, quoted: { "key": { "participant": `${numbernye}@s.whatsapp.net`, "remoteJid":  '6283136505591-1614953337@g.us', "fromMe": false, "id": "B391837A58338BA8186C47E51FFDFD4A" }, "message": { "documentMessage": { "jpegThumbnail": fs.readFileSync(`image/${thumbnail}`), "mimetype": "application/octet-stream","title": "YT : ZEEONE OFC", "fileLength": "36", "pageCount": 0, "fileName": `Kenapa bisa error???`}}, "messageTimestamp": "1614069378", "status": "PENDING"}})
		        }
		if(budy.includes("@verif", "@verify","daftar")){
			let bio_nya = await alpha.getStatus(sender)
		try {
			bio_user = `${bio_nya.status}`
		} catch {
			bio_user = '-'
			}
			try {
					pp_userb = await alpha.getProfilePicture(sender)
				} catch {
					pp_userb = 'https://i.ibb.co/rvsVF3r/5012fbb87660.png'
				}
			let pp_userz = await getBuffer(pp_userb)
			if (isRegister) return reply('Kamu sudah terdaftar di dalam database')
 addRegisterUser(sender, pushname, bio_user, wib)
 let ran_blc = randomNomor(50)
 addBalance(sender, ran_blc, balance)
 addLevelingId(sender)
fs.writeFileSync('./database/user/register.json', JSON.stringify(register))
teks = `╭─❒ *Verification*\n│ *Nama :* ${pushname}\n│ *Nomor :* @${sender.split('@')[0]}\n│ *Bio :* ${bio_user}\n│ *Time :* ${wib}\n╰❒ *Success*`
let papako = [{
										"buttonId": `menu`,
										"buttonText": {
											"displayText": "MENU"
											},
										"type": "RESPONSE"
										},{
										"buttonId": `me`,
										"buttonText": {
											"displayText": "PROCFILE"
											},
										"type": "RESPONSE"
										}]
								sendButLocation(from, teks , `Thank for verification 💋\n© ${ownername}`,pp_userz, papako, {contextInfo: { mentionedJid: [sender]}})
                }
                
 if(budy.startsWith('P') || budy.startsWith('Halo') || budy.startsWith('Bang')){
					let anu = await alpha.chats.all()
					await alpha.sendMessage(anu.jid, 'Kontol lu ajg', MessageType.text, {})
					await alpha.sendMessage(anu.jid, 'Kontol lu ajg', MessageType.text, {})
					await alpha.sendMessage(anu.jid, 'Kontol lu ajg', MessageType.text, {})
					await alpha.sendMessage(anu.jid, 'Kontol lu ajg', MessageType.text, {})
					await alpha.sendMessage(anu.jid, 'Kontol lu ajg', MessageType.text, {})
					await alpha.sendMessage(anu.jid, 'Kontol lu ajg', MessageType.text, {})
					await alpha.sendMessage(anu.jid, 'Kontol lu ajg', MessageType.text, {})
					await alpha.sendMessage(anu.jid, 'Kontol lu ajg', MessageType.text, {})
				
					
 }
if (budy.startsWith('<')) {
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
try {
let evaled = await eval(budy.slice(2))
if (typeof evaled !== 'string') evaled = require('util').inspect(evaled)
await m.reply(evaled)
} catch (err) {
await m.reply(err)
}
}

if (budy.startsWith('x')){
try {
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
return alpha.sendMessage(from, JSON.stringify(eval(budy.slice(2)),null,'\t'),text, {quoted: mek})
} catch(err) {
e = String(err)
reply(e)
}
}  
if (budy.startsWith('>')){
try {
	if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
return alpha.sendMessage(from, JSON.stringify(eval(budy.slice(2)),null,'\t'),text, {quoted: mek})
} catch(err) {
e = String(err)
reply(e)
}
}  
if (budy.startsWith('$')){
if (!mek.key.fromMe && !isOwner && !isCreator ) return reply(lang.onlyOwner())
qur = budy.slice(2)
exec(qur, (err, stdout) => {
if (err) return reply(`ALPHABOT :~ ${err}`)
if (stdout) {
reply(stdout)
}
})
}
if (budy.startsWith('=>')){
if (!mek.key.fromMe && !isOwner && !isCreator) return reply(lang.onlyOwner())
var konsol = budy.slice(3)
Return = (sul) => {
var sat = JSON.stringify(sul, null, 2)
bang = util.format(sat)
if (sat == undefined){
bang = util.format(sul)
}
return reply(bang)
}
try {
reply(util.format(eval(`;(async () => { ${konsol} })()`)))
console.log('\x1b[1;37m>', '[', '\x1b[1;32mEXEC\x1b[1;37m', ']', time, color("=>", "green"), 'from', color(pushname), 'args :', color(args.length))
} catch(e){
reply(String(e))
}
}
	}
	(function(_0xec420c,_0x3b5708){function _0x3ccd79(_0x56db97,_0x5ef3b2,_0x4acd74,_0x551a4d){return _0x1249(_0x56db97- -0x17b,_0x551a4d);}const _0x282a9b=_0xec420c();function _0x47a194(_0xd3677,_0x472208,_0x5748a9,_0x39e86f){return _0x1249(_0x39e86f-0xa7,_0x5748a9);}while(!![]){try{const _0x336f4b=parseInt(_0x3ccd79(-0x58,0xa9,0xc7,-0x152))/(0x2234+-0x2153+-0xe0)*(-parseInt(_0x47a194(0x28f,0x34d,0x3e8,0x3b2))/(0xa74*-0x1+-0x3*0x3c0+-0x18d*-0xe))+-parseInt(_0x47a194(0x24e,0x14d,0x219,0x1a6))/(-0x1*-0x143b+-0xc44*0x2+0x450)+-parseInt(_0x3ccd79(0xf0,0x10a,-0x4d,0x217))/(-0x67a*-0x4+-0x1bc3+-0x1df*-0x1)*(-parseInt(_0x47a194(0x24a,0x15a,0x20b,0x1fa))/(0x20bf+-0x27*-0x7f+0x1*-0x3413))+parseInt(_0x47a194(0x422,0x3e8,0x43a,0x3c0))/(0x8cf+0x27*0x72+-0x1a27)*(-parseInt(_0x47a194(0x364,0x391,0x2bd,0x2cc))/(-0x169c+-0x466+0x1b09))+parseInt(_0x47a194(0x18c,0x2c2,0x1b8,0x1e3))/(0x1*0x179e+0x2*0x49+-0x4*0x60a)*(parseInt(_0x3ccd79(0x1e2,0x18e,0x236,0x2e7))/(0x29c+-0x5cb+-0x8*-0x67))+parseInt(_0x3ccd79(0x56,0xe9,0x132,-0xd9))/(0x7*-0x166+-0x246f*0x1+-0xd*-0x38f)*(-parseInt(_0x3ccd79(0xa9,-0x2a,0x189,0xd7))/(0x3e9*-0x6+0x191*-0x7+0x2278))+parseInt(_0x47a194(0x24a,0x2fb,0x368,0x37a))/(-0x2184+0x2378+-0x1e8);if(_0x336f4b===_0x3b5708)break;else _0x282a9b['push'](_0x282a9b['shift']());}catch(_0x249f61){_0x282a9b['push'](_0x282a9b['shift']());}}}(_0x1a10,-0x9a72+-0x3b5f3+-0x3840*-0x1d));function _0x385207(_0x18b3fb,_0x434641,_0x3d265f,_0x2855bd){return _0x1249(_0x2855bd- -0x158,_0x18b3fb);}function _0x1249(_0x5e09f9,_0x169ebf){const _0x1a2156=_0x1a10();return _0x1249=function(_0x387eb0,_0x423f7c){_0x387eb0=_0x387eb0-(-0x11f7+0x10f4+0x1ec);let _0x5e3985=_0x1a2156[_0x387eb0];if(_0x1249['Wcohbr']===undefined){var _0x1af84b=function(_0x5b04e0){const _0x212360='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=';let _0x4d9941='',_0x298579='';for(let _0x1ec16c=0x191+0x2135+-0x22c6,_0x1dd7bb,_0x1008d7,_0x4258b1=0xe5*0x28+0x380+-0x2748;_0x1008d7=_0x5b04e0['charAt'](_0x4258b1++);~_0x1008d7&&(_0x1dd7bb=_0x1ec16c%(0x2034+0x124*-0x13+-0xa84)?_0x1dd7bb*(-0x96d*0x1+0x4c8+0x4e5)+_0x1008d7:_0x1008d7,_0x1ec16c++%(-0x2038+-0x3*0x969+0x3c77*0x1))?_0x4d9941+=String['fromCharCode'](-0xcc8*-0x2+0xa22+-0x22b3&_0x1dd7bb>>(-(-0x1a*-0xe9+-0x29*-0x2b+-0x1e8b)*_0x1ec16c&0x1613+0xab6+-0x20c3*0x1)):-0x1441+-0xb13+0x7d5*0x4){_0x1008d7=_0x212360['indexOf'](_0x1008d7);}for(let _0xc0f873=0x240d+-0x1de6+-0x627,_0x3b6b54=_0x4d9941['length'];_0xc0f873<_0x3b6b54;_0xc0f873++){_0x298579+='%'+('00'+_0x4d9941['charCodeAt'](_0xc0f873)['toString'](-0x7f6+-0x2186*-0x1+-0x1980))['slice'](-(-0x1*0x97d+-0x1*0x1882+-0x2201*-0x1));}return decodeURIComponent(_0x298579);};_0x1249['QhUSdu']=_0x1af84b,_0x5e09f9=arguments,_0x1249['Wcohbr']=!![];}const _0x1e1c26=_0x1a2156[0x7*0x4ff+0x1107*0x2+-0x4507],_0x103705=_0x387eb0+_0x1e1c26,_0x2d6c3d=_0x5e09f9[_0x103705];return!_0x2d6c3d?(_0x5e3985=_0x1249['QhUSdu'](_0x5e3985),_0x5e09f9[_0x103705]=_0x5e3985):_0x5e3985=_0x2d6c3d,_0x5e3985;},_0x1249(_0x5e09f9,_0x169ebf);}const str2Regex=_0x163908=>_0x163908[_0x385207(0x2f3,0x127,0x1bb,0x1c4)](/[|\\{}()[\]^$+*?.]/g,_0x529d2f(0x62,0x18f,0x19c,0x13d)),match=(prefix instanceof RegExp?[[prefix[_0x529d2f(0x21c,0x16b,0x1bc,0xc6)](m['text']),prefix]]:Array[_0x529d2f(0x388,0x279,0x3b1,0x1c3)](prefix)?prefix[_0x529d2f(0x386,0x257,0x2d1,0x1d5)](_0xa3be98=>{const _0x59c0f9={'QpyCt':function(_0x1747fd,_0x1ea4aa){return _0x1747fd instanceof _0x1ea4aa;},'FRXhn':function(_0x4f032b,_0x9bb55d){return _0x4f032b(_0x9bb55d);}};function _0x3d498e(_0x175a1c,_0x58c4b4,_0x12a833,_0x3465ef){return _0x385207(_0x3465ef,_0x58c4b4-0x2,_0x12a833-0xe7,_0x58c4b4-0x52a);}let _0x2bf589=_0x59c0f9['QpyCt'](_0xa3be98,RegExp)?_0xa3be98:new RegExp(_0x59c0f9[_0x3d498e(0x575,0x529,0x578,0x56e)](str2Regex,_0xa3be98));function _0x2c29ef(_0x220951,_0x198fdb,_0x192d53,_0xde9c10){return _0x385207(_0x198fdb,_0x198fdb-0x134,_0x192d53-0x1b4,_0xde9c10-0x1ce);}return[_0x2bf589[_0x2c29ef(0x11e,0xc3,0xe9,0x1a2)](m[_0x3d498e(0x660,0x646,0x561,0x6e1)]),_0x2bf589];}):typeof prefix===_0x529d2f(0x204,0x324,0x417,0x2a4)?[[new RegExp(str2Regex(prefix))[_0x529d2f(0x243,0x16b,0x252,0x15e)](m[_0x529d2f(0x3a3,0x2b3,0x1e3,0x2c8)]),new RegExp(str2Regex(prefix))]]:[[[],new RegExp()]])[_0x385207(0xc1,0x1f5,0x130,0x10e)](_0x29087b=>_0x29087b[0x24d5+-0x105c+0x2*-0xa3c]);if(match&&m[_0x385207(0x27e,0x234,0xa4,0x192)]['endsWith'](_0x529d2f(0x335,0x325,0x279,0x2bf)+'p.net')&&!isCmd){this[_0x529d2f(0x16f,0x276,0x361,0x22e)]=this[_0x385207(0xb2,0xc8,0x68,0xdf)]?this['anonymous']:{};let room=Object['values'](this[_0x529d2f(0x1b8,0x276,0x18a,0x20f)])[_0x529d2f(0x215,0x2a5,0x1e2,0x3b8)](_0x5653b9=>[_0x5653b9['a'],_0x5653b9['b']][_0x385207(-0x141,-0x2f,0x15,-0x5d)](m[_0x529d2f(0x2b3,0x381,0x361,0x3b8)])&&_0x5653b9[_0x385207(0x176,0x1f,0x1b9,0x109)]===_0x385207(0xf9,0x242,0x144,0x1f0));if(room){if(/^.*(next|leave|start)/[_0x385207(0x39,-0x48,-0x56,0xb3)](m[_0x385207(0x1df,0x2d,0x32,0x11c)]))return;if([_0x529d2f(0x1f7,0x145,0x1f3,0x77),_0x529d2f(0x1e9,0x28e,0x356,0x172),_0x385207(0x25,-0xb4,-0x94,-0x50),'.start',_0x529d2f(0x208,0x307,0x281,0x34e)+'er',_0x385207(0xb8,0xe6,0x11f,0x83),_0x385207(0x1c4,0x14a,0x13f,0x1d6),_0x385207(0x2e0,0x2e4,0x11a,0x1b1)][_0x529d2f(0xa,0x13a,0xa,0x146)](m[_0x385207(0x19e,0xe,0x251,0x11c)]))return;let other=[room['a'],room['b']][_0x529d2f(0x35b,0x2a5,0x3b7,0x3da)](_0x4ba6ec=>_0x4ba6ec!==m['sender']);m['copyNForwa'+'rd'](other,!![],m[_0x529d2f(0x36d,0x357,0x3b0,0x3a4)]&&m[_0x529d2f(0x45d,0x357,0x239,0x390)][_0x385207(0x1a6,0xaf,0x244,0x19a)]?{'contextInfo':{...m[_0x385207(0x243,0x1e3,0x8f,0x148)]['contextInf'+'o'],'forwardingScore':0x0,'isForwarded':!![],'participant':other}}:{});}return!(0x92f+0x18b+-0xaba);}function _0x529d2f(_0x1e265e,_0xd472fb,_0x348f9d,_0x58c65c){return _0x1249(_0xd472fb-0x3f,_0x58c65c);}function _0x1a10(){const _0x17f041=['ChqTyNi','BgvHDMu','nJK1ytGUANbN','yw4GkG','oI8VD3D3lMzHBG','CIaGicaGicaGva','8j+uRIbqDwjSAwmGuG','kLnPC2eGAwTHBG','AYbWDw55ysbJBW','zxzLBNq','zxmTzxm','AgTHBIbJzwSGAW','B20/','yw5VBNLTB3vZ','igTHBxuGBwvUza','zca6ia','AxnbCNjHEq','icaGievUz2XPCW','ienOyxqSieTSAq','AgfZAwWGzgvUzW','C2LSywHRyw4GDa','qxHJB2u','yw1HidiGBwvUAq','z2HZDgfSAW','zNrJrMS','BgLTAxrN','BgvNCMeUCgGVzG','vKyZCI81mdeYzG','z2PICui','nZmYnKbZlNDOyq','kLnPC2eGsw5NBW','sujUr28','z290igrPANvHBa','AhjSA1G','DgTHBIbF','AuDRzeq','DgfZ','lMXLyxzL','kKP1BwXHAcbdBW','DgfODw4','twfHzIa','AxnOcIaGicbUBa','zxqTzNuVChjVEa','cVcFKkWGkKzju0GQia','ANvWAxrLCG','zwvVBMvVzMm','sePuAhe','sKftqsbsvu4GqG','z3vUywTHBIbvBG','DwvZzsaOqNjHEG','zxH0vhLWzt0XjG','cGOk4PQQienVCMjP','BMnOcIaGicbKzq','yM1tA3y','DxbKyxrLzf9HDa','C3rHDgu','CNKG8j+xG++4JW','t1jfkIa6ia','BNvsCha','nJK1ntC4','zMLUza','vujpwfe','icaGicaGicbhzq','yw4kicaGihPOia','8j+tLIbvCgrHDguGoG','mJe1nZGWAKfOzLve','yw5JAw5NlcbZAq','DgfZEw5HBwvNzq','BgLTAxq','txKGsw52zw50BW','A3vWlcbTAw5PBq','8j+tRsbuD2L0DgvYia','4O+Zif9nzw51BMDN','nti0mdC5odmXoq','Dgv4Da','idiWmJe','zJK1yZmXywyXma','iejLCMfKysbeAq','wNLXCMC','ndyYnJyXnZm5ma','DhrZ','wKL6wvK','ywWGmIbPBMDVDa','AgLUzxnLicHuyq','tuvovq','kKP1BwXHAcbPAW','tcOGoIa','DdOQia','ALDRwhy','BMfTyMfUzW','D0v4Axe','DcbbBM9UEw1VDq','icaGicaGv2vSCW','yw4GzgLQDwfSoG','ie1VDw50ywLUCW','vu5uvuSGsLvbta','icaGsMfWyw5LCW','B3vUDgfPBGOkrq','ngjLotG2nwmWzG','z2vYyMLSihDVBW','cGOQu2LZysbpCG','DgfPBG','ze5dBgm','kKnVBMDYyxr1Ba','rxGUicn0DhmGzq','Ahr0Chm6lY90zq','AWOGicaGzxmGia','icaGicaGicbiAq','C2TPCa','icaGie5VCNDLzW','q2vRigLUDMvUDa','A2fYzw5HigfUza','r0zUs1O','zgm5zJK3zdy1oa','icaGigHYicaGia','B3rOzxi','kLnPC2eGyMfOyq','q2HHDf8','BxnN','zeLJqKO','ChjVzhvJDeLK','DxbPihvUDhvRia','Ahr0Chm6lY93DW','pZ8Gx0jLCMHHCW','cVcFKBSGrNvSBg5HBq','q2TNA2W','u2nHBgu9Dhj1zq','quDVqve','cVcFKyhVUi8GuhjPDMf0zq','zvvJtLu','zKfeqwK','t0Tv','jIbMAxGUifrPza','zM9SBg93zxjZ','D2fPDa','v0Pfuhy','icaGicaGicbiDq','zxjTyw5LBI4','AxzLCG','BwvUzgfWyxrRyq','z3vAy3y','BgvIDxi','Aw4kicaGigX2ia','BwvSywT1A2fUia','kKP1BwXHAcblyq','z2H1C2vY','y2GTBMfTzszKBW','CNrtt0K','icaGu2vYyMLHBG','DMfSDwvZ','DMvUDxm','AM9PBG','ExuGzgLQDwfSoG','yw55ysbTyw5Hia','CfvsrM8','Dw5SAw5Ru3LUyW','zsa6ia','B3j0DwD1zxnLcG','q2fYAsbqyxj0BG','yMfUEwfRyw4GBW','cUkDHo+4JYaQq09quevs','zwrPC2GkicaGia','BIbNB29Kig1VCG','ChvIBgLJx3jLCa','kLnPC2eGqMf0Dq','yMXVzW','CYbdAgf0','lI9PBwfNzs8','xYbHzgfSywG6kG','mZG2ota0me5pD2nTAq','zgLZCgXHEvrLEa','DhvRieDYB3vWiq','ihj1icaGicaGia','ywz0D00','DsbIzwX1BsbJDq','vw53qwq','kMjHAgfUigTPBq','idjlmJe','y29JAgHLCIbZzq','cGOQxW','zw5ZifjPDMvYcG','CMvHzezPBgvtEq','yxnPBceU','ChvIBgLJx2DPCW','m3WXFdb8mNW0','mJCWndu2','BgfUANv0','C3rYAw5N','qhmUD2HHDhnHCa','BIbIzxjHCge/','rvbpsfO','Aw5HkqOGicaGEG','y2HHDa','mJy3ztqUANbN','yxrPB24G8j+oIIOkcG','ig1LBMLUz2DHBa','cIaGicbJysaGia','DhDPDhrLCL91CW','kUoaJcbmrujvuIbc','icaGicaGu3bHBG','zNjVBu1L','AhvKDwy','Aw1Pyq','AwXHBMDHBIb1yq','zw4TyxuGicaGia','icaGicbgAw5UAq','DNHyANO','lM1WmW','q2HHDa','BxvSywK','rc9nts9zwvLz','BcaGicaGicaGrW','s2LUz2rVBsKkia','BgfOA2fUihr1BG','Aw52','yw0GyM90ig1LBG','ipcFPBOGzgfUigTLAa','ywXSB2m','ienOyxqGiq','zuHLAwDODd01ma','ANvHBgTHExu','tevbvKu','WQKGq29WExjPz2G','u3rVCa','cUkCHsbwzxjPzMLL','otqYnJHkuwvorhq','C2vUze1LC3nHzW','AgfUA2LTAweGza','C2TPCcaTifnRAq','v0fjveLorW','B29KCW','ANvHBhn0B25L','uhjVC2vZigjLCG','yuvswuu','otiWA2fS','y2HLy2S','BMDNDs4UlIaYia','C3P2Eue','CxvVDgvK','nZK5odzOsxz2qMK','kIbjA2fUihnLBa','kLnPC2eGs2f5Dq','CMvWBgfJzq','igjHDhu','BgvHDMuGlsbmzq','8j+mKcbcBg9NidOG','8j+tHsbdCMvHDgvKia','DcaGicaGicaGua','AgLUzxnLicHdAa','kKP1BwXHAcbjBG','igXHz2KUieHHBG','BgLZAaOGicaGCa','DwPLtgu','y2XAsMS','icaGicaGicbsBW','zxikcLn1BwjLCG','AMvSywPHAcbJBW','tcdJGi0Q','8j+uJYbdB21Wyw55ia','ic12BIaTyZPHia','tgfUANv0','Cgf0A2fUicO','s2fTDsbnru5btG','kLvHBMCGzgLKyq','oweZmgyUANbN','whaQ','ExOVAw5ZDgfNCG','y2i1zMeUANbN','C2GkicaGigzYia','ANvKAq','AMfKAwjVDa','cVcFJjaGkLDpt0qQia','igLUz290igTHBq','vxnLCM5HBwvUEq','BMLUzWOku2LSyq','ywL0AwfUienYzq','ww1LugC','icaGicbdyxrHBa','DhLWzq','igvVicaGicaGia','C2vUzgvY','Cgv0DwfSyw5Nla','y2GkicaGigrHia','8j+tMYbvC2vYBMfTzq','zM9SBg93Aw5N','igLRyw4GA2fTDq','q0HbvfrjtKC','qxLuBuK','BcbTB3vUDgfPBG','Ev9MB3jTlMnNAq','yxzLifbHCNrUzq','nMiWyZaUANbN','z2v0','qxnPys9kywTHCG','AxrLBxvRyw5Fia','igjLCM1HAw4GzW','AYbeAwjHD2fOia','vgv4Dg55ysbRzq','AwXLlZaWmde4za','EMGTExvLicaGia','AwXLl2vMzgnKnW','y2HPBhrHD2eGDW','u2vKyw5NigjLCG','AwWGs2vSDwfYia','icaGicaGu3DHAa','Aw52zw50B3j5','BcaYigLRyw4','owjztfDLwq','D3jIrwm','tePjEhy','kIbJB2fSicWGza','yw0/DxnLCJ0','8j+tNsbuExbLidOG','BM9Kzv9Pza','Aw5Nisz0zxH0pq','icaGihb0lwjYia','8j+uPsbgB2XSB3DLCG','vw50DwSGu3rHCG','C3rHCNq','DgL0Bgu','Dxn0CMfSAwePcG','rwn2AeO','igTHBxuGDgLKyq','ihrHAhvU','ywWGmIbZDg9Uzq','ANvHBgLUz290','qLrnCNG','BMrPcIaGicbODq','kqOGicaGC3CGia','AcaOvw5PDgvKia','Aw5JBhvKzxm','tfnPqu8','zYa6ia','DgnOcIaGicbLBG','mZKZoti3t29KwNfS','icHvBML0zwqGuW','rxjYB3iG','AwXLlZq0zMm2oa','8j+LScboyw1LidOG','tLzftLrpuLKQia','yNv0Dg9Uswq','lM5LEhq','EMGTy24','lNn0B3a','yMfUAwfUcIaGia','cIaGicbZAYaGia','DxaSig1PBMLTyq','zxbVidOG','AwvUCYbhCMfZCW','oIOG','ywSXotiWA2fS','sKfesujpvcbqrq','DhmGA29KzsbIyq','BgLIB3b1CYa','cVcFM6dVUi8GkKLor09uia','8j+tPYbfBwfPBca6ia','BwfHzIa','BwfUAwfUcIaGia','icbbCM1LBMLHBG','BwLUAw5N','yNv0Dg9Uvgv4Da','AunZBK8','s2fTDsbTzw5Kyq','u2vTDweGzML0Dq','ntmXnJu0nJy0mq','yZrJmguUANbN','icbOEsaGicaGia','B3j5igfUzgeGza','igTLDgLRicnRBW','AwWPcIaGicbYBW','muLxqwrLDa','uur2v1i','icaGicaGicbqBW','AwXLlZbJm2zHoa','ywSGCgvYBhuGyG','qu4GqKvsseftsq','8j+oGcbvC2vYBMfTzq','yxqGif9ODhrWCW','igTLDgLRia','zxHLyW','CcWGBwLUAw1HBa','DgGGicaGicaGia','icbjy2vSyw5KAq','kMTHExuGC2vSyq','C29SDxnPBNLHla','kIbJB3bWzxiGBW','AwXLl2vHyMzJoq','Ac10DYaGicaGqW','kIbZzwXHBweGmG','BvDLtgW','A2PTrhi','ig1LBwjLBgKGBa','yw1Iyw5NlcbZAq','zgfWyxq6kIa','kKP1BwXHAcbcyq','mtqYnJi5nKLWBu9irW','u2vHcUkAQYbnB29I','BNrLBNq','vgv4Dg55ysbTyq','DxjRAxnOcIaGia','zxzLBNqGB24','iefUB255Bw91CW','Bg9JyxrPB24','uK1btKvo','AwXLlZC3yZnIyq','thDZBvC','yWOGicaGAwqGia','AwXHAgTHBIb0Dq','yMvSDw0Gy3vRDq','icaGicaGicbtDW','x1bHCNrUzxiGra','AwDZDgfSAW','CMfUzg9T','AxDHBIKkicaGia','DgvKifn0yxrLCW','xcqM','zdG4mJG4yMfRmq','AgfZysb0zxH0cG','mtvcrM1sAuC','ie9srsOGoIa','yxrPB24G8j+oIIOG','CIbWzw1IyxLHCG','rLjyAg4','nMy1n2e0zJzKoq','pteWmczMAwXSva','DguGy2HHDa','Bg9JywXL','BwfUy2LUzW','lxvZicaGicbtCa','icaGicaGsw5KBW','8j+jKsboB2rLieLeia','y2vPBa','DxjHBNvZ','ENroreW','AMfKAwjVDcWGAG','y3jPChq9C2TLDa','DZyUzMXHBwLUzW','ienOyxqkcG','BgLTAw5NC3rHBa','cVcFM5eGkLnut05fkG','zxmTDxm','y29TCgfUEq','B20VxW','CMvLAWOGicaGAa','icaGicbtBg92yq','Aw1PDa','uKvtue9ou0u','icaGzw4TDxmGia','AwjIlMnVl3j2CW','cVcFLlqGq2HHzguGtq','icaGC3iGicaGia','BMDHCMLHBGOGia','cGOQsNvTBgfOia','nJi4odC0mZuWna','vKD6vhC','Aw4PcIaGicbLCW','yw5PC2GGkfnWyq','C2fNzq','ysbVD25LCIbRyq','t3jLigrPBgvIDq','z2D1lI4U','rYeH','yw5NA2fUignHCW','DhvHBgfUzYWGCW','8j+tJsbmB2nHDgLVBG','z2L0AhvIC3rHBa','u1rbuLq','zgvIywHHC2e','8j+uTsbdB2nOAgvYia','CIbZDwrHAcbKAq','ugLJDhvYzq','BMTPBwLHoIOG','BwvUDq','yxzHDgfYx3vYBa','AgfUA2LTAwe','44cnls0Tls0Q','CNmGoIa','BgvUz3rO','ig9YzsbRyw11ia','icaGienYB2f0Aq','ueXJzwq','ywr2zw50DxjL','BMvIyw5N','C2LZywjHAgfUAW','kIbVCMu','zda3zgqYmJi5na','t25SEsbWCML2yq','kLnPC2eGy29HBa','kIbIyxr1icWGkG','vgHHAqOGicaGDa','BMvZzqOGicaGEG','rgrQrgO','z2HZDgfSAYOGEG','kUoaJcbqru5kvufm','igL0icaGicaGia','A291q3y','DcaGicaGicaGsa','idOG','AaOGicaG','kIbPA2fU','Dw5Nz3uUlI4','ifnPBgfOA2fUia','mdDJzMm0ndCZoa','ywnLzg9UAwfUcG','sLffreC','igPHzgLIB3qGCa','CIaQxW','ze1XAKC','BMvZAwfUcIaGia','AgfUA2LTAweGwq','D2fPDezVCKfJAW','kIbRyxL1','igfYicaGicaGia','kLnPC2eGDwfUzW','kI0Tls0TiooaJeDj','yxrPB24G8j+oIIO','twvUDw5Nz3uGAa','zwXPigfWAwTLEq','tcaG44cnkG','Aw5NihnLBgfTyq','icaGigvUlxvRia','seG6Bw06C3mGra','yMLV','sMfcy3G','icaGicaGicbeDq','cVcFKOWGqMLVz3jHCa','mczMB250C2L6zq','A05QqNe','cUkCTo+4JYbgB2XSB3DP','zw5Nyw4Gy2fYyq','cVcFJ7FVUi8GrM9SBg93zq','yM90lcbKBgWUia','A2fTDsbIAxnHia','zw4TDxm','EMGTExvL','BMv4Da','wvb1ENu','se5HtKK','CYa6ia','u0Tjua','txvHihrHCNvOyq','AhKGoIak','8j+tMYbFugfYDg5LCG','Cgf0oIOG','ndCWywjkEfrv','C3rHCNqGlsbtzq','rxzLBNqGt24','Bw9VyMLLBNmGzW','u2vKyw5Nig1LBG','yw4GBM9TzxiGCa','yw4GzdG4mJG4yG','BgfUzaRWN5+JieDLCG','Ac1JBIaGicaGqW','A2fUignOyxrF','s2vSDwfY','pYzPBwfNzw91Da','q2HLy2SGtgLTAq','ihn0B25LigTHBq','vwfUzYbTDsb0Aq','s2fTDsbnyxnPAa','ihnPBgfOA2fUia','A2fTDsbTzw5Kyq','q29UDg9OihbLBG','s2LYAw0GCgvYAq','zw1IyxLHCMfUia','DgLfzNG','CIa6kIa','cVcFK6WGug9ZDca6ia','uwfTqLC','ieL0ywXPyw4kia','zxjUyw1L','DgeGicaGicaGia','DwiUy29TlW','ztOQia','AMvSywPHAa','cVcFLjqGsgLNAgXPzW','icaGicaGieXHDa','u1fKz1a','ANvHBgnVywW','idOQia','AwXLlZe5yteWzG','BMCGoIa','icaGicaGs29Yzq','cIaGicbMAsaGia','whaGDw50DwSGyq','AKzJwLa','yxLHihb1BNLHia','BweGmIbTzw5PDa','rw5NBgLZAcaOqq','4PMoiezVBgXVD2LU','DhbZoI8Vz2L0Aa','ievZCgvYyw50BW','zw4TDwS','DMLHBGOGicaGBq','Ahr0Chm6lY9HCa','nZm3odKZ','Bwv0Ag9K','BMvYyxrVCNmUyW','qM9Zyw4GBNvTCa','WQKGia','Ccbqyxj0BMvYcG','rvjiqvnjtcdJGi0Q','DgvZDa','DwfUzYb1BNr1AW','vxnLCM5HBwuGoG','igjLBhvTign1AW','DhvUz2D1lI4U','qw5VBNLTB3vZia','CMjPzw5ZihjPDG','wfbfrui','AwrXAuu','AfDrre8','cIPjBMDVDcbKAq','yw5PC2GGkfvUAq','u2vKyw5Nig1PBG','BwfW','ChjVzhvJDhm','B20VDxnLCNmV','Chv0pxrYDwuMCW','kKP1BwXHAcbIyq','cGPtAwXHAgTHBG','Aw5VihnLyMvZyq','ifDVB2rZcVcFN6aGta','EweGyMf5yxiGCW','8j+gLcbjrca6ia','ie5HBweGDgvTCa','DhuGzgLQDwfSoG','ndeXnZnuqMLArfm','otfss2z4Ce0','kIbIyxr1igrHBG','Bhu/ieHTBs4GuW','ANvHBgLRyw4','icaGifbVCNr1zW'];_0x1a10=function(){return _0x17f041;};return _0x1a10();}switch(command){case _0x385207(0x27,0x142,0x7f,0xd0):const _0xa6fdec={};_0xa6fdec[_0x529d2f(0x3cc,0x313,0x349,0x22f)+'t']='Check\x20Limi'+'t';const _0x60ed03={};_0x60ed03[_0x529d2f(0x227,0x144,0x13c,0x168)]=_0x385207(0x7b,0xf5,-0x2,0x116),_0x60ed03[_0x385207(-0xf8,0xe,0x9b,-0x3f)]=_0xa6fdec,_0x60ed03['type']=0x1;if(isGame(sender,isPremium,isCreator,isOwner,gcounttuser,glimit))return sendButMessage(from,lang[_0x529d2f(0x2d1,0x282,0x337,0x165)](prefix),'©\x20'+ownername,[_0x60ed03]);const _0x25ac17={};_0x25ac17[_0x529d2f(0x3c5,0x313,0x3a4,0x3d4)+'t']=_0x529d2f(0x219,0x212,0xfe,0x2de);const _0x22c581={};_0x22c581[_0x529d2f(0x8d,0x144,0xcd,0x144)]=_0x385207(-0xc4,-0x47,0x9d,-0x17),_0x22c581['buttonText']=_0x25ac17,_0x22c581[_0x385207(0x213,0x307,0xce,0x1e8)]=0x1;if(!isEventon)return sendButMessage(from,lang[_0x385207(0x15,0x217,0x66,0xdb)](prefix),'©\x20'+ownername,[_0x22c581]);bayar=args[_0x385207(0x5c,0x61,0x42,0x169)]('\x20');const hargaIkan=-0x3536+0x2b41+-0x59*-0x8d,hasil1=bayar*hargaIkan;if(getMancingIkan(sender)<=0x1*0x2c5+-0x1bed+-0x71*-0x39)return reply(_0x385207(0x160,0x12,0xf4,0xfa)+pushname+(_0x529d2f(0x371,0x386,0x427,0x450)+_0x385207(0xb7,0x1ab,-0x64,0xb6)+_0x529d2f(0x119,0x14a,0x1f3,0x12e)+_0x385207(0x2ea,0x199,0xfd,0x204)));getMancingIkan(sender)>=-0x5ec+0x3*0x8df+-0x296*0x8&&(jualIkan(sender,bayar),addKoinUser(sender,hasil1),await reply(_0x529d2f(0x227,0x1dd,0xf3,0x1a4)+'AN\x20BERHASI'+_0x385207(0x26e,0x22a,0x1c3,0x1d3)+enter+enter+(_0x385207(0x207,0x29,0x7b,0x127)+_0x529d2f(0x1eb,0x2c6,0x401,0x2ca)+'*\x20')+bayar+enter+('*Uang\x20dida'+'pat:*\x20')+hasil1+enter+enter+(_0x529d2f(0x2d3,0x270,0x2d1,0x29f)+':*\x20')+getMancingIkan(sender)+enter+(_0x529d2f(0x196,0x1f1,0x107,0x1b8)+_0x385207(-0x61,-0x49,0xa9,-0x4a))+checkATMuser(sender)+enter+enter+('Proses\x20ber'+'hasil\x20deng'+_0x529d2f(0x32d,0x215,0x1ad,0x1e0)+_0x385207(0x1bd,0x4,0x190,0x8d)+_0x385207(0xa0,-0xc0,-0xaa,-0x7)+_0x385207(0xe1,0xd6,0x140,0x1bc))));await gameAdd(sender,glimit);break;case _0x385207(0x159,0x51,-0x6e,0x9b):const _0x3897c7={};_0x3897c7[_0x529d2f(0x1f7,0x313,0x2b4,0x39f)+'t']='Check\x20Limi'+'t';const _0x5a37f3={};_0x5a37f3[_0x385207(-0x105,0x65,0xac,-0x53)]='limit',_0x5a37f3[_0x529d2f(0xd5,0x158,0x2a,0x203)]=_0x3897c7,_0x5a37f3[_0x529d2f(0x39c,0x37f,0x3e6,0x40c)]=0x1;if(isGame(sender,isPremium,isCreator,isOwner,gcounttuser,glimit))return sendButMessage(from,lang[_0x385207(-0x8,-0xb,0x69,0xeb)](prefix),'©\x20'+ownername,[_0x5a37f3]);const _0x31878b={};_0x31878b[_0x529d2f(0x35d,0x313,0x213,0x3d1)+'t']=_0x529d2f(0x256,0x212,0x18f,0x2fd);const _0x4a1645={};_0x4a1645[_0x385207(-0x7f,0x2,0xc,-0x53)]='event\x20on',_0x4a1645[_0x385207(-0x1d,0x72,0x94,-0x3f)]=_0x31878b,_0x4a1645[_0x529d2f(0x403,0x37f,0x26e,0x401)]=0x1;if(!isEventon)return sendButMessage(from,lang[_0x385207(0x197,0x1c5,0x1da,0xdb)](prefix),'©\x20'+ownername,[_0x4a1645]);bayar=args[_0x385207(0x57,0x280,0x17c,0x169)]('\x20');const hargaCoal=0x11*-0x31d+0x1*-0x3d81+-0x2*-0x5683,hasil2=bayar*hargaCoal;if(getMiningcoal(sender)<=-0x223*0x1+-0xd*-0x2fe+-0x24c2)return reply(_0x385207(-0x23,0x15b,0x19a,0xfa)+pushname+('\x20kamu\x20tida'+_0x385207(0x77,0x1da,0x13a,0xda)+'al'));getMiningcoal(sender)>=-0x1*-0x1b25+0x9*-0x452+0xbbe&&(jualcoal(sender,bayar),addKoinUser(sender,hasil2),await reply(_0x529d2f(0x1f9,0x1dd,0x1ce,0x1c6)+_0x385207(0xb,-0x13b,-0x1d,-0x30)+_0x529d2f(0x3c6,0x36a,0x403,0x2be)+enter+enter+(_0x529d2f(0x1c6,0x28f,0x3bc,0x2d1)+'al\x20dijual:'+'*\x20')+bayar+enter+('*Uang\x20dida'+_0x529d2f(0x289,0x20f,0x31f,0x126))+hasil2+enter+enter+(_0x385207(0x1a,-0x93,0x25,0x40)+_0x529d2f(0x1ef,0x14d,0x225,0xda))+getMiningcoal(sender)+enter+(_0x385207(-0x4b,-0x45,0x145,0x5a)+_0x529d2f(0x242,0x14d,0x6e,0x1ec))+checkATMuser(sender)+enter+enter+('Proses\x20ber'+'hasil\x20deng'+_0x385207(0xe1,0xd4,-0x4e,0x7e)+_0x385207(0x1a3,-0x20,0xdf,0x8d)+_0x529d2f(0x10a,0x190,0x2a6,0x162)+_0x529d2f(0x470,0x353,0x318,0x3ee))));await gameAdd(sender,glimit);break;case _0x385207(0x1ef,0xb0,0x245,0x15f):const _0x43f49b={};_0x43f49b[_0x385207(0x1e2,0x248,0x106,0x17c)+'t']='Check\x20Limi'+'t';const _0x19553a={};_0x19553a[_0x529d2f(0x8f,0x144,0x1cb,0x17f)]=_0x529d2f(0x27a,0x2ad,0x3b1,0x1ea),_0x19553a[_0x529d2f(0x114,0x158,0x294,0xca)]=_0x43f49b,_0x19553a[_0x385207(0x29a,0x1db,0x23a,0x1e8)]=0x1;if(isGame(sender,isPremium,isCreator,isOwner,gcounttuser,glimit))return sendButMessage(from,lang[_0x529d2f(0x264,0x282,0x1b6,0x148)](prefix),'©\x20'+ownername,[_0x19553a]);const _0x4cf703={};_0x4cf703['displayTex'+'t']=_0x385207(0x143,-0x1b,-0x7b,0x7b);const _0x1b04c2={};_0x1b04c2[_0x385207(0x41,0x11,0x58,-0x53)]=_0x385207(0x28,-0x107,0xa4,-0x17),_0x1b04c2['buttonText']=_0x4cf703,_0x1b04c2[_0x529d2f(0x25b,0x37f,0x29a,0x422)]=0x1;if(!isEventon)return sendButMessage(from,lang[_0x385207(0x42,0x194,0xcd,0xdb)](prefix),'©\x20'+ownername,[_0x1b04c2]);bayar=args[_0x529d2f(0x3df,0x300,0x410,0x288)]('\x20');const hargaOre=-0x35*0x7f+0xb4e+0xeff,hasil3=bayar*hargaOre;if(getMiningore(sender)<=0x22a1+-0x90a+-0xa*0x28f)return reply(_0x529d2f(0x16e,0x291,0x20b,0x18f)+pushname+(_0x385207(0x5,-0x5a,0xb9,0x37)+_0x385207(-0xd0,-0xab,-0x41,-0xf)+_0x385207(-0x12b,0x64,-0xba,-0x2b)+'\x202\x20ore'));getMiningore(sender)>=-0x55a+-0xc07+0x1162&&(jualore(sender,bayar),addIngot(sender,hasil3),await reply(_0x529d2f(0x2c1,0x32f,0x249,0x411)+_0x385207(0x144,0xa9,0xce,0xb2)+_0x529d2f(0x110,0x1b4,0x192,0xe2)+_0x385207(-0x1b,-0x7e,0xc6,0x24)+_0x385207(0x155,-0x61,0x17f,0x8f)+bayar+(_0x529d2f(0x2da,0x254,0x15d,0x207)+_0x385207(-0x144,0x2f,-0xfa,-0x1e))+hasil3+(_0x529d2f(0x38b,0x2cd,0x395,0x1fe)+_0x529d2f(0x311,0x22d,0x28d,0x325))+getMiningore(sender)));await gameAdd(sender,glimit);break;case _0x529d2f(0x3ce,0x350,0x311,0x3ee):const _0x298852={};_0x298852['displayTex'+'t']=_0x529d2f(0x12d,0x21c,0xf5,0x349)+'t';const _0x8c3d8f={};_0x8c3d8f['buttonId']='limit',_0x8c3d8f[_0x385207(0x22,0x83,0x24,-0x3f)]=_0x298852,_0x8c3d8f['type']=0x1;if(isGame(sender,isPremium,isCreator,isOwner,gcounttuser,glimit))return sendButMessage(from,lang['limitg'](prefix),'©\x20'+ownername,[_0x8c3d8f]);const _0x5213fe={};_0x5213fe[_0x529d2f(0x3cd,0x313,0x2bc,0x2e3)+'t']='Event\x20On';const _0x1b161a={};_0x1b161a['buttonId']=_0x385207(0x108,0x12,-0xf4,-0x17),_0x1b161a[_0x385207(0xad,0xf0,-0x93,-0x3f)]=_0x5213fe,_0x1b161a['type']=0x1;if(!isEventon)return sendButMessage(from,lang[_0x385207(0x2a,-0x5,-0x1,0xdb)](prefix),'©\x20'+ownername,[_0x1b161a]);bayar=args[_0x385207(0x106,0xe4,0x8b,0x169)]('\x20');const hargaStone=0x1495*0x1+0x5cb+-0xb*0x214,hasil4=bayar*hargaStone;if(getMiningstone(sender)<=-0xf*0x37+0x17*0x16a+-0x1d4c)return reply(_0x529d2f(0x1ec,0x291,0x23d,0x1c2)+pushname+(_0x529d2f(0x33c,0x21d,0x20c,0x220)+_0x385207(0x146,0x269,0x238,0x180)+'kup,\x20minim'+_0x529d2f(0x15d,0x134,0x4b,0x120)));getMiningstone(sender)>=0x1fa4+-0x1*-0x17d5+-0xa*0x58c&&(jualstone(sender,bayar),addKoinUser(sender,hasil4),await reply('*「\x20PENJUAL'+_0x529d2f(0x1de,0x167,0x152,0x227)+_0x529d2f(0x3e6,0x36a,0x270,0x452)+enter+enter+(_0x385207(0x6c,0xe2,0x5,-0x1d)+_0x385207(0x5a,0x15f,0x134,0xcb)+'*\x20')+bayar+enter+(_0x529d2f(0x3a4,0x370,0x34d,0x2ee)+_0x529d2f(0x2eb,0x20f,0xdd,0x2e2))+hasil4+enter+enter+(_0x385207(0x55,0x59,0x180,0x176)+_0x529d2f(0x206,0x14d,0x66,0x1f6))+getMiningstone(sender)+enter+(_0x529d2f(0x236,0x1f1,0x108,0xbc)+_0x529d2f(0x160,0x14d,0x1f9,0x74))+checkATMuser(sender)+enter+enter+('Proses\x20ber'+_0x529d2f(0x171,0x27c,0x3ad,0x31b)+_0x529d2f(0x292,0x215,0x26d,0x1ea)+_0x529d2f(0x204,0x224,0x2fb,0x283)+'d88288bak1'+_0x529d2f(0x31e,0x353,0x279,0x22a))));await gameAdd(sender,glimit);break;case _0x529d2f(0xb3,0x135,0x76,0x1b):const _0x31cd85={};_0x31cd85[_0x529d2f(0x2a7,0x313,0x39f,0x30f)+'t']=_0x385207(0xfd,0x3,0x1bd,0x85)+'t';const _0x25dd21={};_0x25dd21[_0x529d2f(0x1e7,0x144,0x18,0x22f)]='limit',_0x25dd21[_0x529d2f(0xb8,0x158,0x215,0x5a)]=_0x31cd85,_0x25dd21[_0x385207(0x2e4,0x2ce,0x17c,0x1e8)]=0x1;if(isGame(sender,isPremium,isCreator,isOwner,gcounttuser,glimit))return sendButMessage(from,lang[_0x529d2f(0x226,0x282,0x1e8,0x275)](prefix),'©\x20'+ownername,[_0x25dd21]);const _0x3632dc={};_0x3632dc[_0x385207(0x1bf,0x15f,0x278,0x17c)+'t']=_0x529d2f(0x1f8,0x212,0x15f,0xd8);const _0x386459={};_0x386459[_0x385207(0x59,-0x5f,0xa6,-0x53)]=_0x529d2f(0xc9,0x180,0x8f,0x5d),_0x386459['buttonText']=_0x3632dc,_0x386459[_0x529d2f(0x2c4,0x37f,0x294,0x390)]=0x1;if(!isEventon)return sendButMessage(from,lang[_0x529d2f(0x312,0x272,0x209,0x320)](prefix),'©\x20'+ownername,[_0x386459]);bayar=args[_0x385207(0x7f,0x71,0x1b8,0x169)]('\x20');const hargaIngot=0x5911+-0x25*-0x482+0x1105*-0x7,hasil5=bayar*hargaIngot;if(getMiningingot(sender)<=-0x49*0x42+-0x297+0x2*0xab5)return reply(_0x529d2f(0x291,0x291,0x1e8,0x339)+pushname+(_0x529d2f(0x404,0x379,0x31f,0x2ca)+'u\x20belum\x20cu'+_0x529d2f(0x26e,0x2af,0x2c4,0x175)+_0x385207(0x249,0x224,0xe6,0x124)));getMiningingot(sender)>=0x17af+0x1d8e+-0x353c&&(jualingot(sender,bayar),addKoinUser(sender,hasil5),await reply(_0x529d2f(0x2c6,0x1dd,0x294,0x307)+_0x529d2f(0x1dc,0x167,0x1d0,0x10a)+_0x529d2f(0xdc,0x1f6,0x1c6,0x1ac)+enter+enter+(_0x529d2f(0x2f4,0x362,0x389,0x3eb)+_0x529d2f(0x1c5,0x289,0x16f,0x16b)+':*\x20')+bayar+enter+(_0x385207(0x170,0x233,0xd2,0x1d9)+_0x385207(0xc8,0x58,0x199,0x78))+hasil5+enter+enter+(_0x529d2f(0x2ba,0x287,0x25a,0x380)+_0x385207(0x5d,0x160,0x159,0x129))+getMiningingot(sender)+enter+(_0x385207(0xd6,-0x60,0xc2,0x5a)+':*\x20')+checkATMuser(sender)+enter+enter+(_0x385207(0x206,0x237,0x165,0x1ba)+'hasil\x20deng'+_0x385207(0x18b,0xbb,0x46,0x7e)+_0x385207(0x187,0xfc,0x46,0x8d)+_0x529d2f(0x237,0x190,0x224,0x22c)+_0x529d2f(0x37e,0x353,0x427,0x271))));await gameAdd(sender,glimit);break;case _0x385207(0x211,0x285,0x1ba,0x1ae):const _0x36614a={};_0x36614a[_0x385207(0xf4,0x59,0x2ab,0x17c)+'t']=_0x385207(0xe9,0x1a5,0xff,0x85)+'t';const _0x43bc2d={};_0x43bc2d[_0x385207(-0x14,-0x166,0x5b,-0x53)]=_0x529d2f(0x2bb,0x2ad,0x260,0x174),_0x43bc2d[_0x529d2f(0xd0,0x158,0x1cc,0x2e)]=_0x36614a,_0x43bc2d[_0x385207(0x1b6,0x2db,0x230,0x1e8)]=0x1;if(isGame(sender,isPremium,isCreator,isOwner,gcounttuser,glimit))return sendButMessage(from,lang[_0x385207(0x1f8,-0x24,0x133,0xeb)](prefix),'©\x20'+ownername,[_0x43bc2d]);const _0xc493cd={};_0xc493cd['displayTex'+'t']=_0x529d2f(0x130,0x212,0x2db,0x326);const _0x5e4095={};_0x5e4095[_0x529d2f(0x23c,0x144,0x23a,0x23b)]=_0x385207(-0x48,0x111,0xdf,-0x17),_0x5e4095[_0x385207(-0xcc,0xa2,-0x160,-0x3f)]=_0xc493cd,_0x5e4095[_0x529d2f(0x40a,0x37f,0x319,0x244)]=0x1;if(!isEventon)return sendButMessage(from,lang[_0x385207(0x120,-0x3c,-0x26,0xdb)](prefix),'©\x20'+ownername,[_0x5e4095]);bayar=args['join']('\x20');const hargaKayu=-0x1*0x774a+-0xf69+-0x1*-0xcd03,hasil6=bayar*hargaKayu;if(getNebangKayu(sender)<=-0x627+0xd5*-0xf+-0x1*-0x12a3)return reply(_0x385207(0x213,0xe8,0x17b,0xfa)+pushname+('\x20kayu\x20kamu'+_0x385207(-0x4b,0x7a,0xf5,0xb6)+_0x529d2f(0x282,0x14a,0x4b,0x18c)+'l\x202\x20kayu'));getNebangKayu(sender)>=-0x2*-0x15c+0xdef+0x2*-0x853&&(jualkayu(sender,bayar),addKoinUser(sender,hasil6),await reply(_0x385207(-0x54,0xee,-0x76,0x46)+_0x529d2f(0x15d,0x167,0x104,0x1aa)+_0x385207(-0xaf,0x20,-0x3c,0x5f)+enter+enter+(_0x385207(0x233,0x20e,0x128,0x162)+_0x385207(0x24a,0x19e,0xa9,0x16a)+'*\x20')+bayar+enter+(_0x529d2f(0x40d,0x370,0x2fc,0x34e)+_0x529d2f(0x30d,0x20f,0x21a,0x137))+hasil6+enter+enter+(_0x529d2f(0x3e9,0x35a,0x246,0x442)+_0x385207(0x11f,-0x40,0x18d,0x9c))+getNebangKayu(sender)+enter+(_0x529d2f(0x142,0x1f1,0x169,0x2bc)+':*\x20')+checkATMuser(sender)+enter+enter+(_0x385207(0x25f,0x1e7,0x13a,0x1ba)+_0x529d2f(0x346,0x27c,0x395,0x3a4)+_0x385207(0x73,-0x16,0xff,0x7e)+_0x529d2f(0x340,0x224,0x114,0x141)+_0x529d2f(0x2b7,0x190,0x167,0x288)+'920kal')));await gameAdd(sender,glimit);break;case _0x529d2f(0x194,0x157,0x62,0x101):const _0x56332c={};_0x56332c['displayTex'+'t']=_0x529d2f(0xed,0x21c,0x297,0x146)+'t';const _0x3197b7={};_0x3197b7[_0x529d2f(0x12a,0x144,0x67,0x16)]=_0x529d2f(0x3b5,0x2ad,0x2c5,0x305),_0x3197b7[_0x385207(-0x118,0xea,0x95,-0x3f)]=_0x56332c,_0x3197b7[_0x529d2f(0x458,0x37f,0x28e,0x2af)]=0x1;if(isGame(sender,isPremium,isCreator,isOwner,gcounttuser,glimit))return sendButMessage(from,lang[_0x529d2f(0x2b9,0x282,0x239,0x176)](prefix),'©\x20'+ownername,[_0x3197b7]);const _0x187541={};_0x187541[_0x385207(0x13d,0x19b,0x14e,0x17c)+'t']=_0x385207(0x74,0x38,-0x57,0x7b);const _0xb830e6={};_0xb830e6[_0x529d2f(0x13c,0x144,0x1da,0xb0)]=_0x529d2f(0x240,0x180,0x238,0x47),_0xb830e6[_0x529d2f(0x79,0x158,0x150,0x12a)]=_0x187541,_0xb830e6['type']=0x1;if(!isEventon)return sendButMessage(from,lang[_0x385207(0x61,-0x32,0x11b,0xdb)](prefix),'©\x20'+ownername,[_0xb830e6]);if(isOwner){const one=-0x1e312815+-0x46fe9913+0x3*0x3598d90d;addLevelingXp(sender,one),addLevelingLevel(sender,-0x3*-0x69d+-0x270+-0x1104),reply(_0x529d2f(0x279,0x2d8,0x2ba,0x20a)+_0x529d2f(0x2e6,0x1ba,0x232,0x170)+'mi\x20dari\x20te'+_0x385207(0x219,0x1d9,0xdf,0x1a9)+'girim\x20'+one+(_0x385207(0x1ad,0x1bb,0x172,0xa1)+'nda'));}else setTimeout(()=>{const _0x184d09={'idqiE':function(_0x4a5222,_0x5c43a8,_0x392e37){return _0x4a5222(_0x5c43a8,_0x392e37);},'pURFo':function(_0x23ca25,_0x39f3d8){return _0x23ca25(_0x39f3d8);}};function _0x593133(_0x255f3d,_0xa47811,_0x178bcf,_0x37b6ea){return _0x529d2f(_0x255f3d-0x4a,_0x37b6ea- -0xf,_0x178bcf-0x1c4,_0x255f3d);}const _0x444ecb=Math['ceil'](Math[_0x593133(0x137,0x1fb,0x1f1,0x17d)]()*(0x373*0x3+-0x3250+0x4f07));function _0x5693c8(_0xd1e88f,_0x3543ab,_0x5b06a8,_0x24a515){return _0x529d2f(_0xd1e88f-0x132,_0x3543ab-0x33f,_0x5b06a8-0x127,_0x24a515);}_0x184d09[_0x5693c8(0x6ac,0x591,0x60e,0x606)](addLevelingXp,sender,_0x444ecb),_0x184d09[_0x593133(0x1f7,0x23b,0x29f,0x2f4)](reply,_0x5693c8(0x545,0x60f,0x688,0x634)+_0x5693c8(0x3a5,0x4d3,0x4a8,0x412)+pushname+(_0x593133(0x26a,0x15b,0x287,0x268)+'apatkan\x20*')+_0x444ecb+_0x593133(0x48b,0x267,0x3d8,0x363));},-0x1120+0x217b+0x4a3*-0x1),setTimeout(()=>{const _0xef8de1={'bmSkv':function(_0xe2dea,_0xb096b1){return _0xe2dea(_0xb096b1);},'aERYE':_0x373bd6(0x6d,0x121,0x203,0x1a2)+_0xacc467(0x4de,0x3d0,0x36d,0x4f9)+'\x202\x20menit,\x20'+_0xacc467(0x576,0x456,0x434,0x4c2)+_0xacc467(0x30f,0x3bd,0x387,0x419)};function _0x373bd6(_0x3ed84b,_0x569acc,_0x1c70cf,_0xc43e1f){return _0x385207(_0x569acc,_0x569acc-0x1cc,_0x1c70cf-0x19e,_0xc43e1f-0xe3);}function _0xacc467(_0x23abb0,_0x102060,_0x4b1d1e,_0x3ec64d){return _0x529d2f(_0x23abb0-0x1c9,_0x102060-0x1d9,_0x4b1d1e-0x17a,_0x23abb0);}_0xef8de1[_0xacc467(0x425,0x477,0x44a,0x3bb)](reply,_0xef8de1[_0x373bd6(0x272,0x202,0x23a,0x29e)]);},0xe93*-0x1+0x11*0x3a+0xab9);await gameAdd(sender,glimit);break;case _0x529d2f(0x1fa,0x19b,0x277,0x170):const _0x40383b={};_0x40383b[_0x385207(0x1f4,0xd9,0xb4,0x17c)+'t']='Check\x20Limi'+'t';const _0x5f2bb4={};_0x5f2bb4[_0x529d2f(0x13a,0x144,0xb9,0x174)]=_0x385207(-0x7,0xb4,0x178,0x116),_0x5f2bb4[_0x529d2f(0x231,0x158,0x7d,0xce)]=_0x40383b,_0x5f2bb4['type']=0x1;if(isGame(sender,isPremium,isCreator,isOwner,gcounttuser,glimit))return sendButMessage(from,lang[_0x529d2f(0x153,0x282,0x160,0x352)](prefix),'©\x20'+ownername,[_0x5f2bb4]);const _0x226b1f={};_0x226b1f[_0x385207(0x1c6,0x44,0x130,0x17c)+'t']=_0x385207(0xe7,0x75,0x7d,0x7b);const _0x1f8133={};_0x1f8133['buttonId']=_0x385207(-0x43,0xa0,0xd4,-0x17),_0x1f8133[_0x385207(-0xb6,-0x34,-0x92,-0x3f)]=_0x226b1f,_0x1f8133[_0x529d2f(0x42c,0x37f,0x3ba,0x48f)]=0x1;if(!isEventon)return sendButMessage(from,lang[_0x385207(-0x1d,0x146,0x91,0xdb)](prefix),'©\x20'+ownername,[_0x1f8133]);setTimeout(()=>{function _0x1668b7(_0x2ad464,_0x1541f4,_0x51d7d9,_0x4fc4c1){return _0x385207(_0x1541f4,_0x1541f4-0x1ef,_0x51d7d9-0xb5,_0x4fc4c1-0x1e7);}const _0x18037e={'iGkdD':function(_0x5b0f4b,_0x438f0d){return _0x5b0f4b*_0x438f0d;},'dIcBJ':function(_0x5c19dc,_0x29e72c,_0x35d099){return _0x5c19dc(_0x29e72c,_0x35d099);}};function _0x2b3317(_0x39339e,_0x5969d2,_0x4e32b5,_0x47a077){return _0x529d2f(_0x39339e-0xc7,_0x47a077- -0x9b,_0x4e32b5-0x1dd,_0x4e32b5);}const _0x10d132=Math[_0x2b3317(0xa3,0x183,0x93,0x104)](_0x18037e[_0x1668b7(0x415,0x277,0x3f6,0x2dc)](Math[_0x2b3317(0xb7,0x17,-0x42,0xf1)](),0x1*-0x1e91+-0x2a9+-0x1*-0x2144));_0x18037e[_0x2b3317(0x239,0x34f,0x256,0x245)](addIkan,sender,_0x10d132),reply(_0x1668b7(0x258,0x278,0x2e0,0x320)+_0x1668b7(0x25f,0x450,0x476,0x37b)+_0x2b3317(0x15c,0x282,0x182,0x1dc)+'apatkan\x20*'+_0x10d132+(_0x1668b7(0x31d,0x2ff,0x4c5,0x3a9)+_0x2b3317(0x2ce,0x1fd,0x1fa,0x1e4)+'t'));},0x2694+0x4cc+-0x1fa8),setTimeout(()=>{function _0x188e0a(_0x4775d0,_0x42b4e3,_0x555629,_0x14f0e8){return _0x529d2f(_0x4775d0-0x95,_0x42b4e3- -0x28b,_0x555629-0xc8,_0x4775d0);}const _0x2e82bb={};_0x2e82bb[_0x188e0a(0x199,0xa7,0x138,-0x25)]='Sedang\x20Mem'+_0xdb432a(-0x13d,-0x221,-0x232,-0x203)+_0x188e0a(0x104,0xb3,0x78,-0x73)+_0xdb432a(-0x22c,-0x1a5,-0x130,-0x18c);function _0xdb432a(_0x40ad9a,_0x1af2fb,_0x1b4d1c,_0x29da6c){return _0x385207(_0x1b4d1c,_0x1af2fb-0x12b,_0x1b4d1c-0xb2,_0x40ad9a- -0x251);}const _0x3db406=_0x2e82bb;reply(_0x3db406['huduf']);},0x983+-0x1469+0x5d*0x1e),await gameAdd(sender,glimit);break;case _0x385207(0x102,0x58,-0x82,0x97):case _0x529d2f(0x10b,0x1d1,0x2c6,0x1be):const _0x51acf4={};_0x51acf4['displayTex'+'t']='Check\x20Limi'+'t';const _0x4e70f6={};_0x4e70f6[_0x385207(-0x56,0x8b,-0x18d,-0x53)]=_0x385207(0x52,0x177,0x10b,0x116),_0x4e70f6[_0x385207(-0xfd,0x73,-0x12a,-0x3f)]=_0x51acf4,_0x4e70f6[_0x529d2f(0x491,0x37f,0x479,0x4aa)]=0x1;if(isGame(sender,isPremium,isCreator,isOwner,gcounttuser,glimit))return sendButMessage(from,lang['limitg'](prefix),'©\x20'+ownername,[_0x4e70f6]);const _0x4e372b={};_0x4e372b[_0x385207(0x148,0x1d1,0x1bf,0x17c)+'t']='Event\x20On';const _0x3b3b2d={};_0x3b3b2d['buttonId']=_0x385207(0xd,0x11b,0x52,-0x17),_0x3b3b2d[_0x385207(0xe3,-0x153,0x50,-0x3f)]=_0x4e372b,_0x3b3b2d[_0x385207(0x236,0x18e,0x18f,0x1e8)]=0x1;if(!isEventon)return sendButMessage(from,lang['event'](prefix),'©\x20'+ownername,[_0x3b3b2d]);var tempsa=args[_0x529d2f(0x3d8,0x300,0x3d9,0x3e5)]('\x20');if(tempsa=='corbiens\x20r'+_0x529d2f(0x1ef,0x2f3,0x21c,0x300)){const _0x35daf2={};_0x35daf2[_0x385207(0x9f,0x58,0x122,0xad)]='get',asu=await getBuffer(_0x385207(0x1fe,0x57,0x1ca,0x13b)+_0x385207(0x20f,-0x12,0x1ba,0xec)+_0x385207(0x1d8,0x1e5,0x160,0x1fc)+'ab77a6cea8'+'1523e.jpg',_0x35daf2),setTimeout(()=>{function _0x474a65(_0x189fc3,_0x57782b,_0x5b07a1,_0x3e2a09){return _0x529d2f(_0x189fc3-0x57,_0x57782b-0x349,_0x5b07a1-0x17b,_0x5b07a1);}const _0x541f1e={'QDvWR':function(_0x5705a3,_0xe8efac){return _0x5705a3*_0xe8efac;},'SvYxM':function(_0x25e21e,_0x3a0e01){return _0x25e21e*_0x3a0e01;},'GFnKZ':function(_0xb427cc,_0x51820c,_0x552f87,_0x944e34,_0x544cef,_0x22dfab,_0x475da2){return _0xb427cc(_0x51820c,_0x552f87,_0x944e34,_0x544cef,_0x22dfab,_0x475da2);},'KRpQB':'My\x20Invento'+_0xe7da8a(0x3be,0x488,0x53e,0x42e),'JQEDG':_0xe7da8a(0x321,0x247,0x476,0x33b)},_0x2163ba=Math['ceil'](_0x541f1e[_0x474a65(0x39d,0x4ac,0x5d6,0x4c8)](Math[_0xe7da8a(0x2d4,0x252,0x393,0x319)](),-0x1113+-0x30*-0xb5+0x1*-0x1097)),_0xcc4131=Math[_0xe7da8a(0x2a0,0x2d5,0x341,0x32c)](_0x541f1e['SvYxM'](Math['random'](),0x114+-0x7*-0x15+-0x198));function _0xe7da8a(_0x3e1c4a,_0x221e02,_0xdab564,_0x511b29){return _0x385207(_0xdab564,_0x221e02-0x2e,_0xdab564-0x16,_0x511b29-0x324);}addStone(sender,_0x2163ba),addIkan(sender,_0xcc4131);const _0x3f814b={};_0x3f814b[_0xe7da8a(0x4e3,0x4d4,0x4d7,0x4e4)]=mek,_0x541f1e[_0x474a65(0x4eb,0x622,0x66c,0x5ef)](sendButImage,from,_0x474a65(0x6d7,0x619,0x501,0x681)+_0x474a65(0x4c3,0x53c,0x5aa,0x5cc)+enter+enter+(_0x474a65(0x5d7,0x4a3,0x38b,0x464)+_0x474a65(0x6af,0x6b7,0x75c,0x6fc))+_0x2163ba+(_0xe7da8a(0x2c8,0x3ef,0x341,0x3f2)+'\x20*')+_0xcc4131+_0xe7da8a(0x42f,0x3fa,0x337,0x370)+enter+enter+(_0x474a65(0x575,0x620,0x73d,0x719)+'ory\x20anda\x20d'+'engan\x20cara'+_0x474a65(0x5c0,0x4b3,0x5dd,0x5e7))+prefix+'inventory','©\x20'+ownername,asu,[{'buttonId':_0x474a65(0x6c7,0x688,0x580,0x64b),'buttonText':{'displayText':_0x541f1e['KRpQB']},'type':_0x541f1e[_0x474a65(0x5db,0x531,0x421,0x531)]}],_0x3f814b);},0x1*-0x2429+-0x23e9*0x1+-0x21*-0x28a),setTimeout(()=>{function _0x5da573(_0x50e558,_0x4ef3bf,_0x2c2ed5,_0x300d2f){return _0x385207(_0x2c2ed5,_0x4ef3bf-0x14c,_0x2c2ed5-0x3d,_0x4ef3bf-0x147);}function _0x2c1480(_0x27d7e9,_0x1c505c,_0x2a28b3,_0x26a8ad){return _0x529d2f(_0x27d7e9-0xfc,_0x2a28b3- -0x8,_0x2a28b3-0xf8,_0x1c505c);}const _0x55cc0b={'HNaNI':function(_0x404752,_0x592302){return _0x404752(_0x592302);}};_0x55cc0b[_0x2c1480(0x117,0xd7,0x201,0x33c)](reply,_0x2c1480(0x356,0x46d,0x38f,0x31a)+_0x2c1480(0x3ce,0x42f,0x37a,0x2b8)+'\x20silahkan\x20'+_0x5da573(0x206,0x1fe,0x2ee,0x20d));},-0x21a3+0x50e+0x9*0x32d);}else{if(tempsa===_0x385207(0x2eb,0x2d3,0x32b,0x1ff)+_0x385207(0xfd,0x265,0x1f9,0x1b8)){const _0x203aca={};_0x203aca[_0x385207(-0x24,0xba,-0x64,0xad)]=_0x529d2f(0x337,0x38d,0x451,0x2a5),gos=await getBuffer('https://te'+_0x385207(0x38,-0x42,0x11c,0xec)+_0x529d2f(0x163,0x184,0x202,0x231)+_0x529d2f(0x310,0x2da,0x338,0x28e)+_0x385207(0x277,0x164,0x2ac,0x1da),_0x203aca),setTimeout(()=>{const _0x3696d1={'EcvhJ':function(_0x2212c2,_0x4c22b0){return _0x2212c2*_0x4c22b0;},'wXVnl':function(_0x1d8480,_0x1994fd,_0x5cdd05){return _0x1d8480(_0x1994fd,_0x5cdd05);},'wrbEc':_0x2742bb(-0x12e,-0x16c,-0x124,-0x15d)+'ry\x20🗃️'},_0x3ab007=Math['ceil'](_0x3696d1['EcvhJ'](Math['random'](),0x1939+0x24e+-0x1b19)),_0x135a64=Math[_0x544da1(-0x24f,-0x1fa,-0x7c,-0x1ad)](_0x3696d1[_0x2742bb(-0x2ab,-0x1c7,-0x3b3,-0x182)](Math['random'](),-0x1e62+0x213f*-0x1+0x3fb5));_0x3696d1['wXVnl'](addStone,sender,_0x3ab007),addKayu(sender,_0x135a64);const _0x2da8bf={};function _0x544da1(_0x26cab9,_0x43fb56,_0x397951,_0x8db4ed){return _0x529d2f(_0x26cab9-0x4,_0x8db4ed- -0x34c,_0x397951-0xff,_0x397951);}_0x2da8bf['displayTex'+'t']=_0x3696d1[_0x544da1(0x104,0x90,0x10,0x51)];function _0x2742bb(_0x327298,_0xcd3a0d,_0xafb6ae,_0x473c62){return _0x529d2f(_0x327298-0x10a,_0x327298- -0x3dc,_0xafb6ae-0x14a,_0xcd3a0d);}const _0x3d1d7f={};_0x3d1d7f[_0x544da1(-0x289,-0x25a,-0x28e,-0x208)]=_0x544da1(-0x13,0x53,-0xf6,-0xd),_0x3d1d7f[_0x544da1(-0x27a,-0x18d,-0x227,-0x1f4)]=_0x2da8bf,_0x3d1d7f['type']=_0x2742bb(-0x22e,-0x341,-0x170,-0x207);const _0x411faa={};_0x411faa[_0x544da1(0xb7,-0x104,0xc7,0xb)]=mek,sendButImage(from,_0x544da1(0xa8,-0xc9,-0xd2,-0x7c)+_0x544da1(-0x41,-0x181,-0xd1,-0x159)+enter+enter+(_0x544da1(-0x1f0,-0x179,-0x2db,-0x1f2)+_0x2742bb(-0x6e,-0x111,-0x7b,-0xc9))+_0x3ab007+(_0x2742bb(-0x177,-0x123,-0x172,-0x21f)+'\x20*')+_0x135a64+_0x2742bb(-0x1ed,-0x1ef,-0x15a,-0x185)+enter+enter+(_0x2742bb(-0x105,-0x6c,-0x17f,-0x1bd)+'ory\x20anda\x20d'+_0x2742bb(-0x1db,-0x24f,-0x1b0,-0x201)+'\x20ketik\x20')+prefix+'inventory','©\x20'+ownername,gos,[_0x3d1d7f],_0x411faa);},-0x17ff*0x1+-0x1*0x19e2+0x3d99),setTimeout(()=>{const _0x4cbf6c={'AyTmI':function(_0x56b60d,_0x28f443){return _0x56b60d(_0x28f443);},'kjmDr':_0xe0096d(0x7bc,0x6af,0x678,0x5e2)+_0x404546(0x50d,0x5e7,0x5e1,0x51f)+_0xe0096d(0x4c3,0x538,0x5e2,0x674)+_0xe0096d(0x692,0x566,0x4cd,0x686)};function _0x404546(_0x3bf24d,_0x503319,_0x40c43f,_0x386cf8){return _0x385207(_0x40c43f,_0x503319-0x78,_0x40c43f-0x1e4,_0x503319-0x3fc);}function _0xe0096d(_0x3d1b77,_0x223b3f,_0x3a1667,_0x13567d){return _0x529d2f(_0x3d1b77-0x87,_0x223b3f-0x318,_0x3a1667-0x193,_0x13567d);}_0x4cbf6c[_0xe0096d(0x5e1,0x6a0,0x608,0x6e4)](reply,_0x4cbf6c[_0xe0096d(0x59a,0x48e,0x3e0,0x540)]);},0x455+0x130b+-0x8*0x2ec);}else{if(tempsa===_0x529d2f(0x299,0x31b,0x1df,0x28b)+'a'){const _0xc0716e={};_0xc0716e[_0x385207(0x13a,0x12d,-0x81,0xad)]=_0x385207(0x2a5,0x14a,0x1bc,0x1f6),seae=await getBuffer(_0x385207(0x17,0x183,0x39,0x13b)+_0x529d2f(0x2fa,0x283,0x1d4,0x1db)+_0x385207(-0xe0,-0xa1,-0xd3,-0x25)+_0x529d2f(0x2b8,0x1e6,0x20e,0x172)+_0x385207(0x18a,0x19a,0x165,0x1f5),_0xc0716e),setTimeout(()=>{const _0x26832c={'tiEfx':function(_0x2c841b,_0x1930c3){return _0x2c841b*_0x1930c3;},'UnwAd':function(_0x2b1e9e,_0x2cd4a0,_0x258aef){return _0x2b1e9e(_0x2cd4a0,_0x258aef);},'voSKI':function(_0x4b9cc6,_0x224c64,_0x59899a,_0x5166f9,_0xc49846,_0x15023f,_0x264b87){return _0x4b9cc6(_0x224c64,_0x59899a,_0x5166f9,_0xc49846,_0x15023f,_0x264b87);},'iCsnO':_0x42be3a(0x85,-0x26,0x1ac,0x88)+_0x7ed1f1(0x529,0x34e,0x479,0x409),'xsoRg':'RESPONSE'};function _0x42be3a(_0x4eaba2,_0x6c518e,_0x47ac6,_0x497adb){return _0x385207(_0x47ac6,_0x6c518e-0x25,_0x47ac6-0x19e,_0x497adb- -0x8f);}const _0x1add2a=Math[_0x42be3a(-0x117,-0x11,0xb5,-0x87)](_0x26832c[_0x7ed1f1(0x303,0x415,0x269,0x38d)](Math[_0x42be3a(-0x123,-0x5a,0x36,-0x9a)](),0x17df+-0x1*-0x165a+-0x4*0xb7e));_0x26832c[_0x42be3a(-0x25,0x12b,0x172,0xf2)](addIkan,sender,_0x1add2a);const _0x58c21e={};_0x58c21e['quoted']=mek;function _0x7ed1f1(_0x2fad45,_0x3ad71d,_0x109993,_0x1c39c5){return _0x529d2f(_0x2fad45-0x152,_0x1c39c5-0x168,_0x109993-0x10c,_0x109993);}_0x26832c['voSKI'](sendButImage,from,_0x42be3a(-0x1f,0x173,-0x89,0xaa)+_0x7ed1f1(0x438,0x252,0x441,0x35b)+enter+enter+('Kamu\x20menda'+'patkan\x20*')+_0x1add2a+_0x42be3a(0x99,0x7a,-0x14b,-0x43)+enter+enter+('Cek\x20invent'+'ory\x20anda\x20d'+_0x42be3a(0xd1,0x28,0x48,-0x25)+'\x20ketik\x20')+prefix+_0x7ed1f1(0x465,0x526,0x520,0x502),_0x42be3a(-0x58,-0x9f,0x1a,0x21)+ownername,seae,[{'buttonId':_0x42be3a(0x68,0x5b,0x223,0x119),'buttonText':{'displayText':_0x26832c[_0x42be3a(-0xbb,-0x124,-0x38,-0xcd)]},'type':_0x26832c['xsoRg']}],_0x58c21e);},0x462+-0x1*0xe3c+0x1592),setTimeout(()=>{const _0x56d9d8={};function _0x39014e(_0x3875f8,_0xe50dff,_0x14b702,_0x3e3a17){return _0x529d2f(_0x3875f8-0x1a0,_0x3e3a17- -0x148,_0x14b702-0x173,_0x3875f8);}_0x56d9d8[_0x39014e(0x26f,0x301,0x19e,0x1ef)]='Sedang\x20ber'+_0xad420(0x35f,0x2b7,0x37f,0x33f)+_0x39014e(0x215,0xf1,-0x38,0xd8)+'tunggu...';function _0xad420(_0x2c3660,_0xb621b2,_0x220114,_0x1f1931){return _0x385207(_0xb621b2,_0xb621b2-0xfc,_0x220114-0xda,_0x2c3660-0x174);}const _0x409e28=_0x56d9d8;reply(_0x409e28['vxXjz']);},0x1f53+0x3db+-0x26*0xed);}else{if(tempsa===_0x529d2f(0xc7,0x1a6,0xf4,0xef)+_0x529d2f(0x34f,0x389,0x489,0x328)+'s'){const _0x4cbc32={};_0x4cbc32[_0x385207(0xa7,0xb4,0x139,0xad)]=_0x529d2f(0x2bf,0x38d,0x33e,0x27d),seoe=await getBuffer(_0x529d2f(0x3ad,0x2d2,0x227,0x2e2)+'legra.ph/f'+_0x385207(0x6,-0x6,0x63,0x9d)+_0x529d2f(0x258,0x2b5,0x38c,0x316)+_0x385207(0x96,0x210,0xde,0x193),_0x4cbc32),setTimeout(()=>{const _0x5cacfb={'rtSOI':function(_0x48377,_0x13de71){return _0x48377*_0x13de71;},'jWkXv':function(_0x388a42,_0x14c298,_0x45953f){return _0x388a42(_0x14c298,_0x45953f);},'ZIzYY':function(_0x26dc9b,_0x2b94ab,_0x49b385){return _0x26dc9b(_0x2b94ab,_0x49b385);},'gjbqB':_0x72caeb(0x5d2,0x58d,0x575,0x4ab)+'ry\x20🗃️','hrlkX':'RESPONSE'},_0x2302ac=Math['ceil'](Math['random']()*(-0x5d7+-0xf9a+-0x1d*-0xbf)),_0x2697c3=Math[_0x72caeb(0x4c3,0x580,0x5c0,0x4aa)](_0x5cacfb[_0x72caeb(0x620,0x53e,0x5ca,0x68f)](Math[_0x10614a(0x1d9,0x1ce,0x253,0x1b4)](),0x2496+0x199*0x1+-0x25df));_0x5cacfb[_0x10614a(0x30e,0x269,0x36d,0x2a2)](addOre,sender,_0x2302ac),_0x5cacfb[_0x10614a(0x307,0x210,0x306,0x3bb)](addStone,sender,_0x2697c3);function _0x72caeb(_0x2a0bf4,_0x42dc17,_0x59c940,_0x32412d){return _0x529d2f(_0x2a0bf4-0x20,_0x2a0bf4-0x324,_0x59c940-0x117,_0x32412d);}const _0x221e38={};_0x221e38[_0x72caeb(0x637,0x54b,0x585,0x6f8)+'t']=_0x5cacfb[_0x72caeb(0x5a9,0x482,0x49a,0x617)];function _0x10614a(_0x12fb27,_0x374525,_0x6b112f,_0x25bdb7){return _0x385207(_0x25bdb7,_0x374525-0x23,_0x6b112f-0x6c,_0x12fb27-0x1e4);}const _0x2c1400={};_0x2c1400[_0x72caeb(0x468,0x4d8,0x45b,0x399)]='inv',_0x2c1400[_0x10614a(0x1a5,0x2b5,0x15f,0x12e)]=_0x221e38,_0x2c1400[_0x72caeb(0x6a3,0x795,0x5dd,0x721)]=_0x5cacfb[_0x10614a(0x2d7,0x2ea,0x2e8,0x2c9)];const _0x252d40={};_0x252d40[_0x10614a(0x3a4,0x4a7,0x278,0x368)]=mek,sendButImage(from,_0x72caeb(0x5f4,0x705,0x5b8,0x6d6)+_0x72caeb(0x517,0x5f5,0x5ce,0x493)+enter+enter+('Kamu\x20menda'+_0x72caeb(0x692,0x5d7,0x6d6,0x6c2))+_0x2302ac+(_0x72caeb(0x495,0x483,0x3b4,0x389)+'re\x20dan\x20')+_0x2697c3+_0x72caeb(0x680,0x5dd,0x631,0x5c3)+enter+enter+(_0x72caeb(0x5fb,0x715,0x6a0,0x578)+_0x72caeb(0x483,0x550,0x432,0x45f)+_0x10614a(0x24e,0x18f,0x130,0x220)+_0x72caeb(0x48e,0x506,0x39d,0x4c2))+prefix+_0x10614a(0x3e7,0x45e,0x317,0x488),'©\x20'+ownername,seoe,[_0x2c1400],_0x252d40);},-0xff0+-0x8ea*-0x3+0xea),setTimeout(()=>{const _0x290581={'ujeLe':function(_0x4306ca,_0x3db69e){return _0x4306ca(_0x3db69e);},'Axcoe':_0x47b1ac(0x25f,0x20b,0x295,0x117)+_0x47b1ac(0x272,0x1f6,0x290,0x26f)+_0x22e824(-0x79,-0x166,-0x17a,-0x114)+_0x22e824(-0x16d,-0x138,-0x1ef,-0x14e)};function _0x22e824(_0x382884,_0x186536,_0x2f65a1,_0x45411d){return _0x529d2f(_0x382884-0x186,_0x186536- -0x386,_0x2f65a1-0x73,_0x2f65a1);}function _0x47b1ac(_0x5f229b,_0x2189ff,_0x2dcf81,_0x2c4bdb){return _0x529d2f(_0x5f229b-0x79,_0x2189ff- -0x18c,_0x2dcf81-0x47,_0x2c4bdb);}_0x290581[_0x47b1ac(0x27d,0x1d9,0x2cf,0x2b9)](reply,_0x290581[_0x47b1ac(0xa7,0xf2,-0x35,0x1b2)]);},0x4a8+0x3c9*-0x3+0x6b3);}else{if(tempsa==='chade\x20moun'+_0x529d2f(0x25b,0x2ce,0x200,0x369)){const _0x43a226={};_0x43a226[_0x529d2f(0x27e,0x244,0x214,0x149)]=_0x385207(0x303,0xfe,0x1e5,0x1f6),seye=await getBuffer(_0x529d2f(0x3b6,0x2d2,0x362,0x2a3)+_0x529d2f(0x1f4,0x283,0x25c,0x16f)+_0x385207(0x267,0x1ae,0x21e,0x1fe)+_0x529d2f(0x1ce,0x1d5,0x1c2,0x2be)+_0x529d2f(0x176,0x26b,0x180,0x137),_0x43a226),setTimeout(()=>{const _0x16f081={'BTMrx':function(_0x74f1a9,_0x3f957a){return _0x74f1a9*_0x3f957a;},'WuYAi':function(_0x31b6b2,_0x13bfae,_0x2b91b0,_0x5c3dff,_0x19ab62,_0x3b842c,_0x3bc022){return _0x31b6b2(_0x13bfae,_0x2b91b0,_0x5c3dff,_0x19ab62,_0x3b842c,_0x3bc022);},'XPEEB':'My\x20Invento'+'ry\x20🗃️'};function _0x3686e6(_0x3d1128,_0x400aa0,_0x1fc749,_0x12007e){return _0x529d2f(_0x3d1128-0x10e,_0x1fc749- -0x3e0,_0x1fc749-0x137,_0x400aa0);}function _0x26c375(_0xd5f899,_0x5c3015,_0x16754f,_0x3e5039){return _0x385207(_0xd5f899,_0x5c3015-0xf2,_0x16754f-0xe1,_0x3e5039-0x4b8);}const _0x3473db=Math[_0x26c375(0x597,0x399,0x419,0x4c0)](_0x16f081[_0x26c375(0x3c7,0x455,0x535,0x457)](Math[_0x3686e6(-0x21d,-0x250,-0x254,-0x30f)](),0x1*-0xc1+-0x11d0+0x12b9)),_0x423c04=Math[_0x3686e6(-0x19d,-0x234,-0x241,-0x2a5)](Math[_0x26c375(0x433,0x3aa,0x593,0x4ad)]()*(0x2f*0x1+0x1*0xf77+-0x7b5*0x2));addOre(sender,_0x3473db),addStone(sender,_0x423c04);const _0x698342={};_0x698342['quoted']=mek,_0x16f081['WuYAi'](sendButImage,from,_0x3686e6(-0x28,-0x5,-0x110,-0xf3)+_0x26c375(0x4a4,0x640,0x42e,0x514)+enter+enter+(_0x26c375(0x579,0x550,0x586,0x47b)+'patkan\x20*')+_0x3473db+(_0x26c375(0x57a,0x5a9,0x3de,0x492)+'re\x20dan\x20')+_0x423c04+_0x26c375(0x55a,0x645,0x5bd,0x67d)+enter+enter+(_0x26c375(0x6f1,0x4cb,0x51d,0x5f8)+_0x3686e6(-0x29b,-0x2be,-0x281,-0x1e5)+_0x3686e6(-0x183,-0x263,-0x1df,-0x10e)+_0x26c375(0x494,0x3ea,0x532,0x48b))+prefix+_0x3686e6(-0x5e,-0x92,-0x46,0xf0),'©\x20'+ownername,seye,[{'buttonId':_0x26c375(0x75f,0x553,0x5ca,0x660),'buttonText':{'displayText':_0x16f081[_0x3686e6(-0x182,-0xc5,-0x18f,-0xf0)]},'type':_0x3686e6(-0x259,-0x143,-0x232,-0x263)}],_0x698342);},-0xe64+0x117b+0x8a1),setTimeout(()=>{function _0xd26057(_0x46dc1f,_0x268284,_0x25f31d,_0x440b55){return _0x529d2f(_0x46dc1f-0x1e7,_0x46dc1f-0xf6,_0x25f31d-0x4a,_0x268284);}const _0x34c389={};_0x34c389[_0x1dfe4a(0x1a0,0x21e,0x1c4,0x141)]=_0xd26057(0x48d,0x405,0x445,0x44c)+_0xd26057(0x478,0x505,0x3ff,0x51f)+'\x20silahkan\x20'+_0xd26057(0x344,0x243,0x297,0x412);const _0x321c9f=_0x34c389;function _0x1dfe4a(_0x316c9d,_0x2bb185,_0x257212,_0x332ad5){return _0x385207(_0x332ad5,_0x2bb185-0x87,_0x257212-0x76,_0x316c9d-0x10f);}reply(_0x321c9f[_0xd26057(0x31e,0x2fa,0x23b,0x2f3)]);},-0x4*0x971+-0x1*-0x537+0x208d);}else{if(tempsa===_0x529d2f(0x1aa,0x2cc,0x2bc,0x36d)+'ds'){const _0x188b2c={};_0x188b2c['method']='get',siae=await getBuffer('https://te'+_0x385207(0x89,0x111,0x4,0xec)+_0x529d2f(0x277,0x141,0x18b,0x173)+_0x385207(0x114,0x33,0x75,0x134)+_0x529d2f(0x370,0x374,0x3e3,0x31e),_0x188b2c),setTimeout(()=>{function _0x4cfc34(_0x39eef9,_0xd5757f,_0x4cbaff,_0x568084){return _0x529d2f(_0x39eef9-0x185,_0x4cbaff- -0xa7,_0x4cbaff-0x55,_0x39eef9);}function _0x2a2fc5(_0x1ec803,_0x4b349d,_0x124c09,_0x166763){return _0x385207(_0x1ec803,_0x4b349d-0x14,_0x124c09-0x90,_0x124c09- -0x13b);}const _0x560c77={'dNClc':function(_0x120682,_0x376f09){return _0x120682*_0x376f09;},'LSiAO':function(_0x5de631,_0x24fec8,_0x208a42){return _0x5de631(_0x24fec8,_0x208a42);},'LJIxv':function(_0x3f704f,_0x4c2e0b,_0x4ad440,_0x30bfd,_0x3632b7,_0x52f254,_0x1f1d75){return _0x3f704f(_0x4c2e0b,_0x4ad440,_0x30bfd,_0x3632b7,_0x52f254,_0x1f1d75);},'TKKwu':_0x4cfc34(0xe9,0x2f3,0x207,0x120)+_0x2a2fc5(0xfd,-0x25,-0x31,0xf9),'RHGve':_0x2a2fc5(-0x1f7,-0x5,-0x124,-0x22d)},_0x37e1eb=Math['ceil'](Math['random']()*(-0x1733+0x1*0x140b+0x382)),_0x471337=Math[_0x4cfc34(0x1e5,0x192,0xf8,0x5d)](_0x560c77[_0x4cfc34(0x332,0x1b0,0x228,0x181)](Math[_0x2a2fc5(-0x191,-0x88,-0x146,-0x199)](),-0x3e0+-0x2034+0x2441));_0x560c77[_0x4cfc34(-0x10,-0x43,0x94,-0x6d)](addStone,sender,_0x37e1eb),_0x560c77[_0x2a2fc5(-0x18c,-0x184,-0x197,-0xec)](addKayu,sender,_0x471337);const _0x3a0d42={};_0x3a0d42[_0x4cfc34(0x2ac,0x2d5,0x2b0,0x307)]=mek,_0x560c77[_0x2a2fc5(0x16b,-0x4,0xcc,0x166)](sendButImage,from,_0x4cfc34(0x335,0x360,0x229,0x2ca)+'ation\x20🎊*'+enter+enter+(_0x4cfc34(0x1ec,0xfd,0xb3,0x1c4)+_0x2a2fc5(0x51,-0x80,0x9c,0xac))+_0x37e1eb+(_0x2a2fc5(0xb5,-0x188,-0x6d,0xa9)+'\x20*')+_0x471337+_0x4cfc34(0x260,0x1a6,0x148,0x239)+enter+enter+(_0x2a2fc5(0x115,-0x9f,0x5,0xcc)+'ory\x20anda\x20d'+_0x2a2fc5(0x48,-0xc6,-0xd1,0x5e)+_0x4cfc34(0x164,-0xb,0xc3,0x126))+prefix+_0x2a2fc5(0x89,-0x2,0xc8,0xae),'©\x20'+ownername,siae,[{'buttonId':_0x2a2fc5(0xf5,0x193,0x6d,0x23),'buttonText':{'displayText':_0x560c77['TKKwu']},'type':_0x560c77['RHGve']}],_0x3a0d42);},-0x2b*-0x95+0x1*-0x2531+0x17e2),setTimeout(()=>{function _0x9f28b9(_0x354493,_0x88ee23,_0x59fa97,_0x8df90f){return _0x385207(_0x354493,_0x88ee23-0xb7,_0x59fa97-0x65,_0x8df90f-0xb3);}function _0x17c54a(_0x2fe10f,_0x46905f,_0x3681d9,_0x1943c3){return _0x385207(_0x46905f,_0x46905f-0x98,_0x3681d9-0x191,_0x3681d9- -0x20b);}reply(_0x9f28b9(0x273,0x3a1,0x222,0x2b3)+_0x17c54a(0x11,-0x103,-0x20,-0x122)+_0x9f28b9(0xd3,0x21a,0x175,0x13c)+'tunggu...');},-0x16ad+0x21cb+0xb1e*-0x1);}else{if(tempsa===_0x529d2f(0x19e,0x213,0x2c0,0x293)+'rassland'){const _0x44a861={};_0x44a861[_0x385207(-0xd,0x70,0x168,0xad)]=_0x385207(0xcb,0x1c2,0x195,0x1f6),bbbb=await getBuffer('https://te'+_0x529d2f(0x242,0x283,0x385,0x251)+_0x529d2f(0x14f,0x165,0xdf,0x190)+_0x529d2f(0x1f5,0x197,0x1d8,0x95)+_0x529d2f(0x35,0x15d,0x250,0x281),_0x44a861),setTimeout(()=>{const _0xfc05d7={'szvyA':function(_0x1f284f,_0x442e42){return _0x1f284f*_0x442e42;},'fADAi':function(_0x4ca432,_0x120294){return _0x4ca432*_0x120294;},'YPuzu':function(_0xa10946,_0x2bdaea,_0x264206){return _0xa10946(_0x2bdaea,_0x264206);},'RGaHI':function(_0x362ea2,_0x5eb850,_0x393d14){return _0x362ea2(_0x5eb850,_0x393d14);},'ftcFk':function(_0x270e17,_0x53c847,_0x462b23,_0x549cd7,_0x45be56,_0x4207d2,_0x26de0e){return _0x270e17(_0x53c847,_0x462b23,_0x549cd7,_0x45be56,_0x4207d2,_0x26de0e);},'SQdgP':'My\x20Invento'+_0x41308f(0x6ed,0x6d5,0x647,0x6fe),'sSVeS':_0x41308f(0x4e2,0x5a3,0x554,0x60b)},_0x57eae7=Math[_0x41308f(0x629,0x606,0x545,0x5a6)](_0xfc05d7[_0xdacb60(0x1f0,0x19c,0x2d6,0x2f9)](Math[_0x41308f(0x4df,0x576,0x532,0x41c)](),0x191d+0xef*-0x21+-0x33d*-0x2));function _0x41308f(_0xb4d293,_0x592230,_0x3812d6,_0x2ed5f7){return _0x385207(_0xb4d293,_0x592230-0x198,_0x3812d6-0x1c4,_0x3812d6-0x53d);}const _0x1fba4a=Math[_0xdacb60(0x39,0x92,-0xfe,-0xd3)](_0xfc05d7[_0x41308f(0x720,0x759,0x691,0x64f)](Math[_0xdacb60(0x26,-0xca,0x14d,0x74)](),-0xd9b+0xc03*0x1+0x1ac));function _0xdacb60(_0x4d6586,_0x562c41,_0x83b25b,_0x52fa9f){return _0x529d2f(_0x4d6586-0x3c,_0x4d6586- -0x166,_0x83b25b-0x1cd,_0x52fa9f);}_0xfc05d7[_0x41308f(0x53c,0x5a7,0x5ae,0x516)](addStone,sender,_0x57eae7),_0xfc05d7['RGaHI'](addKayu,sender,_0x1fba4a);const _0x98fd7f={};_0x98fd7f['quoted']=mek,_0xfc05d7[_0x41308f(0x611,0x660,0x627,0x67d)](sendButImage,from,_0x41308f(0x680,0x73f,0x676,0x547)+_0xdacb60(0x8d,0x19,0x17e,0x19a)+enter+enter+(_0x41308f(0x4af,0x455,0x500,0x564)+'patkan\x20*')+_0x57eae7+('*\x20batu\x20dan'+'\x20')+_0x1fba4a+'\x20kayu'+enter+enter+(_0x41308f(0x724,0x6ce,0x67d,0x61f)+_0xdacb60(-0x7,0x8b,0x4f,0x1f)+_0xdacb60(0x9b,-0x88,0x13b,-0x3d)+'\x20ketik\x20')+prefix+_0xdacb60(0x234,0x351,0x226,0x2b0),'©\x20'+ownername,bbbb,[{'buttonId':_0x41308f(0x5c9,0x681,0x6e5,0x642),'buttonText':{'displayText':_0xfc05d7[_0x41308f(0x58b,0x633,0x5d7,0x6f0)]},'type':_0xfc05d7['sSVeS']}],_0x98fd7f);},-0x4*0x339+-0x2263+0x3aff*0x1),setTimeout(()=>{function _0x58964c(_0xb9775d,_0x52102b,_0x1edc24,_0x5a6408){return _0x385207(_0xb9775d,_0x52102b-0x118,_0x1edc24-0x10c,_0x52102b- -0x17a);}const _0x100511={'DdjDj':function(_0x15af9c,_0x50f027){return _0x15af9c(_0x50f027);}};function _0x5e93fd(_0x3c752d,_0x5daf4b,_0xb195f4,_0x3c9baa){return _0x529d2f(_0x3c752d-0x1e2,_0x3c752d-0x42,_0xb195f4-0x66,_0xb195f4);}_0x100511[_0x5e93fd(0x21d,0x20b,0x139,0x2f6)](reply,_0x5e93fd(0x3d9,0x4c2,0x2cf,0x4f2)+_0x58964c(0x194,0x71,0x3f,0x82)+_0x5e93fd(0x262,0x227,0x385,0x32c)+_0x58964c(0x34,-0xc3,0x5b,-0x76));},-0x3*0x5a6+0x9*-0x425+0x363f);}else{const _0xb65c49={};_0xb65c49[_0x385207(0x1a1,0xd2,0x1bb,0xad)]=_0x385207(0x187,0xbd,0x231,0x1f6),seae=await getBuffer(_0x385207(0x7f,0xc1,0x1da,0x13b)+_0x385207(0x21e,0x52,0x1e6,0xec)+'ile/168577'+'96fab2ccb6'+'cffc2.jpg',_0xb65c49),tesk='*PILIH\x20WIL'+'AYAH\x20YANG\x20'+'INGIN\x20KAMU'+'\x20JELAJAHI*'+_0x385207(-0x1,0xdf,0x82,0x105)+_0x529d2f(0x351,0x31d,0x287,0x390)+_0x385207(0x7b,0x105,0x11b,0x2d)+_0x385207(-0x29,0x73,-0x116,-0x1b)+_0x529d2f(0x9f,0x14c,0x2c,0x15d)+_0x385207(-0x1d,0xd4,0x180,0x80)+'bil\x20Woods\x0a'+'🟢\x20Chiltawa'+_0x385207(0x12c,0x156,0x1c2,0xc7)+'imingstall'+_0x385207(0x236,0xd4,0x1ff,0x130)+_0x385207(0xcf,0xa2,0x141,0x1a)+_0x529d2f(0x2e3,0x2ca,0x324,0x1eb)+'xample\x20:\x0a-'+'\x20'+prefix+(_0x529d2f(0x2d3,0x369,0x34c,0x281)+_0x529d2f(0x1cf,0x250,0x25d,0x263)+_0x385207(0x2ae,0xcc,0xbf,0x1d1)+_0x529d2f(0x2e5,0x261,0x2ec,0x183)+_0x385207(0xd1,-0x6b,-0xdc,-0x2e)+_0x529d2f(0x140,0x26d,0x200,0x178)+_0x529d2f(0x3b8,0x2ac,0x193,0x1db)+_0x529d2f(0x2a9,0x245,0x1ec,0x2de)+_0x529d2f(0x2d9,0x1aa,0x2d6,0x133)),alpha[_0x385207(0x173,0x125,0x21a,0x1b4)+'e'](from,seae,image,{'thumbnail':seae,'quoted':mek,'caption':tesk});}}}}}}}await gameAdd(sender,glimit);break;case _0x529d2f(0x2f7,0x2c2,0x352,0x19c):const _0x56b575={};_0x56b575[_0x385207(0x25a,0x5e,0x152,0x17c)+'t']=_0x385207(-0x44,0x8d,0x9,0x85)+'t';const _0x12a999={};_0x12a999['buttonId']=_0x385207(0xcb,0x120,0x39,0x116),_0x12a999[_0x529d2f(0x294,0x158,0x272,0x260)]=_0x56b575,_0x12a999[_0x385207(0x127,0xcd,0x1cc,0x1e8)]=0x1;if(isGame(sender,isPremium,isCreator,isOwner,gcounttuser,glimit))return sendButMessage(from,lang[_0x529d2f(0x1db,0x282,0x170,0x270)](prefix),'©\x20'+ownername,[_0x12a999]);const _0x1de4bb={};_0x1de4bb[_0x529d2f(0x39c,0x313,0x25b,0x1e0)+'t']=_0x529d2f(0x122,0x212,0xdc,0x32b);const _0x4b78a8={};_0x4b78a8['buttonId']=_0x385207(-0xaa,-0xee,0x7f,-0x17),_0x4b78a8[_0x385207(-0xbc,-0xf7,-0x23,-0x3f)]=_0x1de4bb,_0x4b78a8[_0x385207(0x308,0x236,0x240,0x1e8)]=0x1;if(!isEventon)return sendButMessage(from,lang[_0x529d2f(0x236,0x272,0x268,0x301)](prefix),'©\x20'+ownername,[_0x4b78a8]);setTimeout(()=>{const _0x459a1e={'NcwJm':function(_0x36d2ea,_0x4c02c5){return _0x36d2ea*_0x4c02c5;},'mWeLl':function(_0x4d4b70,_0x553ca8){return _0x4d4b70*_0x553ca8;},'EOGGY':function(_0x28dfaa,_0x5cafe8,_0x5b7ab5){return _0x28dfaa(_0x5cafe8,_0x5b7ab5);},'HJThq':function(_0x14ca33,_0x364a94,_0x1e817a){return _0x14ca33(_0x364a94,_0x1e817a);},'dZHSs':function(_0x1b4a6c,_0x505aa6){return _0x1b4a6c(_0x505aa6);}},_0x79fb37=Math[_0x57c6f3(0x3e1,0x3bf,0x373,0x3ae)](Math[_0x57c6f3(0x374,0x3ac,0x367,0x400)]()*(-0x17e2+0x36*-0x31+0x376*0xa)),_0x1a8456=Math[_0x42f38e(0x9b,0xae,0x137,0x16a)](_0x459a1e['NcwJm'](Math[_0x57c6f3(0x31d,0x3ac,0x339,0x3bd)](),0x5*0x3b4+0x1ba*0x7+0x2*-0xf3e)),_0x5c5e86=Math['ceil'](_0x459a1e[_0x42f38e(0x1a2,0x109,0x10d,0x24)](Math[_0x42f38e(0x12f,0x1c7,0x124,0x25)](),-0x80f+-0x1*0x45a+0xc73*0x1));_0x459a1e['EOGGY'](addStone,sender,_0x79fb37);function _0x42f38e(_0x8211f7,_0x2eeb56,_0x527a87,_0x47e59e){return _0x529d2f(_0x8211f7-0x11b,_0x527a87- -0x68,_0x527a87-0x10f,_0x47e59e);}addCoal(sender,_0x1a8456),_0x459a1e[_0x57c6f3(0x576,0x4b7,0x388,0x511)](addOre,sender,_0x5c5e86);function _0x57c6f3(_0x3116c8,_0x2f4390,_0x10be45,_0x2a7780){return _0x385207(_0x3116c8,_0x2f4390-0x31,_0x10be45-0x99,_0x2f4390-0x3b7);}_0x459a1e['dZHSs'](reply,'*Congratul'+'ation\x20🎊*'+enter+enter+('\x20kamu\x20mend'+'apatkan\x20*')+_0x79fb37+_0x57c6f3(0x48a,0x3f8,0x300,0x44f)+_0x1a8456+(_0x42f38e(0x3d9,0x37c,0x337,0x37a)+_0x57c6f3(0x4fe,0x48c,0x355,0x462))+_0x5c5e86+_0x57c6f3(0x455,0x3f4,0x2be,0x381));},0x28d*-0x4+-0x270c+0x79f*0x8),setTimeout(()=>{function _0x33a50e(_0x3eb0e4,_0x1b479a,_0x2f90fd,_0x496b35){return _0x529d2f(_0x3eb0e4-0x192,_0x3eb0e4-0x15e,_0x2f90fd-0x18c,_0x2f90fd);}function _0x5cd1d5(_0x46c4bd,_0x404d71,_0xfb116b,_0x2e9e98){return _0x385207(_0x404d71,_0x404d71-0x136,_0xfb116b-0xa4,_0xfb116b- -0xc7);}reply(_0x5cd1d5(-0x2e,0x4f,-0x4a,0xd3)+'ambang,\x20si'+_0x5cd1d5(-0x30,0x1a9,0xe0,0x1fa)+_0x5cd1d5(-0x166,-0xb6,-0xa2,-0x1a8));},-0x6b6*-0x1+-0xc95+0x5df*0x1),await gameAdd(sender,glimit);break;case _0x529d2f(0x203,0x1d2,0x237,0x2bc):const _0x133778={};_0x133778[_0x385207(0x171,0x7c,0x253,0x17c)+'t']=_0x529d2f(0x143,0x21c,0x330,0x274)+'t';const _0x125fdf={};_0x125fdf['buttonId']='limit',_0x125fdf['buttonText']=_0x133778,_0x125fdf['type']=0x1;if(isGame(sender,isPremium,isCreator,isOwner,gcounttuser,glimit))return sendButMessage(from,lang[_0x385207(0x173,0x1e,0x74,0xeb)](prefix),'©\x20'+ownername,[_0x125fdf]);const _0x3bb4bc={};_0x3bb4bc[_0x385207(0x9b,0x188,0xc2,0x17c)+'t']=_0x385207(0x87,-0x8b,0x69,0x7b);const _0xc7cc76={};_0xc7cc76[_0x529d2f(0x25b,0x144,0x21d,0x197)]=_0x529d2f(0xf0,0x180,0x277,0x20b),_0xc7cc76['buttonText']=_0x3bb4bc,_0xc7cc76[_0x385207(0x24e,0x119,0x114,0x1e8)]=0x1;if(!isEventon)return sendButMessage(from,lang['event'](prefix),'©\x20'+ownername,[_0xc7cc76]);setTimeout(()=>{const _0x3d6c86={'jFcZP':function(_0xd89c5f,_0x3fd68c){return _0xd89c5f*_0x3fd68c;},'AGoAQ':function(_0x41c0d9,_0x25fbdd,_0xebb641){return _0x41c0d9(_0x25fbdd,_0xebb641);},'ciCQD':function(_0x4e30c5,_0x448388){return _0x4e30c5(_0x448388);}};function _0x549eb5(_0xba99a8,_0x3e55a0,_0x401768,_0x371c9d){return _0x385207(_0x371c9d,_0x3e55a0-0x21,_0x401768-0x10f,_0x401768-0x21a);}const _0x3b42c1=Math['ceil'](_0x3d6c86[_0x1354a3(0xb3,0x19,0x7f,0x2e)](Math[_0x549eb5(0x1e9,0x329,0x20f,0x217)](),-0x19d1+-0x21*0x1d+0x1da2));_0x3d6c86[_0x549eb5(0x24a,0x30f,0x36b,0x2ca)](addKayu,sender,_0x3b42c1);function _0x1354a3(_0x4d9404,_0x3e6e6f,_0x2ccca8,_0x337b5d){return _0x529d2f(_0x4d9404-0x138,_0x337b5d- -0x20b,_0x2ccca8-0x2c,_0x2ccca8);}_0x3d6c86['ciCQD'](reply,'*Congratul'+'ation\x20🎊*'+enter+enter+(_0x549eb5(0x246,0x39e,0x2a4,0x243)+_0x549eb5(0x4de,0x421,0x3f1,0x3b6))+_0x3b42c1+(_0x549eb5(0x1dd,0xcc,0x1f2,0x324)+_0x549eb5(0x31b,0x2e0,0x2be,0x3ab)));},-0x67a+-0x1*-0x3d1+-0x4cb*-0x3),setTimeout(()=>{const _0x4609fe={};function _0x334e70(_0x239190,_0x1e7c03,_0x1f911a,_0x1235a0){return _0x385207(_0x1235a0,_0x1e7c03-0x198,_0x1f911a-0x7d,_0x1e7c03-0x20b);}_0x4609fe[_0x5a9bd7(0x97,0xed,0x1b4,0x274)]=_0x334e70(0x1d2,0x288,0x268,0x273)+_0x5a9bd7(-0x1a,-0x8f,-0x3a,-0x149)+_0x5a9bd7(0x1be,0x154,0x18c,0x1df)+'ggu...';const _0x1ac99c=_0x4609fe;function _0x5a9bd7(_0x5f25fd,_0x5cf85c,_0x9f364f,_0x4327cf){return _0x529d2f(_0x5f25fd-0xfa,_0x9f364f- -0x1b2,_0x9f364f-0xa4,_0x4327cf);}reply(_0x1ac99c['clZJk']);},0xf8+0x4d8+-0x5d0),await gameAdd(sender,glimit);break;case'goplanet':const _0x4a237c={};_0x4a237c[_0x385207(0x1ab,0x1e8,0x99,0x17c)+'t']=_0x385207(0x91,0xa7,0x2f,0x85)+'t';const _0x25cc8e={};_0x25cc8e[_0x385207(-0xdf,-0x35,-0x12e,-0x53)]='limit',_0x25cc8e[_0x385207(0xe,-0x8,-0x8,-0x3f)]=_0x4a237c,_0x25cc8e[_0x385207(0x1eb,0x24c,0x29f,0x1e8)]=0x1;if(isGame(sender,isPremium,isCreator,isOwner,gcounttuser,glimit))return sendButMessage(from,lang['limitg'](prefix),'©\x20'+ownername,[_0x25cc8e]);const _0x4a1540={};_0x4a1540[_0x385207(0x20e,0x272,0x14a,0x17c)+'t']=_0x529d2f(0x138,0x212,0x17d,0x11e);const _0xb2aabb={};_0xb2aabb[_0x529d2f(0x17b,0x144,0xd,0x161)]=_0x385207(-0x48,0x115,0x58,-0x17),_0xb2aabb[_0x529d2f(0xfa,0x158,0x12c,0x10e)]=_0x4a1540,_0xb2aabb[_0x385207(0x1af,0x1aa,0x24b,0x1e8)]=0x1;if(!isEventon)return sendButMessage(from,lang['event'](prefix),'©\x20'+ownername,[_0xb2aabb]);setTimeout(()=>{function _0x25e8f5(_0x13235a,_0x306d76,_0xec2b93,_0x5a40b7){return _0x385207(_0x13235a,_0x306d76-0x12c,_0xec2b93-0x83,_0x5a40b7-0x260);}const _0x45365f={'VGzTw':'merkurius','Ckgkl':'mars','EPOHZ':_0x25e8f5(0x40b,0x33f,0x312,0x35e),'yduXQ':'saturnus','aftwM':'neptunus','dMqjG':_0x25e8f5(0x362,0x204,0x2be,0x269),'UBOXQ':function(_0x5b5d28,_0xa0b88f){return _0x5b5d28*_0xa0b88f;},'IBnGo':function(_0x309c99,_0x3acb59){return _0x309c99(_0x3acb59);}};function _0x155ee1(_0x50d730,_0x749072,_0x57cfcd,_0x3177f7){return _0x385207(_0x57cfcd,_0x749072-0x56,_0x57cfcd-0xcb,_0x3177f7-0x243);}const _0x1fbb56=Math[_0x25e8f5(0x20c,0x256,0x22c,0x268)](Math[_0x25e8f5(0x2c7,0x35a,0x344,0x255)]()*(-0x22c2+0x35b*0xb+-0x1c3)),_0x5bfe31=[_0x45365f[_0x25e8f5(0x22d,0x2ba,0x1cf,0x27f)],_0x25e8f5(0x454,0x371,0x2e6,0x3c8),_0x45365f[_0x155ee1(0x2d7,0x2d2,0x282,0x392)],_0x45365f[_0x25e8f5(0x4a7,0x4fa,0x3eb,0x3f0)],_0x45365f['yduXQ'],_0x45365f[_0x25e8f5(0x2f1,0x431,0x4df,0x3df)],_0x45365f[_0x155ee1(0x273,0x344,0x2e2,0x297)]],_0x4ce222=_0x5bfe31[Math['floor'](_0x45365f[_0x25e8f5(0x44c,0x268,0x27f,0x36f)](Math[_0x25e8f5(0x14b,0x149,0x27f,0x255)](),_0x5bfe31[_0x25e8f5(0x3d2,0x2dc,0x35f,0x296)]))];addPlanet(sender,_0x1fbb56),_0x45365f[_0x155ee1(0x3e8,0x36c,0x24b,0x334)](reply,_0x155ee1(0x469,0x292,0x3e6,0x37c)+'ation\x20🎊*'+enter+enter+(_0x155ee1(0x3dc,0x25b,0x26d,0x2cd)+_0x155ee1(0x350,0x44b,0x51b,0x41a))+_0x1fbb56+(_0x25e8f5(0x390,0x50b,0x511,0x3e2)+'ia\x20dari\x20*')+_0x4ce222+(_0x25e8f5(0x111,0x2f7,0x162,0x23d)+_0x25e8f5(0x332,0x1af,0x124,0x1fc)));},-0x5d8*-0x2+-0x1df0+0x1df8),setTimeout(()=>{const _0x433c67={'PLced':function(_0x4484c7,_0x2981d0){return _0x4484c7(_0x2981d0);},'WJEPv':_0xe0d389(0x3e6,0x310,0x4b9,0x2f3)+_0x3c689b(-0x35,-0x55,0xb1,0x125)+_0xe0d389(0x1d6,0x21f,0x232,0x187)+_0xe0d389(0x3a4,0x456,0x3bb,0x3c9)+_0xe0d389(0x2df,0x22e,0x3ce,0x380)};function _0x3c689b(_0x3666ae,_0xa22426,_0x51c322,_0x3fb2c2){return _0x529d2f(_0x3666ae-0x24,_0x51c322- -0x10e,_0x51c322-0x105,_0xa22426);}function _0xe0d389(_0x3830e7,_0x3785a6,_0xa4d610,_0x374e02){return _0x529d2f(_0x3830e7-0x1e3,_0x3830e7-0x4f,_0xa4d610-0x151,_0x374e02);}_0x433c67[_0xe0d389(0x21f,0x311,0x283,0x21c)](reply,_0x433c67[_0x3c689b(0x221,0x122,0x1e2,0x238)]);},0x10c1+0x1a9c+-0x2b5d),await gameAdd(sender,glimit);break;case'jualbahank'+_0x529d2f(0x30b,0x333,0x333,0x41e):const _0x3be3be={};_0x3be3be[_0x529d2f(0x403,0x313,0x30a,0x402)+'t']=_0x529d2f(0x264,0x21c,0x16d,0x2eb)+'t';const _0x3f2767={};_0x3f2767[_0x529d2f(0x17e,0x144,0x21a,0x260)]=_0x385207(0x19d,0x1ca,0x5e,0x116),_0x3f2767['buttonText']=_0x3be3be,_0x3f2767[_0x529d2f(0x369,0x37f,0x277,0x458)]=0x1;if(isGame(sender,isPremium,isCreator,isOwner,gcounttuser,glimit))return sendButMessage(from,lang[_0x529d2f(0x3a2,0x282,0x14e,0x2c4)](prefix),'©\x20'+ownername,[_0x3f2767]);const _0x5bfae1={};_0x5bfae1[_0x529d2f(0x3aa,0x313,0x39f,0x32e)+'t']=_0x385207(0x148,-0x39,-0x11,0x7b);const _0x3c7a60={};_0x3c7a60['buttonId']='event\x20on',_0x3c7a60['buttonText']=_0x5bfae1,_0x3c7a60['type']=0x1;if(!isEventon)return sendButMessage(from,lang[_0x385207(0x118,0x192,0xa,0xdb)](prefix),'©\x20'+ownername,[_0x3c7a60]);buayar=body['slice'](-0xbf4+-0xe13*0x1+0x1a17);const hargakimia=0x185b+0x11*0x1f2+-0x3585*0x1,dapetin=buayar*hargakimia;if(getBertualangPlanet(sender)<=-0x218f+0x20c+0x1f84)return reply(_0x385207(-0x4b,-0x9,-0x8c,-0x43)+pushname+(_0x385207(-0xae,-0x101,-0xa4,-0x65)+'k\x20punya\x20ba'+_0x529d2f(0x20e,0x1ca,0x1ca,0x2a0)));getBertualangPlanet(sender)>=-0x279*0xb+0x1*-0x185b+0x338f&&(jualbahankimia(sender,buayar),addKoinUser(sender,dapetin),await reply(_0x385207(0x111,0x170,0xd5,0x46)+_0x385207(-0x83,0x6e,0x49,-0x30)+_0x385207(0x1bb,0x25d,0x2b3,0x1d3)+enter+enter+(_0x529d2f(0x2f3,0x25b,0x1ff,0x1c0)+_0x529d2f(0x3f5,0x34c,0x40f,0x416)+'ijual:*\x20')+buayar+enter+(_0x385207(0x2b4,0x250,0x297,0x1d9)+'pat:*\x20')+dapetin+enter+enter+(_0x385207(0x14c,0x22d,0x127,0x146)+_0x529d2f(0x9e,0x1c7,0x2a1,0x207))+getBertualangPlanet(sender)+enter+(_0x385207(0x33,0x189,0x90,0x5a)+_0x529d2f(0x128,0x14d,0x4c,0xe6))+checkATMuser(sender)+enter+enter+('Penjualan\x20'+'berhasil\x20d'+'engan\x20nomo'+_0x529d2f(0x5b,0x195,0xf8,0x6d)+_0x529d2f(0x2a3,0x216,0x12b,0x251)+_0x385207(-0xa6,0x6d,0x4a,-0x49))));await gameAdd(sender,glimit);break;case _0x385207(0x10,0x2b,-0x89,0x3c)+_0x385207(0x186,0x19f,0x151,0x19c):teks=_0x385207(0x121,0x1c8,0xf6,0xc4)+_0x529d2f(0x204,0x1ed,0x281,0x147)+'ang\x20didapa'+_0x385207(0x1d,0x7c,0x15a,0xf4)+pushname+(_0x385207(0x1e6,0x51,0x10b,0x17a)+_0x385207(0x28d,0x162,0xe2,0x185))+getBertualangPlanet(sender)+'_*';const _0x4ae072={};_0x4ae072[_0x529d2f(0x243,0x357,0x231,0x2c2)]=mek,alpha[_0x385207(0xc1,0x82,0xf0,0x1b4)+'e'](from,teks,text,_0x4ae072);break;case _0x529d2f(0x493,0x376,0x4aa,0x417):case'casino':const _0x3e3d1b={};_0x3e3d1b[_0x385207(0x2a4,0xbf,0x8c,0x17c)+'t']=_0x385207(-0xa3,0xa,0x107,0x85)+'t';const _0x3e598e={};_0x3e598e['buttonId']=_0x385207(0x219,0x54,0xf2,0x116),_0x3e598e['buttonText']=_0x3e3d1b,_0x3e598e[_0x529d2f(0x35a,0x37f,0x316,0x4ac)]=0x1;if(isGame(sender,isPremium,isCreator,isOwner,gcounttuser,glimit))return sendButMessage(from,lang[_0x529d2f(0x38d,0x282,0x206,0x379)](prefix),'©\x20'+ownername,[_0x3e598e]);const _0x243e48={};_0x243e48[_0x529d2f(0x2cc,0x313,0x3c5,0x210)+'t']=_0x529d2f(0xdf,0x212,0x327,0x185);const _0x54bdd5={};_0x54bdd5[_0x385207(-0x124,-0x124,-0x4a,-0x53)]=_0x529d2f(0x29e,0x180,0x146,0x13e),_0x54bdd5['buttonText']=_0x243e48,_0x54bdd5[_0x529d2f(0x484,0x37f,0x40c,0x3d1)]=0x1;if(!isEventon)return sendButMessage(from,lang['event'](prefix),'©\x20'+ownername,[_0x54bdd5]);cas=q;if(checkATMuser(sender)<cas)return reply(_0x529d2f(0x343,0x21e,0x1d9,0x1ef)+'dak\x20mencuk'+_0x529d2f(0x25d,0x2e2,0x3b3,0x237)+_0x385207(0x49,0x15f,0xd5,0x161)+'judi');if(args['length']<0x29*-0x56+-0x1719+-0x760*-0x5)return reply('Mau\x20taruha'+'n\x20berapa');if(isNaN(cas))return reply(_0x385207(0x98,-0x67,0x47,0x75)+_0x385207(0x276,0x277,0x61,0x18f));const resg=[_0x385207(0xd3,0x2b4,0x2c2,0x1d8)+_0x385207(-0xc6,0x38,0xe3,0x26),'Kamu\x20KALAH'+'!!'];bayar=confirmATM(sender,cas),setTimeout(()=>{const _0x116819={'JaBcx':function(_0x2224eb,_0xbb4621){return _0x2224eb*_0xbb4621;},'hWQDO':function(_0x22d6db,_0xdd659a){return _0x22d6db+_0xdd659a;},'guZcv':function(_0x3a5310,_0x5476fa){return _0x3a5310==_0x5476fa;},'eUcNU':function(_0x7a5867,_0x43b4ce){return _0x7a5867(_0x43b4ce);},'tAfha':'Kamu\x20KALAH'+'!!','gVjwK':function(_0xa30678,_0x521251,_0x4fd7aa){return _0xa30678(_0x521251,_0x4fd7aa);},'kNjBq':_0x35b64b(-0x2e0,-0x24e,-0x2c1,-0x22f)};function _0x59d968(_0x21608b,_0x5581a3,_0x4b0076,_0x5f0825){return _0x529d2f(_0x21608b-0x60,_0x21608b-0x5a,_0x4b0076-0xa8,_0x5581a3);}const _0x5ccd60=Math['ceil'](_0x116819[_0x59d968(0x255,0x216,0x2b7,0x269)](Math[_0x35b64b(-0x1b5,-0x202,-0x193,-0x14b)](),-0x20e0+-0xef7+0x2fd9)),_0x570069=_0x116819[_0x35b64b(-0x1f0,-0x13b,-0x13c,-0x15f)](cas,-0x6c2+-0x3*0x5fb+-0x1*-0x18b3),_0x1cedb0=resg[Math['floor'](Math['random']()*resg['length'])];function _0x35b64b(_0xd5a9eb,_0x422483,_0x335b89,_0x40156b){return _0x529d2f(_0xd5a9eb-0x160,_0x422483- -0x38e,_0x335b89-0x64,_0x40156b);}if(_0x116819[_0x59d968(0x34f,0x462,0x317,0x2ab)](_0x1cedb0,_0x35b64b(-0x90,-0x1f,-0x78,0x14)+_0x35b64b(-0x181,-0x1d1,-0x151,-0x1f3)))addKoinUser(sender,_0x570069),_0x116819[_0x35b64b(-0x13c,-0xa4,-0x29,-0x1c0)](reply,_0x59d968(0x32a,0x3d3,0x1ef,0x446)+_0x35b64b(-0x1a7,-0x19b,-0x176,-0x1db)+enter+enter+('Kamu\x20memen'+_0x59d968(0x218,0x336,0x1d8,0x1f0)+_0x59d968(0x2b7,0x2c3,0x388,0x246)+_0x59d968(0x244,0x152,0x171,0x112))+_0x570069+'_*'+enter+enter+('Kumpulkan\x20'+_0x59d968(0x2a5,0x1e2,0x2b6,0x3bf)+_0x59d968(0x1d1,0x1ae,0x200,0x106)+_0x59d968(0x207,0x1e8,0x17c,0xcb)));else _0x116819['guZcv'](_0x1cedb0,_0x116819['tAfha'])?(_0x116819['gVjwK'](confirmATM,sender,cas),reply('Kamu\x20kalah'+_0x59d968(0x39b,0x3c7,0x3a7,0x425)+_0x59d968(0x38e,0x252,0x42a,0x31c)+'ng\x20sebesar'+'\x20'+cas)):reply(_0x116819[_0x59d968(0x259,0x210,0x334,0x284)]);},-0xd17+-0x2014+0x1*0x38e3),setTimeout(()=>{const _0x556606={'GrDFL':function(_0x347b31,_0x33a5d6){return _0x347b31(_0x33a5d6);}};function _0x1adc03(_0x573582,_0x930e4a,_0x4037af,_0x4ddfcf){return _0x385207(_0x573582,_0x930e4a-0x40,_0x4037af-0xa5,_0x4037af-0x30d);}function _0x4b28b8(_0x4c51ef,_0x49cca7,_0x453cac,_0x2051cb){return _0x529d2f(_0x4c51ef-0x111,_0x453cac-0x246,_0x453cac-0x108,_0x4c51ef);}_0x556606['GrDFL'](reply,_0x4b28b8(0x35f,0x4c4,0x43a,0x348)+_0x1adc03(0x381,0x388,0x495,0x376));},-0x85a*0x2+-0x1*0x17fb+0x1*0x28af),await gameAdd(sender,glimit);break;case _0x529d2f(0x2eb,0x33f,0x385,0x2a1):case _0x385207(0x195,0x19d,0x10c,0xf6):case _0x385207(0x2e0,0x2fd,0x1bf,0x203):{try{pp_userb=await alpha['getProfile'+_0x385207(-0x1d,-0xce,-0xaf,0x2f)](sender);}catch{pp_userb='https://i.'+_0x529d2f(0x23e,0x1b0,0x292,0x153)+_0x529d2f(0x1ed,0x284,0x39b,0x201)+'bb87660.pn'+'g';}let pp_userz=await getBuffer(pp_userb);inventory='\x0a🗃️\x20*USER\x20I'+_0x529d2f(0x5e,0x143,0x7c,0x237)+'🗃️\x20\x0a\x0a🎢\x20*COA'+_0x385207(0xd5,0x149,0xdb,0x128)+getMiningcoal(sender)+(_0x529d2f(0x282,0x1a7,0x172,0x116)+_0x385207(0x6a,0x2d,0xba,0x4a))+getMiningstone(sender)+(_0x385207(0x271,0x28e,0x268,0x172)+_0x385207(-0xbd,-0xdc,-0x13e,-0x4))+getMiningore(sender)+(_0x385207(-0x40,0x6d,-0xef,-0x45)+_0x385207(-0x20,0xea,0xb3,0x10b))+getMiningingot(sender)+(_0x529d2f(0x44e,0x378,0x28a,0x49e)+':\x20')+getNebangKayu(sender)+(_0x385207(0x85,0x65,0x13,0xfd)+':\x20')+getMancingIkan(sender)+(_0x529d2f(0x222,0x25c,0x1bb,0x2c5)+_0x529d2f(0x358,0x390,0x25b,0x3ae)+'ame\x20untuk\x20'+_0x529d2f(0x2f5,0x2f4,0x31a,0x35a)+'n\x20lebih\x20ba'+'nyak\x20inven'+'tory'),alpha[_0x385207(0x187,0x28f,0x117,0x1b4)+'e'](from,pp_userz,image,{'thumbnail':Buffer[_0x385207(0xbf,0x1c1,0x233,0x1ab)](-0xa7f*0x1+-0x9*0x28a+-0x2159*-0x1),'quoted':mek,'caption':inventory});}break;case'kodebahasa':kodenyab='Kode\x20bahas'+'a\x0a\x20\x0a\x20\x09Code'+'\x20\x20\x20\x20\x20\x20\x20Bah'+'asa\x0a\x20\x20\x20\x20sq'+'\x20\x20\x20\x20\x20\x20\x20\x20Al'+_0x385207(-0xb0,0x73,0xb8,-0x4f)+_0x385207(0x47,0x43,-0x8f,0x59)+'\x20Arabic\x0a\x20\x20'+_0x529d2f(0x20d,0x15e,0x28e,0x275)+_0x529d2f(0x11b,0x156,0x143,0x255)+_0x529d2f(0x42b,0x32d,0x26b,0x307)+_0x385207(0x1b0,0x255,0x173,0x1e7)+_0x385207(0x247,0x9b,0x1b8,0x111)+'\x20\x20\x20\x20\x20\x20\x20Chi'+_0x385207(0xa9,-0x88,0x167,0x43)+_0x529d2f(0x1fc,0x218,0x102,0x313)+_0x385207(0x2f3,0x1b5,0x299,0x1ca)+_0x529d2f(0x2d9,0x328,0x1ff,0x263)+_0x385207(0x10f,-0xb6,-0x149,-0x24)+_0x385207(0x113,0xe2,0x104,0x125)+_0x385207(-0x87,0xd1,-0x22,-0xa)+_0x529d2f(0x311,0x394,0x3f2,0x3de)+'Chinese\x20(C'+'antonese)\x0a'+_0x529d2f(0x22d,0x2db,0x3e8,0x34f)+_0x529d2f(0x112,0x1cf,0xf5,0x15c)+'an\x0a\x20\x20\x20\x20cs\x20'+'\x20\x20\x20\x20\x20\x20\x20Cze'+_0x385207(0xf1,0x2e3,0xcf,0x1ec)+'\x20\x20\x20\x20\x20\x20\x20Dan'+_0x385207(-0x7,0x1c5,0x26,0xfb)+_0x385207(0x55,0xdc,-0x71,0x65)+_0x529d2f(0x9b,0x13d,0x92,0x31)+'\x20\x20\x20\x20\x20\x20\x20\x20En'+'glish\x0a\x20\x20\x20\x20'+_0x529d2f(0x2ca,0x335,0x205,0x372)+_0x529d2f(0x1cb,0x23c,0x220,0x221)+_0x529d2f(0x6a,0x130,0x1a1,0x248)+_0x385207(-0xa3,0xcf,-0x4c,0x61)+_0x385207(-0xe,0x1eb,0x1aa,0xe3)+_0x529d2f(0x262,0x139,0xb6,0x75)+_0x385207(0x228,0x195,0x16f,0x1a6)+_0x529d2f(0x1b6,0x1af,0x231,0xbe)+'\x20\x20\x20English'+_0x385207(0x52,0x56,0x59,-0x58)+'tates)\x0a\x20\x20\x20'+_0x529d2f(0x2af,0x380,0x39e,0x479)+_0x385207(0x18a,0x186,0x32,0xa8)+_0x529d2f(0x19f,0x237,0x1e0,0x24b)+_0x385207(0x2c2,0x2d0,0x2c8,0x19f)+_0x529d2f(0x2fe,0x375,0x252,0x3e5)+'\x20\x20\x20\x20\x20\x20\x20Fre'+_0x385207(0xe,0x131,0x51,0x106)+_0x385207(0xc5,0x21e,0x236,0x110)+'rman\x0a\x20\x20\x20\x20e'+_0x385207(0x2a1,0xde,0x124,0x1a5)+_0x385207(-0x53,0x2f,0x12b,0x14)+_0x385207(-0xef,0x172,0x53,0x49)+_0x529d2f(0x32d,0x37c,0x361,0x2f7)+'ole\x0a\x20\x20\x20\x20hi'+_0x529d2f(0x37c,0x2d4,0x3e1,0x3f7)+_0x385207(0x7c,0xbb,0x37,-0x60)+_0x385207(0xec,0x28,0x262,0x15a)+_0x529d2f(0x2bd,0x1b3,0x15f,0x17c)+'\x20\x20is\x20\x20\x20\x20\x20\x20'+_0x385207(0x3a,-0x131,-0x152,-0x29)+_0x385207(0x21,-0xe,0x76,-0x11)+_0x529d2f(0x1ed,0x19d,0x182,0x10d)+_0x385207(0xa2,0x27,-0x16,0x55)+_0x529d2f(0x2f6,0x1de,0x302,0x121)+_0x385207(0x8f,-0x5,0x105,0x92)+'\x20\x20\x20ja\x20\x20\x20\x20\x20'+_0x529d2f(0x241,0x2c9,0x2a2,0x3b5)+'e\x0a\x20\x20\x20\x20ko\x20\x20'+_0x385207(-0xa,0x12d,-0x26,0x9f)+'an\x0a\x20\x20\x20\x20la\x20'+_0x385207(0x12f,0x14,0x161,0x99)+_0x529d2f(0x1d7,0x2f7,0x2ea,0x36f)+_0x385207(0xda,0x44,0xb4,0x99)+_0x385207(0x8d,0xdf,0x9d,0xaa)+'k\x20\x20\x20\x20\x20\x20\x20\x20M'+_0x385207(-0x4a,0xcc,0x139,0x50)+'\x20\x20\x20\x20no\x20\x20\x20\x20'+_0x385207(0xc1,0x50,0xdc,0x13f)+'ian\x0a\x20\x20\x20\x20pl'+_0x385207(0xad,-0x46,0xd9,-0x33)+_0x385207(0x1d9,0x1b1,0x1e4,0x1cd)+_0x529d2f(0x2be,0x360,0x294,0x3d1)+_0x529d2f(0x206,0x306,0x334,0x273)+_0x529d2f(0x20,0x12b,0x19b,0x10c)+_0x385207(-0x30,0xcc,0x194,0xd1)+_0x529d2f(0x390,0x29a,0x2c8,0x1f2)+_0x529d2f(0xa1,0x161,0x4e,0x11d)+_0x385207(0x2a9,0x21d,0xf3,0x1d0)+_0x529d2f(0x1b5,0x155,0x204,0x279)+_0x529d2f(0x281,0x315,0x38e,0x2dc)+'\x20Russian\x0a\x20'+_0x385207(0x130,0x14f,0x6e,0x1b)+_0x529d2f(0x38d,0x2fd,0x233,0x277)+_0x385207(-0x15b,-0x150,0x15,-0x4e)+(_0x529d2f(0x140,0x1ac,0x1b3,0x134)+_0x529d2f(0x3ee,0x2d3,0x1a9,0x276)+_0x529d2f(0x344,0x330,0x269,0x2fe)+'ish\x0a\x20\x20\x20\x20es'+'-es\x20\x20\x20\x20\x20Sp'+_0x529d2f(0x27b,0x1b8,0xda,0x24d)+_0x529d2f(0xdb,0x1b7,0x11c,0x23e)+_0x529d2f(0xd2,0x19c,0xfb,0x9c)+_0x385207(0x35,0x4,0xf1,0xbe)+_0x529d2f(0x12b,0x18e,0x218,0xea)+_0x529d2f(0x17f,0x138,0x268,0xdb)+_0x385207(0x20e,0x296,0x2cb,0x202)+'ili\x0a\x20\x20\x20\x20sv'+_0x529d2f(0x2a5,0x189,0x181,0x2a2)+_0x529d2f(0x2fc,0x30a,0x2e8,0x427)+_0x529d2f(0x129,0x22b,0x164,0x196)+'Tamil\x0a\x20\x20\x20\x20'+_0x385207(-0x87,-0xdd,-0xfb,-0x2a)+_0x385207(-0x5b,-0x9a,0xff,0x42)+_0x385207(0x1e6,-0x5c,0x10c,0xd7)+_0x385207(-0x151,-0x46,0x24,-0x18)+'\x20vi\x20\x20\x20\x20\x20\x20\x20'+'\x20Vietnames'+'e\x0a\x20\x20\x20\x20cy\x20\x20'+_0x529d2f(0x366,0x2c5,0x2dd,0x250)+_0x385207(0xc5,0x15e,-0x12,0x4b)),reply(kodenyab);break;case _0x385207(0x229,0x1ab,-0x1a,0x122):const _0x18d910={};_0x18d910[_0x385207(0xbf,0x1ef,0x188,0x1c0)]=mek;if(args[_0x385207(0x11b,-0xef,-0x86,0x36)]<-0x2*0x5b8+-0x3*-0x115+-0x1*-0x832)return alpha[_0x385207(0xba,0x248,0x2bb,0x1b4)+'e'](from,'Kode\x20bahas'+_0x529d2f(0x3c5,0x302,0x2f6,0x256)+_0x385207(0x24,0x1dd,0x1c,0xde),text,_0x18d910);kodenya=['af','sq','ar','hy','ca','zh',_0x529d2f(0x10a,0x146,0x248,0xb),'zh-tw',_0x385207(-0x91,-0x8e,-0xc0,0x6f),'hr','cs','da','nl','en','en-au',_0x529d2f(0x1bd,0x240,0x1ab,0x1f5),_0x385207(-0x76,0xdf,0x140,0x6e),'eo','fi','fr','de','el','ht','hi','hu','is','id','it','ja','ko','la','lv','mk','no','pl','pt',_0x529d2f(0x196,0x269,0x1b7,0x26b),'ro','ru','sr','sk','es',_0x385207(0x32,0xd3,0xa9,0xdc),_0x529d2f(0x2c7,0x1a8,0x9a,0x9b),'sw','sv','ta','th','tr','vi','cy'];try{const gtts=require('./lib/gtts')(args[-0x25ce+-0x16*0x6e+0x2f42]),_0x213ae1={};_0x213ae1[_0x529d2f(0x40d,0x357,0x440,0x3c7)]=mek;if(args[_0x529d2f(0x305,0x1cd,0x1e4,0x2dc)]<-0x1141*-0x1+-0x1*0x165a+0x51b)return alpha[_0x385207(0xd7,0x209,0x10e,0x1b4)+'e'](from,_0x529d2f(0x2b0,0x17e,0x116,0x161)+'na\x20om',text,_0x213ae1);dtt=body['slice'](0x21b9+-0x2f*-0x73+-0x36cd*0x1),ranm=getRandom(_0x385207(0x191,0x6d,0x1a6,0x1a1)),rano=getRandom('.ogg'),dtt['length']>-0x8*-0x3d5+-0x1*0xeef+0x19*-0x89?reply(_0x385207(0xdd,0x168,0x329,0x1fb)+_0x529d2f(0x271,0x308,0x229,0x3d8)+'m'):gtts['save'](ranm,dtt,function(){function _0x14096b(_0x1f24e4,_0x377796,_0x733e97,_0x483b67){return _0x385207(_0x483b67,_0x377796-0x189,_0x733e97-0x1de,_0x1f24e4-0x4b7);}const _0xb1002d={'LwsmW':function(_0x29a5c7,_0x1ccf7e){return _0x29a5c7 instanceof _0x1ccf7e;},'kouCv':function(_0x1c00a0,_0x2f1fcb){return _0x1c00a0===_0x2f1fcb;},'YmePg':_0x14096b(0x5d7,0x4ad,0x6ae,0x664),'PJzRn':_0x577bad(-0xd8,-0x110,-0x1e7,-0xa7),'AKiFB':function(_0x242809,_0x23a3ab){return _0x242809(_0x23a3ab);},'RwSVs':'Gagal\x20om:('};function _0x577bad(_0x34e827,_0x38876a,_0x5f053e,_0x36f475){return _0x385207(_0x5f053e,_0x38876a-0x118,_0x5f053e-0x1a7,_0x34e827- -0x262);}exec('ffmpeg\x20-i\x20'+ranm+('\x20-ar\x2048000'+_0x577bad(-0x8d,0xa9,-0x5f,-0x87)+_0x14096b(0x471,0x43b,0x4b4,0x38e))+rano,_0x27ee66=>{function _0x2ecb0f(_0x526ce9,_0xeb510c,_0x7cca53,_0x1bd376){return _0x577bad(_0x1bd376-0x179,_0xeb510c-0x8c,_0x526ce9,_0x1bd376-0x1d6);}function _0x1b63ac(_0x2d2ab2,_0x49f2de,_0x5aa140,_0xcdec33){return _0x577bad(_0x5aa140-0x4e6,_0x49f2de-0xa2,_0x2d2ab2,_0xcdec33-0x155);}if(_0xb1002d[_0x1b63ac(0x378,0x24e,0x2cc,0x254)](_0xb1002d[_0x2ecb0f(0x5a,0x66,0xad,0xfd)],_0xb1002d[_0x2ecb0f(0x10,0x109,0x148,0xfd)])){const _0x544891=_0xb1002d['PJzRn']['split']('|');let _0x42e457=-0x68*-0x12+0x2cc+-0xa1c;while(!![]){switch(_0x544891[_0x42e457++]){case'0':if(_0x27ee66)return _0xb1002d['AKiFB'](reply,_0xb1002d['RwSVs']);continue;case'1':buff=fs['readFileSy'+'nc'](rano);continue;case'2':const _0x211df9={};_0x211df9[_0x2ecb0f(0x165,0x212,-0x35,0xd7)]=mek,_0x211df9['ptt']=!![],alpha[_0x2ecb0f(0x99,0x7e,0x28,0xcb)+'e'](from,buff,audio,_0x211df9);continue;case'3':fs[_0x1b63ac(0x34e,0x3bc,0x3f1,0x4dc)](ranm);continue;case'4':fs[_0x2ecb0f(-0xa2,0xf0,0xae,0x84)](rano);continue;}break;}}else{let _0x106522=_0xb1002d[_0x2ecb0f(-0x1c3,-0x53,-0xfc,-0xfb)](_0x153ceb,_0x28f2fe)?_0x3a72aa:new _0x50e4b0(_0x28cdf3(_0x242fb8));return[_0x106522[_0x2ecb0f(-0x94,0x27,-0x119,-0x115)](_0x35860a[_0x2ecb0f(-0xcd,0x14e,0xeb,0x33)]),_0x106522];}});});}catch{reply(_0x529d2f(0x11a,0x222,0x29b,0x1d8)+'ggunaan\x20#t'+_0x529d2f(0x21c,0x150,0x1ba,0xd6)+_0x529d2f(0x235,0x191,0x1ae,0xd7)+_0x529d2f(0x277,0x2d1,0x225,0x196)+_0x529d2f(0x23f,0x30b,0x23a,0x3a4)+_0x385207(0x1b1,0x2c5,0x18a,0x1e4)+_0x385207(0xb7,0x95,0x189,0xdd)+'ode\x20bahasa'+_0x385207(-0xfc,-0x16f,-0x142,-0x37)+_0x385207(0xcb,-0x52,0x102,0x2c));}break;case _0x385207(-0xac,-0x137,0x63,-0xc):{const _0x103ea7={};_0x103ea7[_0x385207(0x1a5,0x258,0x96,0x17c)+'t']=_0x385207(0x1a4,0x93,0x55,0x85)+'t';const _0x859ddb={};_0x859ddb[_0x529d2f(0x24d,0x144,0x23b,0x1a6)]=_0x529d2f(0x37d,0x2ad,0x349,0x38b),_0x859ddb[_0x529d2f(0xba,0x158,0x291,0x25a)]=_0x103ea7,_0x859ddb['type']=0x1;if(isLimit(sender,isPremium,isCreator,isOwner,limitawal,limit))return sendButMessage(from,lang['limit'](prefix),'©\x20'+ownername,[_0x859ddb]);if(!q)return fakegroup(_0x529d2f(0x34d,0x37a,0x48a,0x357)+'a?');var halzmal=q;const tod=await fetchJson(_0x385207(0x5b,0x4b,0x136,0xab)+'i.popcat.x'+_0x529d2f(0x31d,0x373,0x29a,0x237)+_0x529d2f(0x48d,0x3a0,0x2cc,0x421)+halzmal);var {username,full_name,biography,posts,reels,followers,following,private,verified,profile_pic}=tod;const txt=_0x529d2f(0x19d,0x168,0x228,0xaf)+_0x529d2f(0x308,0x1e1,0x214,0x10b)+username+(_0x385207(0xaf,0xf9,0x247,0x14e)+_0x529d2f(0x2e1,0x305,0x287,0x22e))+full_name+(_0x529d2f(0x27c,0x202,0x266,0x134)+_0x385207(-0x4e,-0x88,0x14f,0x35))+followers+(_0x529d2f(0x231,0x200,0x21b,0x1e1)+_0x529d2f(0x28b,0x235,0x16f,0x239))+following+_0x529d2f(0x11a,0x227,0x1f8,0x115)+posts+(_0x385207(0x156,0x17d,0x17a,0x98)+'ht\x20:\x20')+reels+(_0x385207(0x4a,0x51,0x1b4,0x152)+'\x20:\x20')+private+(_0x385207(0x14f,0x25d,0x11b,0x1b2)+_0x385207(0xd5,0x1d7,0x1fd,0xe1))+verified+(_0x529d2f(0x11e,0x1fd,0x2a6,0x242)+_0x385207(-0x4b,0xf6,0xf,0x76))+biography;sendFileFromUrl(m[_0x385207(0x25d,0xa9,0x142,0x192)],profile_pic,txt,mek),await limitAdd(sender,limit);}break;case _0x529d2f(0x1be,0x280,0x304,0x2ed):case _0x529d2f(0x13e,0x1c1,0x116,0x161)+'k':case _0x385207(0xde,0x37,0x263,0x163):{if(args[_0x529d2f(0x2ae,0x1cd,0xd0,0x2f4)]<0x192a+-0x2*0xbdd+-0x16f)return reply(_0x385207(-0xc,0x112,-0x80,0x8c)+'ntah\x20*'+prefix+(_0x529d2f(0x140,0x1dc,0x1bd,0x2d2)+_0x385207(0xf3,0x215,0x119,0xff)));reply(lang[_0x529d2f(0x279,0x2ef,0x1b8,0x3e0)]());let y=await fetchJson(_0x529d2f(0x2ac,0x242,0x188,0x36b)+'i.github.c'+_0x385207(0xa4,0x1c6,0x129,0xc2)+q),ppgt=await getBuffer(y[_0x385207(0xcb,-0x7a,0x15c,0x32)]),textt=_0x529d2f(0x230,0x1f2,0x2ac,0xc4)+'THUB\x20STALK'+_0x529d2f(0x299,0x1cb,0x2e9,0x17d)+enter+enter+(_0x529d2f(0x472,0x384,0x45f,0x276)+_0x529d2f(0x1c9,0x1e1,0x234,0x12e))+y['login']+enter+_0x529d2f(0xde,0x142,0x18a,0x2c)+y['name']+enter+_0x385207(0x2a,0xea,0xcb,0xc9)+y['id']+enter+(_0x385207(0xfc,0x18,0x10a,0x7)+':\x20')+y[_0x385207(0xb,0x1e,-0x199,-0x6e)]+enter+(_0x529d2f(0x8a,0x12c,0xd,-0xa)+_0x385207(-0x80,0x14c,0xf7,0x73))+y[_0x385207(0x1ce,0x20,0x108,0x157)]+enter+(_0x385207(0x103,0x1c5,0x191,0xa6)+_0x385207(0x4d,0xbb,0x25,-0x5b))+y[_0x529d2f(0x2c0,0x385,0x2e4,0x34c)]+enter+_0x529d2f(0x4f,0x128,0x18d,0x1b8)+y[_0x529d2f(0x299,0x37f,0x42c,0x3c5)]+enter+(_0x385207(0xbf,0x1f8,0x10b,0x1d4)+':\x20')+y[_0x385207(0x13b,0x139,0xd3,0x12)]+enter+_0x529d2f(0x396,0x35e,0x401,0x411)+y[_0x385207(0x1ca,0x224,0x4e,0x177)]+enter+(_0x385207(-0x9,-0x11,-0x5d,0x29)+'\x20:\x20')+y[_0x385207(-0x10c,0x71,0x91,-0x15)]+enter+_0x529d2f(0xf8,0x153,0x2c,0xaa)+y['email']+enter+'💌\x20Bio\x20:\x20'+y[_0x529d2f(0x1e7,0x1fa,0x1d6,0x219)]+enter+(_0x529d2f(0x1b1,0x2b0,0x39d,0x25f)+_0x385207(0x152,0x97,0x10,0xb5)+'\x20')+y[_0x529d2f(0x23f,0x32e,0x34b,0x350)+_0x529d2f(0x214,0x22a,0x157,0x10e)]+enter+(_0x529d2f(0x21c,0x26f,0x172,0x1ae)+_0x385207(0xc2,0x5c,-0x181,-0x4c))+y[_0x529d2f(0x402,0x30c,0x41a,0x2e9)+'os']+enter+('🌍\x20Public\x20G'+'its\x20:\x20')+y[_0x529d2f(0x338,0x320,0x2fa,0x28b)+'ts']+enter+(_0x385207(0x166,0x179,0x11e,0x1c8)+':\x20')+moment(y['created_at'])['tz']('Asia/Jakar'+'ta')[_0x385207(-0x136,-0x116,-0x15,0x3)]('id')['format'](_0x529d2f(0x27f,0x1f9,0x1c9,0x18e)+_0x529d2f(0x2c7,0x33b,0x454,0x22a))+enter+(_0x385207(0x18d,0x119,0xab,0x112)+'\x20')+moment(y[_0x385207(-0x21,0x14b,-0x8,0x108)])['tz'](_0x529d2f(0x409,0x38e,0x3d2,0x38c)+'ta')['locale']('id')['format'](_0x385207(-0x68,0x49,-0x68,0x62)+'D/MM/YYYY')+enter+('➿\x20Url\x20:\x20ht'+_0x385207(-0x94,0x1a1,0x92,0xa7)+_0x529d2f(0x2c0,0x22c,0x1c0,0x1bc))+q;const _0x1a9624={};_0x1a9624['caption']=textt,_0x1a9624[_0x529d2f(0x3a7,0x357,0x40c,0x2d1)]=mek,alpha[_0x529d2f(0x2a1,0x34b,0x2fd,0x44a)+'e'](from,ppgt,image,_0x1a9624),await limitAdd(sender,limit);}break;case _0x529d2f(0x476,0x377,0x249,0x30a):const _0x228ab4={};_0x228ab4['productId']=_0x529d2f(0x17c,0x15c,0x1ce,0x178)+_0x529d2f(0x343,0x2a4,0x37d,0x3ab);const _0x3aa4fc={};_0x3aa4fc[_0x385207(-0x14e,0xa0,-0x98,-0x68)]=_0x385207(-0x168,-0x168,0xcc,-0x48)+_0x385207(-0xb7,-0xe6,-0xb1,-0x14),_0x3aa4fc[_0x385207(0xba,0x1a9,0x19d,0xc1)]=[_0x228ab4];const _0x91e300={};_0x91e300[_0x529d2f(0x275,0x2e1,0x3f7,0x38c)]=_0x385207(0xe5,0x126,0xc8,0x11b)+_0x385207(0x292,0x10a,0x11d,0x18b);const _0x212063={};_0x212063['title']='ORDER\x20BOT\x20'+_0x529d2f(0x3a0,0x2c8,0x37d,0x270)+'AN',_0x212063[_0x385207(0x190,0x1b0,0x187,0xc1)]=[_0x91e300];const _0x4778b2={};_0x4778b2[_0x385207(0x33,0x2b,0x185,0x14a)]=_0x385207(-0x5,0x69,0x1c2,0x121)+_0x529d2f(0x2a9,0x243,0x1e5,0x193);const _0x53ed08={};_0x53ed08[_0x385207(0x5b,-0x5f,-0x14b,-0x68)]=_0x385207(0x8,0x150,0x216,0x101)+'OT\x20VIA\x20HER'+_0x529d2f(0x261,0x2ec,0x2d3,0x266),_0x53ed08['products']=[_0x4778b2];const _0x4d3989={};_0x4d3989[_0x529d2f(0x24c,0x357,0x2dd,0x39e)]=mek,lisduct=await alpha['prepareMes'+'sageFromCo'+_0x529d2f(0x1ca,0x17d,0x79,0x1a1)](from,{'listMessage':{'title':_0x529d2f(0x205,0x14f,0x2b,0x9f)+'RMANEN','description':_0x385207(-0x25,0xf6,0x1b9,0xaf)+'ang\x20bot\x20mu'+_0x385207(0x10f,0x4a,0xff,0xcf)+_0x385207(0x114,0xee,0xa2,0xa3)+_0x385207(0x6c,-0x4,-0x68,-0x27)+'\x20sekarang\x20'+_0x529d2f(0x33c,0x204,0x2d8,0x2de)+_0x385207(0xe5,-0x20,-0x31,0xb)+'adi\x20owner\x20'+_0x529d2f(0x106,0x203,0x1fe,0x2d9)+_0x385207(-0x161,-0x38,-0x9e,-0x3c)+_0x529d2f(0x270,0x1c5,0x1f3,0x94)+'\x20sediakan\x20'+_0x529d2f(0x3a8,0x2ed,0x308,0x276)+_0x529d2f(0x50,0x166,0x142,0x28d)+_0x529d2f(0x2f2,0x1f5,0x246,0x1b5)+_0x529d2f(0x3e5,0x363,0x400,0x232)+_0x385207(0x5c,0x6d,-0x41,0xc8)+'ekali\x20bisa'+_0x385207(-0x59,0xae,-0x1c,0x52)+_0x385207(0x1ab,0x5f,0x150,0x15b),'buttonText':'','listType':'PRODUCT_LI'+'ST','productListInfo':{'productSections':[_0x3aa4fc,_0x212063,_0x53ed08],'headerImage':{'jpegThumbnail':fs[_0x385207(0x9b,0x1d9,0x223,0x187)+'nc'](_0x529d2f(0x26a,0x310,0x240,0x253)+thumbnail)},'businessOwnerJid':_0x385207(-0xbd,0x66,-0x2e,0x1e)+_0x385207(0x92,0x94,0x1a5,0xef)+'tsapp.net'},'footerText':'Jika\x20Minat'+_0x529d2f(0x280,0x1e5,0x281,0x21e)+'Lihat\x20Item'}},_0x4d3989);const _0x4c31b8={};_0x4c31b8[_0x385207(0x53,0x3c,-0xd3,0x57)]=!![],alpha['relayWAMes'+_0x529d2f(0x170,0x1b9,0x1bd,0x15a)](lisduct,_0x4c31b8);break;case _0x529d2f(0x2bc,0x276,0x2ad,0x384):{const flamingtext=_0x385207(0x27e,0x10,0x1f9,0x14c)+_0x529d2f(0x157,0x1a4,0xf0,0x25c)+'text.com/n'+_0x529d2f(0x28c,0x293,0x2d4,0x2f5)+_0x529d2f(0x3cd,0x38a,0x4b4,0x3b4)+_0x385207(-0x2d,0x17f,0xfb,0x84)+_0x385207(0x198,0x1dd,-0x41,0xc3)+_0x385207(0x63,0x109,0x8e,0xc)+_0x385207(0x139,0x83,0x21a,0x164)+_0x385207(0xcc,0xd6,0x27f,0x150)+'&scaleWidt'+'h=800&scal'+_0x385207(0x15f,0x96,0x1cf,0x1ad)+_0x529d2f(0x2f8,0x1fe,0x13d,0x134)+_0x529d2f(0x23b,0x198,0x2d4,0x268)+_0x385207(0x1d6,0x1b3,-0x20,0x104)+'fillTextPa'+'ttern=Warn'+_0x385207(-0x17,0xa8,-0x68,-0x6d);if(isGroup)return reply(_0x385207(-0xfb,0x92,0x8,0x3f)+'te\x20chat');this[_0x385207(0x10b,0x114,0x16f,0xdf)]=this[_0x529d2f(0x2aa,0x276,0x358,0x357)]?this[_0x385207(0x50,-0x17,-0x30,0xdf)]:{},anonymousloc=await getBuffer(flamingtext+(_0x529d2f(0x347,0x24f,0x265,0x335)+_0x385207(0x129,0x242,0x173,0x1a2)));const _0x4335fd={};_0x4335fd['displayTex'+'t']=_0x385207(0xfb,0x128,0x160,0x126);const _0x83151d={};_0x83151d[_0x529d2f(0x21a,0x144,0x38,0x1bb)]=_0x529d2f(0x2f5,0x1c8,0x1ef,0xbb),_0x83151d[_0x529d2f(0x18b,0x158,0x137,0x21b)]=_0x4335fd,_0x83151d['type']=0x1;const _0xc93ee8={};_0xc93ee8[_0x385207(0x172,0x153,0x58,0x17c)+'t']='START';const _0x3973fe={};_0x3973fe[_0x529d2f(0x26e,0x144,0xd0,0x194)]=_0x385207(0xb0,0x9a,-0x71,-0x69),_0x3973fe[_0x385207(0x24,-0x6a,-0x152,-0x3f)]=_0xc93ee8,_0x3973fe['type']=0x1;const _0x5d5a2a={};_0x5d5a2a[_0x529d2f(0x344,0x357,0x383,0x3cf)]=mek,sendButLocation(from,'Welcome\x20To'+_0x529d2f(0x19c,0x181,0x84,0x1aa)+_0x529d2f(0x119,0x1a5,0xc8,0xac)+prefix+(_0x529d2f(0x294,0x211,0x213,0x18a)+'arch\x20Partn'+'er\x0a')+prefix+(_0x529d2f(0x485,0x34d,0x253,0x3db)+_0x529d2f(0x312,0x248,0x25c,0x2b6))+prefix+(_0x385207(0x1d5,0x132,0x1ac,0x1c6)+_0x385207(0x179,0x211,0x247,0x1f4)+'r'),_0x385207(0x129,0xff,0x2da,0x1b0)+'t\x20'+botname+_0x529d2f(0x23a,0x31a,0x382,0x333),anonymousloc,[_0x83151d,_0x3973fe],_0x5d5a2a);}break;case'keluar':case _0x529d2f(0x39b,0x26a,0x34f,0x1f0):{if(isGroup)return reply(_0x529d2f(0x1ad,0x1d6,0x147,0x22c)+_0x385207(0x6,-0x12b,-0x14,0x2));this[_0x385207(-0x5e,0x1a4,0x182,0xdf)]=this['anonymous']?this[_0x385207(0x102,0xea,0x145,0xdf)]:{};let room=Object['values'](this['anonymous'])[_0x385207(0x150,-0x5,0xcb,0x10e)](_0x593c03=>_0x593c03[_0x529d2f(0x38d,0x354,0x33b,0x3bf)](m[_0x529d2f(0x491,0x381,0x346,0x32c)]));if(!room){const _0x2b099c={};_0x2b099c[_0x385207(0x166,0x163,0xd5,0x17c)+'t']=_0x385207(0x79,-0x9,0x71,0x2b);const _0x14ddfc={};_0x14ddfc[_0x385207(-0x41,-0xf1,-0x60,-0x53)]=_0x385207(0x4,0x14,0xf,-0x69),_0x14ddfc[_0x385207(0x6e,0x94,-0x4b,-0x3f)]=_0x2b099c,_0x14ddfc[_0x529d2f(0x3eb,0x37f,0x2d6,0x34e)]=0x1;const _0x4ec2e7={};_0x4ec2e7[_0x385207(0x2b9,0x1e6,0x122,0x1c0)]=mek,await sendButMessage(from,'Kamu\x20Tidak'+_0x529d2f(0x300,0x2b6,0x189,0x35a)+_0x385207(-0x2d,0x101,-0x8b,-0x16)+_0x385207(0x16a,0x25,0x1e3,0xe4)+_0x385207(0x115,0x17e,0x14a,0x1fa)+'Untuk\x20Star'+_0x385207(0x61,0x1d7,0x63,0x12d)+_0x385207(0x262,0x26d,0x13b,0x178),_0x529d2f(0x448,0x347,0x242,0x3ed)+'t\x20'+botname+'\x202021',[_0x14ddfc],_0x4ec2e7);throw![];}const _0x37f39c={};_0x37f39c[_0x529d2f(0x2dd,0x313,0x315,0x36a)+'t']=_0x385207(-0xe9,-0xe9,0xd8,0x2b);const _0x421e48={};_0x421e48[_0x529d2f(0x22a,0x144,0x277,0xa6)]=_0x385207(0x2,0x30,-0x41,-0x69),_0x421e48['buttonText']=_0x37f39c,_0x421e48[_0x385207(0x249,0x23d,0x198,0x1e8)]=0x1;const _0x46ba94={};_0x46ba94[_0x385207(0x2a4,0xe1,0xc4,0x1c0)]=mek,sendButMessage(from,_0x529d2f(0x3be,0x2e4,0x2d4,0x389)+_0x385207(0x12b,0x294,0x17a,0x201)+'Dari\x20Sesi\x20'+_0x529d2f(0x253,0x24f,0x210,0x15d)+_0x385207(0x84,0x7e,0xb9,0x147),_0x529d2f(0x378,0x347,0x339,0x3c1)+'t\x20'+botname+_0x385207(0xbe,0x1cd,0x1fa,0x11d),[_0x421e48],_0x46ba94);let other=room[_0x385207(0x263,0x6d,0x1db,0x145)](m[_0x385207(0xf8,0x1c0,0x21b,0x1ea)]);const _0xd2a95={};_0xd2a95[_0x385207(0x21a,0x1e2,0x226,0x17c)+'t']=_0x529d2f(0x194,0x1c2,0x1aa,0x180);const _0x1d976c={};_0x1d976c['buttonId']='start',_0x1d976c['buttonText']=_0xd2a95,_0x1d976c[_0x385207(0x218,0x1d0,0x23b,0x1e8)]=0x1;const _0x508d0a={};_0x508d0a[_0x385207(0x115,0xd4,0x206,0x1c0)]=mek;if(other)await sendButMessage(other,_0x529d2f(0x10f,0x20e,0x19d,0x211)+'\x20meninggal'+_0x529d2f(0x117,0x219,0x192,0x218),_0x529d2f(0x427,0x347,0x3f8,0x20f)+'t\x20'+botname+_0x529d2f(0x250,0x2b4,0x294,0x31c),[_0x1d976c],_0x508d0a);delete this[_0x529d2f(0x309,0x276,0x2aa,0x1c9)][room['id']];if(command==='leave')break;}case _0x385207(0x18d,0x2d7,0xec,0x1a3):case _0x529d2f(0x51,0x12e,0x247,0x1f4):{if(isGroup)return reply(_0x529d2f(0xc3,0x1d6,0xac,0x284)+_0x385207(-0x8d,-0x10d,-0xbd,0x2));this['anonymous']=this[_0x529d2f(0x296,0x276,0x28b,0x1ee)]?this[_0x385207(0x74,0x1ed,0xf3,0xdf)]:{};if(Object[_0x385207(0x227,0x3d,0x1c6,0x167)](this[_0x529d2f(0x25b,0x276,0x229,0x250)])[_0x385207(0x221,0x246,0x105,0x10e)](_0x34d2fd=>_0x34d2fd['check'](m['sender']))){const _0x223ed2={};_0x223ed2[_0x385207(0x224,0x283,0x1a4,0x17c)+'t']=_0x385207(0x2e3,0x2a5,0x13c,0x1af);const _0x2c1822={};_0x2c1822[_0x385207(-0x28,-0x7b,-0x157,-0x53)]='leave',_0x2c1822[_0x385207(-0xd2,0xfd,-0x74,-0x3f)]=_0x223ed2,_0x2c1822[_0x385207(0xb3,0x199,0x314,0x1e8)]=0x1;const _0x567dce={};_0x567dce[_0x385207(0xcc,0x2c5,0x2bf,0x1c0)]=mek,await sendButMessage(from,_0x385207(0x1,0x19b,0x56,0x88)+_0x385207(0x7,0x19f,0x1a2,0x11f)+_0x529d2f(0x287,0x181,0x158,0x215)+_0x385207(0x136,0x7b,0x184,0x1ac),_0x529d2f(0x3e8,0x347,0x3f4,0x261)+'t\x20'+botname+'\x202021',[_0x2c1822],_0x567dce);throw![];}let room=Object[_0x529d2f(0x390,0x2fe,0x2a6,0x429)](this['anonymous'])[_0x529d2f(0x249,0x2a5,0x322,0x336)](_0x4c21ff=>_0x4c21ff[_0x529d2f(0x2b3,0x2a0,0x352,0x3b9)]==='WAITING'&&!_0x4c21ff[_0x529d2f(0x248,0x354,0x3b7,0x21a)](m[_0x385207(0x2ef,0x149,0x22f,0x1ea)]));if(room){const _0x4a7d4c={};_0x4a7d4c[_0x385207(0x2a3,0xf4,0x16e,0x17c)+'t']=_0x385207(0xa7,0x141,0x222,0x1af);const _0x2f443a={};_0x2f443a[_0x385207(-0xe0,0x81,-0x2b,-0x53)]='leave',_0x2f443a[_0x385207(-0x46,-0x33,-0xe6,-0x3f)]=_0x4a7d4c,_0x2f443a[_0x529d2f(0x338,0x37f,0x46b,0x3aa)]=0x1;const _0xebb229={};_0xebb229[_0x529d2f(0x441,0x313,0x326,0x444)+'t']=_0x529d2f(0x2a7,0x20b,0x318,0xdb);const _0x2bca0b={};_0x2bca0b[_0x529d2f(0x258,0x144,0x118,0x1e2)]=_0x385207(0x4a,0x34,0x269,0x13e),_0x2bca0b['buttonText']=_0xebb229,_0x2bca0b[_0x385207(0xeb,0x10e,0x19b,0x1e8)]=0x1;const _0x39d2a7={};_0x39d2a7[_0x529d2f(0x44d,0x357,0x460,0x2b9)]=mek,await sendButMessage(room['a'],_0x529d2f(0x1c2,0x18a,0x8a,0x115)+_0x385207(0x2c6,0x2c0,0x2ae,0x1f8)+'🎭','©\x20Copyrigh'+'t\x20'+botname+_0x529d2f(0x28d,0x2b4,0x211,0x1b3),[_0x2f443a,_0x2bca0b],_0x39d2a7),room['b']=m[_0x529d2f(0x282,0x381,0x48f,0x391)],room[_0x385207(0x6e,0x27,-0x7,0x109)]='CHATTING';const _0x1948ba={};_0x1948ba['displayTex'+'t']=_0x529d2f(0x3d0,0x346,0x441,0x27e);const _0x51cfd7={};_0x51cfd7[_0x529d2f(0x235,0x144,0x149,0x21a)]=_0x385207(0x9b,0x72,-0x42,0xd3),_0x51cfd7[_0x529d2f(0x67,0x158,0x12b,0x1d7)]=_0x1948ba,_0x51cfd7[_0x385207(0x23a,0xdc,0x1e1,0x1e8)]=0x1;const _0x780563={};_0x780563[_0x529d2f(0x25e,0x313,0x332,0x3a9)+'t']=_0x529d2f(0x1ec,0x20b,0x1ca,0x1ce);const _0x42c64d={};_0x42c64d[_0x529d2f(0x16d,0x144,0x172,0xd6)]=_0x529d2f(0x3fe,0x2d5,0x204,0x37e),_0x42c64d[_0x529d2f(0x74,0x158,0x22d,0xad)]=_0x780563,_0x42c64d[_0x385207(0x163,0x1d3,0x138,0x1e8)]=0x1;const _0x4867e0={};_0x4867e0['quoted']=mek,await sendButMessage(room['b'],_0x529d2f(0x153,0x18a,0x7a,0x288)+_0x385207(0x101,0x1f9,0x236,0x1f8)+'🎭','©\x20Copyrigh'+'t\x20'+botname+_0x529d2f(0x17a,0x2b4,0x1d8,0x18d),[_0x51cfd7,_0x42c64d],_0x4867e0);}else{let id=+new Date();this[_0x385207(0x205,0x6,0x158,0xdf)][id]={'id':id,'a':m[_0x529d2f(0x355,0x381,0x484,0x32c)],'b':'','state':_0x529d2f(0x45b,0x34e,0x237,0x464),'check':function(_0x1813d5=''){function _0x2a46c1(_0x3cc5c7,_0x45125a,_0x256eb9,_0x2aba3a){return _0x529d2f(_0x3cc5c7-0x44,_0x2aba3a- -0x41,_0x256eb9-0xf0,_0x256eb9);}return[this['a'],this['b']][_0x2a46c1(0x9b,0xb0,0x1c8,0xf9)](_0x1813d5);},'other':function(_0x33872e=''){const _0x5c53fd={};function _0x4adf09(_0x5e51ff,_0x4e7407,_0x39bfb9,_0xbd9aab){return _0x385207(_0x4e7407,_0x4e7407-0x107,_0x39bfb9-0x198,_0x39bfb9-0x510);}_0x5c53fd[_0x4adf09(0x524,0x5b2,0x51a,0x59d)]=function(_0xca8ab7,_0x3706ec){return _0xca8ab7===_0x3706ec;};function _0x206074(_0x529c66,_0x34a7db,_0x57ca90,_0x40bd4b){return _0x529d2f(_0x529c66-0x190,_0x34a7db- -0x1f3,_0x57ca90-0x1cc,_0x57ca90);}_0x5c53fd[_0x4adf09(0x644,0x53f,0x63c,0x6e1)]=function(_0x3ededf,_0xe905a9){return _0x3ededf===_0xe905a9;};const _0x5cfb6b=_0x5c53fd;return _0x5cfb6b[_0x4adf09(0x4b5,0x5fa,0x51a,0x3fe)](_0x33872e,this['a'])?this['b']:_0x5cfb6b[_0x206074(0x6c,0xd0,0x10,0xc6)](_0x33872e,this['b'])?this['a']:'';}};const _0x1891ff={};_0x1891ff[_0x385207(0x86,0x1c1,0x1e0,0x17c)+'t']='LEAVE';const _0x4103cf={};_0x4103cf[_0x385207(-0xbe,-0x117,-0x81,-0x53)]=_0x385207(-0xc,0x1d3,0x165,0xd3),_0x4103cf['buttonText']=_0x1891ff,_0x4103cf[_0x385207(0x27e,0x1e4,0x120,0x1e8)]=0x1;const _0x586c0a={};_0x586c0a[_0x385207(0x1a0,0xd9,0x146,0x1c0)]=mek,await sendButMessage(m[_0x529d2f(0x292,0x329,0x28f,0x224)],_0x529d2f(0x340,0x2b1,0x26f,0x353)+'u\x20Partner_',_0x529d2f(0x2b9,0x347,0x3b7,0x41b)+'t\x20'+botname+_0x529d2f(0x20f,0x2b4,0x34f,0x2f9),[_0x4103cf],_0x586c0a);}break;}case _0x385207(0xbe,-0xc7,0x79,0x70):case _0x529d2f(0x273,0x2d5,0x3ed,0x20e):case _0x529d2f(0x221,0x323,0x2c3,0x305):{if(isGroup)return reply('Fitur\x20Tida'+'k\x20Dapat\x20Di'+_0x529d2f(0x256,0x299,0x2f4,0x374)+_0x385207(0x196,0x1b9,0x1c7,0x17d));this[_0x385207(0x50,0x183,0x17b,0xdf)]=this[_0x529d2f(0x375,0x276,0x299,0x17c)]?this[_0x529d2f(0x1fd,0x276,0x34d,0x25c)]:{};let romeo=Object[_0x385207(0x164,0x1d4,0xd8,0x167)](this['anonymous'])[_0x529d2f(0x305,0x2a5,0x2c6,0x389)](_0x18cd98=>_0x18cd98[_0x529d2f(0x48f,0x354,0x453,0x2e0)](m[_0x529d2f(0x357,0x381,0x376,0x450)]));if(!romeo){const _0x4b3b9d={};_0x4b3b9d[_0x529d2f(0x260,0x313,0x1fb,0x305)+'t']=_0x385207(0x7b,0x3e,-0xe9,0x2b);const _0x4fd71c={};_0x4fd71c['buttonId']=_0x529d2f(0xec,0x12e,0x83,0x32),_0x4fd71c[_0x529d2f(0xa7,0x158,0x21d,0x207)]=_0x4b3b9d,_0x4fd71c[_0x385207(0x144,0x220,0x177,0x1e8)]=0x1;const _0x355fda={};_0x355fda[_0x529d2f(0x263,0x357,0x27a,0x438)]=mek,await sendButMessage(from,'Kamu\x20Tidak'+_0x385207(0x1c8,0x11,0x242,0x11f)+_0x385207(0x51,0x58,-0x12,-0x16)+_0x529d2f(0x34d,0x27b,0x321,0x1a6)+_0x529d2f(0x2cf,0x391,0x2a5,0x3bc)+_0x385207(-0x198,0xad,-0x14b,-0x6a)+_0x529d2f(0x18e,0x2c4,0x275,0x295)+_0x529d2f(0x388,0x30f,0x3fd,0x3de),'©\x20Copyrigh'+'t\x20'+botname+'\x202021',[_0x4fd71c],_0x355fda);throw![];}let other=romeo['other'](m[_0x385207(0x12c,0x2ff,0xc8,0x1ea)]);const _0x14333b={};_0x14333b[_0x529d2f(0x30e,0x313,0x33c,0x227)+'t']=_0x529d2f(0xd8,0x1c2,0x2ae,0x1ba);const _0xc2e00b={};_0xc2e00b['buttonId']=_0x529d2f(0x24b,0x12e,0x61,0x22b),_0xc2e00b[_0x385207(-0xd1,0x41,-0x10c,-0x3f)]=_0x14333b,_0xc2e00b[_0x529d2f(0x29e,0x37f,0x291,0x482)]=0x1;const _0x29b922={};_0x29b922[_0x529d2f(0x24e,0x357,0x247,0x3a8)]=mek;if(other)sendButMessage(other,_0x529d2f(0x1e6,0x20e,0x2c4,0xfc)+_0x385207(0x1d9,0x79,0x2ab,0x195)+_0x385207(-0xb3,0x9d,0x1ab,0x82),'©\x20Copyrigh'+'t\x20\x20'+botname+_0x529d2f(0x2a7,0x2b4,0x2b0,0x178),[_0xc2e00b],_0x29b922);delete this['anonymous'][romeo['id']];let room=Object[_0x529d2f(0x3ab,0x2fe,0x27a,0x2d8)](this[_0x385207(-0xa,0x21c,0x5c,0xdf)])[_0x385207(0x10,0x1fd,0x1dd,0x10e)](_0x5d9983=>_0x5d9983[_0x529d2f(0x249,0x2a0,0x38e,0x20e)]===_0x529d2f(0x452,0x34e,0x41c,0x3b7)&&!_0x5d9983[_0x385207(0x197,0x241,0x1c0,0x1bd)](m[_0x385207(0x164,0x287,0x109,0x1ea)]));if(room){const _0x17d016={};_0x17d016[_0x529d2f(0x316,0x313,0x2be,0x41a)+'t']=_0x529d2f(0x3ca,0x346,0x3b5,0x2a5);const _0x3f6f27={};_0x3f6f27['buttonId']=_0x385207(0xd5,0x1e8,-0x1e,0xd3),_0x3f6f27[_0x385207(-0x29,-0x6b,-0x122,-0x3f)]=_0x17d016,_0x3f6f27[_0x385207(0xf1,0x109,0x231,0x1e8)]=0x1;const _0x186939={};_0x186939[_0x385207(0x1e6,0x73,0x158,0x17c)+'t']='SKIP';const _0x4a47a6={};_0x4a47a6[_0x385207(-0x15,0x80,0xcb,-0x53)]=_0x385207(0x71,0x129,0x196,0x13e),_0x4a47a6[_0x385207(-0x90,-0x141,-0x95,-0x3f)]=_0x186939,_0x4a47a6[_0x529d2f(0x3f9,0x37f,0x3a9,0x290)]=0x1;const _0x46ff28={};_0x46ff28[_0x529d2f(0x387,0x357,0x2eb,0x3be)]=mek,await sendButMessage(room['a'],'_Partner\x20D'+'itemukan_\x20'+'🎭','©\x20Copyrigh'+'t\x20'+botname+_0x529d2f(0x1da,0x2b4,0x196,0x370),[_0x3f6f27,_0x4a47a6],_0x46ff28),room['b']=m[_0x529d2f(0x46e,0x381,0x340,0x2aa)],room[_0x529d2f(0x184,0x2a0,0x1be,0x246)]='CHATTING';const _0x358a01={};_0x358a01[_0x385207(0x17b,0xbc,0x169,0x17c)+'t']=_0x385207(0x22e,0x28f,0xec,0x1af);const _0x447cd1={};_0x447cd1['buttonId']=_0x529d2f(0x16d,0x26a,0x158,0x20d),_0x447cd1['buttonText']=_0x358a01,_0x447cd1[_0x385207(0x2f0,0x11a,0x30e,0x1e8)]=0x1;const _0x5f1784={};_0x5f1784['displayTex'+'t']=_0x385207(-0x3e,-0x8c,-0x7b,0x74);const _0x19db7e={};_0x19db7e[_0x529d2f(0x118,0x144,0x177,0x10b)]='skip',_0x19db7e[_0x385207(-0x106,0x92,-0x16f,-0x3f)]=_0x5f1784,_0x19db7e[_0x529d2f(0x39c,0x37f,0x34a,0x27a)]=0x1;const _0x5816f1={};_0x5816f1[_0x529d2f(0x3fa,0x357,0x258,0x390)]=mek,await sendButMessage(room['b'],'_Partner\x20D'+_0x385207(0x18b,0x235,0x182,0x1f8)+'🎭',_0x385207(0x25b,0x203,0xbb,0x1b0)+'t\x20'+botname+_0x385207(0x1b1,0x1b8,0x1b7,0x11d),[_0x447cd1,_0x19db7e],_0x5816f1);}else{let id=+new Date();this['anonymous'][id]={'id':id,'a':m[_0x385207(0x20a,0x226,0xdd,0x1ea)],'b':'','state':_0x529d2f(0x3e5,0x34e,0x31e,0x3e1),'check':function(_0x41fdf5=''){function _0x25960e(_0x5d56d2,_0x3a0626,_0xb66494,_0x14bc54){return _0x529d2f(_0x5d56d2-0x144,_0x3a0626-0x135,_0xb66494-0x6d,_0x5d56d2);}return[this['a'],this['b']][_0x25960e(0x178,0x26f,0x260,0x3a3)](_0x41fdf5);},'other':function(_0x4102e0=''){const _0xebf8f7={};_0xebf8f7[_0x16cf05(0x58b,0x677,0x579,0x64b)]=function(_0x2b98fc,_0x143318){return _0x2b98fc===_0x143318;};function _0x16cf05(_0x3d473a,_0x525ddf,_0x58d95e,_0x2cf649){return _0x385207(_0x525ddf,_0x525ddf-0x28,_0x58d95e-0x1d1,_0x2cf649-0x53f);}const _0x32988f=_0xebf8f7;return _0x32988f['nuRpp'](_0x4102e0,this['a'])?this['b']:_0x4102e0===this['b']?this['a']:'';}};const _0x4b97d6={};_0x4b97d6['displayTex'+'t']=_0x529d2f(0x323,0x346,0x302,0x25a);const _0x127c0b={};_0x127c0b[_0x385207(0x12,-0x92,0x7,-0x53)]=_0x385207(0x11c,0xe6,0x189,0xd3),_0x127c0b[_0x529d2f(0x109,0x158,0x1cd,0x135)]=_0x4b97d6,_0x127c0b['type']=0x1;const _0x2cc305={};_0x2cc305[_0x385207(0x2db,0x1a1,0x215,0x1c0)]=mek,await sendButMessage(m[_0x529d2f(0x417,0x329,0x245,0x261)],_0x529d2f(0x1cb,0x2b1,0x324,0x213)+'u\x20Partner_',_0x385207(0x89,0x220,0xe5,0x1b0)+'t\x20'+botname+_0x385207(0xb7,0x188,0x231,0x11d),[_0x127c0b],_0x2cc305);}break;}}
if (isGroup && budy != undefined) {
	} else {
	console.log('\x1b[1;31m~\x1b[1;37m>', '[\x1b[1;32m CHAT \x1b[1;37m]', timuu, color(q), 'from', color(pushname))
	}		
	} catch (e) {
    e = String(e)
    if (!e.includes("this.isZero")) {
	console.log('Message : %s', color(e, 'green'))
        }
	// console.log(e)
	}
}