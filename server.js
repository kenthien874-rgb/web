const express = require('express');
const session = require('express-session');
const path = require('path');

const app =express();

// Cấu hình session
app.use(session({
    secret: 'bot-hosting-secret-key-2026',
    resave: false,
    saveUninitialized: true,
}));

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Thông tin tài khoản Admin theo yêu cầu của bạn
const ADMIN_ACCOUNT = {
    email: 'giabaotrungki@gmail.com',
    password: 'Tgb@2008'
};

// Trạng thái giả lập của Bot
let botState = {
    status: 'Offline', // Online, Offline, Starting, Restarting
    cpuLoad: '0.00%',
    memory: '0 Bytes / 256 MiB',
    disk: '0 Bytes / 1 GiB',
    address: 'us3.bot-hosting.net:20576',
    consoleLogs: ['[System] Panel initialized successfully.', '[System] Waiting for bot startup...']
};

// API Đăng nhập
app.post('/api/login', (req, res) => {
    const { email, password } = req.body;
    if (email === ADMIN_ACCOUNT.email && password === ADMIN_ACCOUNT.password) {
        req.session.user = { email: ADMIN_ACCOUNT.email, role: 'admin' };
        return res.json({ success: true, message: 'Đăng nhập thành công!' });
    }
    res.status(401).json({ success: false, message: 'Sai tài khoản hoặc mật khẩu!' });
});

// Kiểm tra trạng thái đăng nhập
app.get('/api/check-auth', (req, res) => {
    if (req.session.user) {
        res.json({ loggedIn: true, user: req.session.user });
    } else {
        res.json({ loggedIn: false });
    }
});

// Đăng xuất
app.get('/api/logout', (req, res) => {
    req.session.destroy();
    res.redirect('/');
});

// API Lấy thông tin Bot
app.get('/api/bot/status', (req, res) => {
    if (!req.session.user) return res.status(401).json({ error: 'Unauthorized' });
    res.json(botState);
});

// API Điều khiển Bot (Start, Stop, Restart)
app.post('/api/bot/action', (req, res) => {
    if (!req.session.user) return res.status(401).json({ error: 'Unauthorized' });
    const { action } = req.body;

    if (action === 'start') {
        botState.status = 'Online';
        botState.cpuLoad = '4.15%';
        botState.memory = '45.2 MiB / 256 MiB';
        botState.consoleLogs.push('[Bot] Starting Node.js application...');
        botState.consoleLogs.push('[Bot] Bot logged in as Discord Bot#1234');
    } else if (action === 'stop') {
        botState.status = 'Offline';
        botState.cpuLoad = '0.00%';
        botState.memory = '0 Bytes / 256 MiB';
        botState.consoleLogs.push('[Bot] Bot process stopped by user.');
    } else if (action === 'restart') {
        botState.status = 'Restarting';
        botState.consoleLogs.push('[Bot] Restarting application...');
        setTimeout(() => {
            botState.status = 'Online';
            botState.cpuLoad = '3.80%';
            botState.memory = '42.1 MiB / 256 MiB';
            botState.consoleLogs.push('[Bot] Restart successful.');
        }, 2000);
    }
    res.json({ success: true, botState });
});

app.listen(3000, () => {
    console.log('Server đang chạy tại: http://localhost:3000');
});
