// Uso: node gerar.mjs <arquivo.html> <saida-sem-extensao>
import { chromium } from 'playwright-core'
import QRCode from 'qrcode'
import { pathToFileURL } from 'node:url'

const [, , html, saida] = process.argv
const browser = await chromium.launch({ channel: 'chrome' })
const page = await browser.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 })
await page.goto(pathToFileURL(html).href, { waitUntil: 'networkidle' })

const urls = await page.$$eval('.qr[data-url]', els => els.map(e => e.dataset.url))
const svgs = await Promise.all(urls.map(u => u ? QRCode.toString(u, { type: 'svg', margin: 0, errorCorrectionLevel: 'M' }) : ''))
await page.$$eval('.qr[data-url]', (els, svgs) => els.forEach((e, i) => { if (svgs[i]) e.innerHTML = svgs[i] }), svgs)
await page.evaluate(() => document.fonts.ready)

await page.pdf({ path: saida + '.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true, outline: true, tagged: true })
await page.screenshot({ path: saida + '.png', fullPage: true })
await page.emulateMedia({ media: 'print' })
await browser.close()
