const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const htmlPath = process.argv[2], pdfPath = process.argv[3];
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(htmlPath), { waitUntil: 'networkidle' });
  await page.pdf({
    path: pdfPath, format: 'A4', printBackground: true,
    margin: { top: '0mm', bottom: '12mm', left: '0mm', right: '0mm' },
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-size:7.5px;color:#8a94a3;width:100%;padding:0 14mm;display:flex;justify-content:space-between;"><span>SalesOps CRM UK · Company-in-a-Box · Confidential — Partner Review</span><span class="pageNumber"></span></div>',
  });
  await browser.close();
  console.log('OK', pdfPath);
})();
