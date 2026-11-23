index_html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>CronoNotas Equipe — Dez/2026 a Dez/2027</title>
  <style>
    :root {
      --bg-main: #0e131b;
      --bg-surface: #161d29;
      --bg-card: #1d2636;
      --bg-card-hover: #243044;
      --bg-input: #111722;
      --border: #2b374d;
      --border-strong: #425372;
      --text-primary: #f1f5f9;
      --text-secondary: #94a3b8;
      --text-muted: #64748b;
      --accent: #3b82f6;
      --accent-soft: rgba(59, 130, 246, 0.16);
      --danger: #ef4444;
      --danger-soft: rgba(239, 68, 68, 0.16);
      --warning: #f59e0b;
      --warning-soft: rgba(245, 158, 11, 0.16);
      --success: #10b981;
      --success-soft: rgba(16, 185, 129, 0.16);
      --holiday: #a855f7;
      --holiday-soft: rgba(168, 85, 247, 0.16);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --bottom-nav-h: 64px;
    }

    * {
      box-sizing: border-box;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      margin: 0;
      padding: 0 0 calc(var(--bottom-nav-h) + 20px) 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg-main);
      color: var(--text-primary);
      line-height: 1.45;
      min-height: 100vh;
    }

    button, input, textarea, select {
      font-family: inherit;
      color: inherit;
    }

    /* LOGIN SCREEN */
    .login-screen {
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 16px;
      background: radial-gradient(circle at top, #182338 0%, #0e131b 70%);
    }

    .login-card {
      width: 100%;
      max-width: 420px;
      background: var(--bg-surface);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-lg);
      padding: 20px;
      box-shadow: 0 20px 45px rgba(0, 0, 0, 0.45);
    }

    .login-title {
      font-size: 1.25rem;
      font-weight: 800;
      margin: 0 0 4px 0;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .login-sub {
      font-size: 0.83rem;
      color: var(--text-secondary);
      margin: 0 0 14px 0;
    }

    .form-group {
      margin-bottom: 11px;
    }

    .form-group label {
      display: block;
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--text-secondary);
      margin-bottom: 4px;
      text-transform: uppercase;
    }

    .form-control {
      width: 100%;
      background: var(--bg-input);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 9px 11px;
      font-size: 0.88rem;
      outline: none;
    }

    .form-control:focus {
      border-color: var(--accent);
    }

    .privacy-box {
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.35);
      border-radius: var(--radius-sm);
      padding: 9px 10px;
      font-size: 0.77rem;
      color: #a7f3d0;
      margin-bottom: 12px;
    }

    .mode-badge {
      display: inline-block;
      font-size: 0.7rem;
      padding: 2px 8px;
      border-radius: 999px;
      font-weight: 700;
      background: var(--accent-soft);
      color: #93c5fd;
      border: 1px solid rgba(59, 130, 246, 0.4);
    }

    /* TOP HEADER */
    .topbar {
      position: sticky;
      top: 0;
      z-index: 30;
      background: rgba(14, 19, 27, 0.95);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border);
      padding: 10px 14px;
    }

    .topbar-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      flex-wrap: wrap;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 800;
      font-size: 1rem;
    }

    .user-info-pill {
      display: flex;
      align-items: center;
      gap: 6px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      padding: 4px 9px;
      border-radius: var(--radius-sm);
      font-size: 0.79rem;
    }

    .role-pill {
      font-size: 0.68rem;
      padding: 2px 6px;
      border-radius: 999px;
      font-weight: 700;
      background: var(--warning-soft);
      color: var(--warning);
      border: 1px solid rgba(245, 158, 11, 0.35);
    }

    .role-pill.collab {
      background: var(--accent-soft);
      color: #93c5fd;
      border-color: rgba(59, 130, 246, 0.35);
    }

    .subbar {
      margin-top: 8px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      flex-wrap: wrap;
    }

    .viewing-banner {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.82rem;
      background: var(--bg-card);
      border: 1px solid var(--border);
      padding: 5px 10px;
      border-radius: var(--radius-sm);
      flex: 1;
      min-width: 220px;
    }

    .btn-mini {
      background: var(--accent-soft);
      color: #93c5fd;
      border: 1px solid rgba(59, 130, 246, 0.4);
      border-radius: 6px;
      padding: 3px 8px;
      font-size: 0.74rem;
      font-weight: 600;
      cursor: pointer;
      white-space: nowrap;
    }

    .btn-mini:hover {
      background: rgba(59, 130, 246, 0.28);
    }

    /* MAIN LAYOUT */
    .container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 12px 14px;
    }

    .schedule-split {
      display: grid;
      grid-template-columns: 1fr;
      gap: 14px;
      align-items: start;
    }

    @media (min-width: 980px) {
      .schedule-split {
        grid-template-columns: 1.85fr 1fr;
      }
      .day-drawer-panel {
        position: sticky;
        top: 96px;
      }
    }

    /* PARTICIPANTS STRIP */
    .participants-section {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 10px;
      margin-bottom: 12px;
    }

    .participants-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 8px;
      flex-wrap: wrap;
    }

    .section-label {
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .filter-controls {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }

    .search-input {
      background: var(--bg-input);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 5px 9px;
      font-size: 0.8rem;
      outline: none;
    }

    .search-input:focus {
      border-color: var(--accent);
    }

    .chip-btn {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 5px 10px;
      font-size: 0.76rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }

    .chip-btn.active {
      background: var(--accent);
      border-color: var(--accent);
      color: #fff;
    }

    .participants-scroll {
      display: flex;
      gap: 7px;
      overflow-x: auto;
      padding-bottom: 4px;
      scrollbar-width: thin;
    }

    .p-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 10px;
      border-radius: 999px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      font-size: 0.79rem;
      cursor: pointer;
      white-space: nowrap;
      flex-shrink: 0;
    }

    .p-pill.selected-view {
      border-color: #fff;
      box-shadow: 0 0 0 1px #fff;
    }

    .p-pill.selected-common {
      background: rgba(16, 185, 129, 0.18);
      border-color: var(--success);
      color: #a7f3d0;
    }

    .p-role-tag {
      font-size: 0.66rem;
      color: var(--text-secondary);
      background: rgba(255, 255, 255, 0.05);
      padding: 1px 5px;
      border-radius: 4px;
    }

    .p-dot {
      width: 9px;
      height: 9px;
      border-radius: 50%;
      flex-shrink: 0;
    }

    /* MONTH CONTROLS */
    .month-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 10px;
      flex-wrap: wrap;
    }

    .month-select {
      background: var(--bg-card);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-sm);
      padding: 6px 10px;
      font-size: 0.95rem;
      font-weight: 700;
      outline: none;
    }

    .btn {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 7px 11px;
      font-size: 0.81rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 5px;
    }

    .btn:hover {
      background: var(--bg-card-hover);
    }

    .btn-primary {
      background: var(--accent);
      border-color: var(--accent);
      color: #fff;
    }

    .btn-primary:hover {
      background: #2563eb;
    }

    .btn-danger {
      background: var(--danger-soft);
      border-color: rgba(239, 68, 68, 0.45);
      color: #fca5a5;
    }

    /* COMMON SUMMARY */
    .common-summary {
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.4);
      border-radius: var(--radius-md);
      padding: 10px 12px;
      margin-bottom: 10px;
      font-size: 0.83rem;
    }

    .common-list {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 6px;
    }

    .common-tag {
      background: var(--bg-card);
      border: 1px solid rgba(16, 185, 129, 0.45);
      padding: 4px 8px;
      border-radius: 8px;
      font-size: 0.77rem;
      cursor: pointer;
    }

    /* CALENDAR GRID */
    .grid-wrapper {
      overflow-x: auto;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 8px;
    }

    .calendar-grid {
      min-width: 690px;
    }

    .dow-header {
      display: grid;
      grid-template-columns: 74px repeat(7, 1fr);
      gap: 5px;
      margin-bottom: 5px;
    }

    .dow-cell {
      text-align: center;
      font-size: 0.74rem;
      font-weight: 700;
      color: var(--text-secondary);
      padding: 4px 2px;
    }

    .week-row {
      display: grid;
      grid-template-columns: 74px repeat(7, 1fr);
      gap: 5px;
      margin-bottom: 5px;
      align-items: stretch;
    }

    .week-label {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--text-secondary);
      padding: 5px 4px;
      text-align: center;
    }

    .day-square {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      min-height: 94px;
      padding: 6px;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 3px;
      transition: border-color 0.15s;
    }

    .day-square:hover {
      border-color: var(--border-strong);
      background: var(--bg-card-hover);
    }

    .day-square.selected-day {
      border: 2px solid #60a5fa;
      box-shadow: 0 0 0 1px rgba(96, 165, 250, 0.4);
    }

    .day-square.other-month {
      opacity: 0.32;
    }

    .day-square.dimmed {
      opacity: 0.24;
    }

    .day-square.common-highlight {
      border: 2px solid var(--success);
      background: rgba(16, 185, 129, 0.12);
      opacity: 1 !important;
    }

    .day-square.holiday-day {
      background: linear-gradient(180deg, rgba(168, 85, 247, 0.14) 0%, var(--bg-card) 48%);
      border-color: rgba(168, 85, 247, 0.48);
    }

    .day-square.cancelled-day {
      border-color: var(--danger);
      background: rgba(239, 68, 68, 0.09);
    }

    .day-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 3px;
    }

    .day-num {
      font-size: 0.82rem;
      font-weight: 700;
    }

    .day-badges {
      display: flex;
      align-items: center;
      gap: 3px;
      flex-wrap: wrap;
      justify-content: flex-end;
    }

    .badge-holiday {
      background: var(--holiday-soft);
      color: #d8b4fe;
      border: 1px solid rgba(168, 85, 247, 0.4);
      padding: 1px 4px;
      border-radius: 4px;
      font-size: 0.62rem;
      font-weight: 700;
    }

    .badge-edit {
      background: var(--warning-soft);
      color: var(--warning);
      padding: 1px 4px;
      border-radius: 4px;
      font-size: 0.62rem;
      font-weight: 700;
    }

    .badge-cancel {
      background: var(--danger-soft);
      color: #fca5a5;
      padding: 1px 4px;
      border-radius: 4px;
      font-size: 0.62rem;
      font-weight: 700;
    }

    .badge-incoming {
      background: var(--accent-soft);
      color: #93c5fd;
      padding: 1px 4px;
      border-radius: 4px;
      font-size: 0.62rem;
      font-weight: 700;
    }

    .holiday-mini-name {
      font-size: 0.66rem;
      color: #d8b4fe;
      font-weight: 600;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .day-note-preview {
      font-size: 0.73rem;
      color: var(--text-primary);
      white-space: pre-line;
      word-break: break-word;
      overflow: hidden;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      flex: 1;
    }

    .day-note-preview.empty {
      color: var(--text-muted);
      font-style: italic;
    }

    .day-mentions {
      display: flex;
      flex-wrap: wrap;
      gap: 3px;
    }

    .mention-chip {
      font-size: 0.65rem;
      padding: 1px 5px;
      border-radius: 999px;
      font-weight: 600;
      background: var(--accent-soft);
      color: #bfdbfe;
      border: 1px solid rgba(59, 130, 246, 0.35);
    }

    /* RIGHT / BOTTOM DAY ACTIVITIES PANEL (PAINEL DO DIA) */
    .day-drawer-panel {
      background: var(--bg-surface);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-md);
      padding: 13px;
    }

    .drawer-header {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 8px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 9px;
      margin-bottom: 10px;
    }

    .drawer-title {
      font-size: 1rem;
      font-weight: 800;
    }

    .drawer-sub {
      font-size: 0.76rem;
      color: var(--text-secondary);
    }

    .holiday-alert-box {
      background: var(--holiday-soft);
      border: 1px solid rgba(168, 85, 247, 0.45);
      border-radius: var(--radius-sm);
      padding: 8px 10px;
      margin-bottom: 10px;
      font-size: 0.8rem;
      color: #e9d5ff;
    }

    .activity-block {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 10px;
      margin-bottom: 9px;
    }

    .activity-block-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 6px;
      margin-bottom: 5px;
      font-size: 0.78rem;
    }

    .status-pill-tag {
      font-size: 0.68rem;
      padding: 2px 6px;
      border-radius: 999px;
      font-weight: 700;
    }

    .st-confirmado {
      background: var(--success-soft);
      color: #6ee7b7;
    }

    .st-pendente {
      background: var(--warning-soft);
      color: #fcd34d;
    }

    .st-cancelado {
      background: var(--danger-soft);
      color: #fca5a5;
    }

    /* STATUS FEED */
    .status-composer {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 12px;
      margin-bottom: 12px;
    }

    .status-composer textarea {
      width: 100%;
      background: var(--bg-input);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 9px;
      font-size: 0.86rem;
      min-height: 72px;
      resize: vertical;
      outline: none;
      margin-bottom: 8px;
    }

    .status-feed-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 12px;
      margin-bottom: 10px;
    }

    .status-feed-card.top-recent {
      border-left: 4px solid var(--success);
    }

    .status-card-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 6px;
      flex-wrap: wrap;
    }

    /* ALERTS & CHAT */
    .alert-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 10px 12px;
      margin-bottom: 8px;
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 10px;
    }

    .alert-card.mention-alert {
      border-left: 4px solid var(--accent);
    }

    .alert-card.change-alert {
      border-left: 4px solid var(--warning);
    }

    .chat-box {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 12px;
      margin-top: 12px;
    }

    .chat-context-tag {
      display: inline-block;
      background: var(--accent-soft);
      color: #93c5fd;
      border: 1px solid rgba(59, 130, 246, 0.35);
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.76rem;
      font-weight: 600;
      margin-bottom: 8px;
    }

    .chat-messages {
      max-height: 260px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 10px;
      padding-right: 4px;
    }

    .msg-item {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 8px 10px;
      font-size: 0.83rem;
    }

    .msg-head {
      display: flex;
      justify-content: space-between;
      font-size: 0.72rem;
      color: var(--text-secondary);
      margin-bottom: 3px;
    }

    .chat-form {
      display: flex;
      gap: 6px;
    }

    .chat-form input {
      flex: 1;
      background: var(--bg-input);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 8px 10px;
      font-size: 0.84rem;
      outline: none;
    }

    /* TEAM / OWNER */
    .admin-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 12px;
      margin-bottom: 12px;
    }

    .admin-note {
      font-size: 0.8rem;
      color: var(--text-secondary);
      background: var(--bg-card);
      border: 1px dashed var(--border-strong);
      border-radius: var(--radius-sm);
      padding: 9px 10px;
      margin-bottom: 10px;
    }

    .member-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      padding: 8px 0;
      border-bottom: 1px solid var(--border);
      font-size: 0.84rem;
      flex-wrap: wrap;
    }

    /* MODAL */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.75);
      z-index: 60;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 14px;
    }

    .modal-backdrop.open {
      display: flex;
    }

    .modal {
      background: var(--bg-surface);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-lg);
      width: 100%;
      max-width: 500px;
      max-height: 92vh;
      overflow-y: auto;
      padding: 15px;
    }

    .modal-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 10px;
    }

    .modal textarea {
      width: 100%;
      min-height: 95px;
      background: var(--bg-input);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 9px;
      font-size: 0.88rem;
      resize: vertical;
      outline: none;
      margin-bottom: 8px;
    }

    .mention-picker {
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
      max-height: 125px;
      overflow-y: auto;
      background: var(--bg-input);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 7px;
      margin-bottom: 10px;
    }

    .mention-pick-btn {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 3px 8px;
      font-size: 0.74rem;
      cursor: pointer;
    }

    .two-cols {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin-bottom: 10px;
    }

    .bottom-nav {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      height: var(--bottom-nav-h);
      background: rgba(14, 19, 27, 0.98);
      border-top: 1px solid var(--border);
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      z-index: 40;
    }

    .nav-btn {
      background: transparent;
      border: none;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 2px;
      font-size: 0.7rem;
      font-weight: 600;
      color: var(--text-secondary);
      cursor: pointer;
      position: relative;
    }

    .nav-btn.active {
      color: #60a5fa;
    }

    .nav-badge {
      position: absolute;
      top: 6px;
      right: 22%;
      background: var(--danger);
      color: #fff;
      font-size: 0.62rem;
      padding: 1px 5px;
      border-radius: 999px;
      font-weight: 700;
    }

    .hidden {
      display: none !important;
    }
  </style>
</head>
<body>

  <!-- TELA DE ACESSO INDIVIDUAL POR E-MAIL -->
  <div id="loginScreen" class="login-screen">
    <div class="login-card">
      <div class="login-title">
        <span>📅 CronoNotas Equipe</span>
        <span class="mode-badge" id="backendModeBadge">Pronto p/ GitHub</span>
      </div>
      <p class="login-sub">
        Cronograma mensal e semanal (Dez/2026 a Dez/2027) com feriados, pontos facultativos e mural diário.
      </p>

      <div class="privacy-box">
        🔒 <strong>Privacidade de Acesso:</strong> Cada participante cria a própria senha pessoal com seu e-mail. O proprietário gerencia quem participa da equipe, mas <strong>não tem acesso às senhas</strong> nem pode editar ou apagar cronogramas de outras pessoas.
      </div>

      <div class="form-group">
        <label>1. Selecione seu nome na equipe</label>
        <select id="loginMemberSelect" class="form-control" onchange="syncLoginEmailFromMember()"></select>
      </div>

      <div class="form-group">
        <label>2. Seu E-mail de Acesso</label>
        <input type="email" id="loginEmailInput" class="form-control" placeholder="seu.email@exemplo.com" required />
      </div>

      <div class="form-group">
        <label>3. Sua Senha Pessoal (privada)</label>
        <input type="password" id="loginPasswordInput" class="form-control" placeholder="Mínimo 6 caracteres" required />
      </div>

      <div id="loginErrorMsg" style="color:#fca5a5; font-size:0.79rem; margin-bottom:8px;" class="hidden"></div>

      <button class="btn btn-primary" style="width:100%; padding:10px; font-size:0.9rem;" onclick="handleEmailLogin()">
        Entrar no Meu Cronograma
      </button>

      <p style="font-size:0.74rem; color:var(--text-secondary); margin:10px 0 0 0; text-align:center;">
        Primeiro acesso? Digite seu e-mail e crie sua senha acima para ativar sua conta individual.
      </p>
    </div>
  </div>

  <!-- APLICATIVO PRINCIPAL -->
  <div id="appShell" class="hidden">
    <header class="topbar">
      <div class="topbar-row">
        <div class="brand">
          <span>CronoNotas</span>
          <span class="mode-badge" id="topSyncBadge">Dez/26–Dez/27</span>
        </div>
        <div class="user-info-pill">
          <span id="loggedUserDisplay"><strong>Gabriel</strong></span>
          <span id="loggedRolePill" class="role-pill">Proprietário</span>
          <button class="btn-mini" onclick="logoutUser()">Sair</button>
        </div>
      </div>

      <div class="subbar">
        <div class="viewing-banner">
          <span id="viewingLabel">Meu cronograma: <strong>Gabriel</strong></span>
          <button id="backToMineBtn" class="btn-mini hidden" onclick="viewParticipantSchedule(loggedUserId)">Voltar ao meu</button>
        </div>
      </div>
    </header>

    <main class="container">
      <!-- ABA 1: CRONOGRAMA + PAINEL DO DIA -->
      <section id="tab-schedule">
        <div class="participants-section">
          <div class="participants-top">
            <span class="section-label">Equipe (16/20) — Toque no nome para ver agenda ou filtrar dias em comum</span>
            <div class="filter-controls">
              <input type="text" id="participantSearch" class="search-input" style="width:130px;" placeholder="Nome ou cargo..." oninput="renderParticipantsBar()" />
              <select id="roleFilterSelect" class="search-input" style="width:135px;" onchange="renderParticipantsBar()">
                <option value="ALL">Todos os cargos</option>
                <option value="Agente de Saúde">Agente de Saúde</option>
                <option value="Agente Social">Agente Social</option>
                <option value="Auxiliar Enfermagem">Aux. Enfermagem</option>
                <option value="Assistente Social">Assistente Social</option>
                <option value="Psicóloga">Psicóloga</option>
                <option value="Médica">Médica</option>
              </select>
              <button id="commonToggleBtn" class="chip-btn" onclick="toggleCommonFilter()">🤝 Dias em comum</button>
              <button class="chip-btn" onclick="clearFilters()">Limpar</button>
            </div>
          </div>
          <div id="participantsScroll" class="participants-scroll"></div>
        </div>

        <div id="commonSummaryBox" class="common-summary hidden"></div>

        <div class="month-bar">
          <div style="display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
            <select id="monthYearSelect" class="month-select" onchange="selectMonthFromDropdown(this.value)"></select>
            <span style="font-size:0.75rem; color:#d8b4fe;">🟣 Feriados / Pontos Facultativos marcados</span>
          </div>
          <div style="display:flex; gap:6px;">
            <button class="btn" onclick="changeMonth(-1)">◀ Ant.</button>
            <button class="btn" onclick="changeMonth(1)">Próx. ▶</button>
          </div>
        </div>

        <div class="schedule-split">
          <!-- GRADE HORIZONTAL POR SEMANA -->
          <div class="grid-wrapper">
            <div class="calendar-grid">
              <div class="dow-header">
                <div class="dow-cell">Semana</div>
                <div class="dow-cell">Dom</div>
                <div class="dow-cell">Seg</div>
                <div class="dow-cell">Ter</div>
                <div class="dow-cell">Qua</div>
                <div class="dow-cell">Qui</div>
                <div class="dow-cell">Sex</div>
                <div class="dow-cell">Sáb</div>
              </div>
              <div id="weeksContainer"></div>
            </div>
          </div>

          <!-- PAINEL DE ATIVIDADES DO DIA SELECIONADO -->
          <aside class="day-drawer-panel" id="dayDrawerPanel">
            <div class="drawer-header">
              <div>
                <div class="drawer-title" id="drawerDayTitle">Selecione um dia</div>
                <div class="drawer-sub" id="drawerDaySub">Atividades e marcações da data</div>
              </div>
              <button id="drawerEditBtn" class="btn btn-primary" onclick="openEditModalForSelectedDay()">✏️ Editar Dia</button>
            </div>

            <div id="drawerHolidayBox" class="holiday-alert-box hidden"></div>

            <div class="section-label" style="margin-bottom:5px;">Atividade neste cronograma</div>
            <div id="drawerOwnerActivity" class="activity-block"></div>

            <div class="section-label" style="margin:10px 0 5px 0;">Quem marcou você neste dia</div>
            <div id="drawerIncomingMentions"></div>

            <div style="margin-top:10px; display:flex; gap:6px; flex-wrap:wrap;">
              <button class="btn" style="width:100%;" onclick="openChatForSelectedDay()">💬 Abrir Chat deste Dia</button>
            </div>
          </aside>
        </div>
      </section>

      <!-- ABA 2: STATUS DIÁRIO -->
      <section id="tab-status" class="hidden">
        <div class="status-composer">
          <div class="participants-top">
            <span class="section-label">Meu Status Diário e da Semana</span>
            <span style="font-size:0.74rem; color:var(--text-secondary);">Ao publicar, seu cartão sobe para o topo</span>
          </div>
          <textarea id="statusInput" placeholder="Ex.: Hoje: Visita domiciliar com @Aldenan e atendimento na unidade com @Talita. Semana: fechar cronograma de Dezembro..."></textarea>
          <div style="display:flex; justify-content:space-between; align-items:center; gap:8px; flex-wrap:wrap;">
            <button class="btn" onclick="insertMentionIntoStatus()">+ Marcar @Colega</button>
            <button class="btn btn-primary" onclick="publishDailyStatus()">Publicar / Subir Registro</button>
          </div>
        </div>

        <div class="participants-top" style="margin-bottom:8px;">
          <span class="section-label">Mural da Equipe (Mais recentes no topo)</span>
          <select id="statusFilterUser" class="search-input" style="width:185px;" onchange="renderStatusFeed()"></select>
        </div>

        <div id="statusFeedList"></div>
      </section>

      <!-- ABA 3: ALERTAS & CHAT -->
      <section id="tab-alerts" class="hidden">
        <div class="participants-top" style="margin-bottom:8px;">
          <span class="section-label">Notificações de Marcações e Alterações</span>
          <button class="btn-mini" onclick="markAllAlertsRead()">Marcar lidas</button>
        </div>
        <div id="alertsList"></div>

        <div class="chat-box">
          <div class="participants-top">
            <span class="section-label">Chat da Equipe</span>
            <span id="chatContextBadge" class="chat-context-tag">Assunto: Geral</span>
          </div>
          <div id="chatMessages" class="chat-messages"></div>
          <form class="chat-form" onsubmit="sendChatMessage(event)">
            <input type="text" id="chatInput" placeholder="Combine horários, trocas ou ausências..." required />
            <button type="submit" class="btn btn-primary">Enviar</button>
          </form>
        </div>
      </section>

      <!-- ABA 4: EQUIPE & PROPRIETÁRIO -->
      <section id="tab-team" class="hidden">
        <div class="admin-card">
          <div class="section-label" style="margin-bottom:6px;">Regras de Privacidade e Acesso</div>
          <div class="admin-note">
            <strong>1. Senhas Individuais:</strong> Cada integrante entra com o próprio e-mail e senha privada. Nem o proprietário nem outros colegas têm acesso às senhas uns dos outros.<br />
            <strong>2. Proprietário (Gabriel):</strong> Pode incluir ou remover participantes (até 20 pessoas) e acompanhar todos os cronogramas, mas <strong>não pode</strong> apagar ou editar anotações escritas por outras pessoas.<br />
            <strong>3. Colaborador:</strong> Edita e apaga apenas o próprio cronograma e status diário.
          </div>

          <div id="ownerControls" class="hidden">
            <div class="section-label" style="margin-bottom:6px;">Incluir Novo Participante (até 20)</div>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:6px; margin-bottom:6px;">
              <input type="text" id="newMemberName" class="search-input" placeholder="Nome (ex.: Lucas)" />
              <input type="text" id="newMemberRole" class="search-input" placeholder="Cargo (ex.: Agente Social)" />
            </div>
            <div style="display:flex; gap:6px; margin-bottom:12px;">
              <input type="email" id="newMemberEmail" class="search-input" style="flex:1;" placeholder="E-mail autorizado para cadastro (opcional)" />
              <button class="btn btn-primary" onclick="addCollaborator()">+ Incluir</button>
            </div>
          </div>

          <div class="section-label" style="margin-bottom:6px;">Participantes Ativos (<span id="activeMembersCount">0</span>/20)</div>
          <div id="membersList"></div>
        </div>
      </section>
    </main>

    <!-- MODAL DE EDIÇÃO DO DIA -->
    <div id="dayModalBackdrop" class="modal-backdrop" onclick="if(event.target.id==='dayModalBackdrop') closeDayModal()">
      <div class="modal">
        <div class="modal-header">
          <div>
            <div style="font-weight:800; font-size:0.98rem;" id="modalDayTitle">Data</div>
            <div style="font-size:0.75rem; color:var(--text-secondary);" id="modalOwnerInfo">Meu cronograma</div>
          </div>
          <button class="btn" onclick="closeDayModal()">✕</button>
        </div>

        <div id="modalHolidayBanner" class="holiday-alert-box hidden"></div>

        <div class="two-cols">
          <div>
            <label class="section-label" style="display:block; margin-bottom:4px;">Turno / Horário</label>
            <select id="modalShiftSelect" class="form-control">
              <option value="Dia todo">Dia todo</option>
              <option value="Manhã">Manhã</option>
              <option value="Tarde">Tarde</option>
              <option value="Manhã e Tarde">Manhã e Tarde</option>
              <option value="Horário específico">Horário específico (na nota)</option>
            </select>
          </div>
          <div>
            <label class="section-label" style="display:block; margin-bottom:4px;">Situação</label>
            <select id="modalStatusSelect" class="form-control">
              <option value="confirmado">✅ Confirmado</option>
              <option value="pendente">⏳ Pendente / A combinar</option>
              <option value="cancelado">❌ Cancelado / Ausência</option>
            </select>
          </div>
        </div>

        <label class="section-label" style="display:block; margin-bottom:4px;">Atividades e anotações do dia</label>
        <textarea id="modalNoteTextarea" placeholder="Ex.: Visita ao Hospital 09h + @Sheila + @Talita"></textarea>

        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
          <span class="section-label">Marcar colega (@)</span>
          <span style="font-size:0.72rem; color:var(--text-secondary);">Toque para inserir</span>
        </div>
        <div id="modalMentionPicker" class="mention-picker"></div>

        <div style="display:flex; justify-content:flex-end; gap:8px; margin-top:10px;">
          <button class="btn" onclick="closeDayModal()">Cancelar</button>
          <button class="btn btn-primary" onclick="saveDayModal()">Salvar no Meu Cronograma</button>
        </div>
      </div>
    </div>

    <!-- NAVEGAÇÃO INFERIOR -->
    <nav class="bottom-nav">
      <button class="nav-btn active" id="nav-schedule" onclick="switchTab('schedule')">
        <span>📅</span>
        <span>Cronograma</span>
      </button>
      <button class="nav-btn" id="nav-status" onclick="switchTab('status')">
        <span>⚡</span>
        <span>Status Diário</span>
      </button>
      <button class="nav-btn" id="nav-alerts" onclick="switchTab('alerts')">
        <span>🔔</span>
        <span>Alertas & Chat</span>
        <span id="alertsBadge" class="nav-badge hidden">0</span>
      </button>
      <button class="nav-btn" id="nav-team" onclick="switchTab('team')">
        <span>👥</span>
        <span>Equipe</span>
      </button>
    </nav>
  </div>

  <!-- Firebase SDK (opcional: ativado automaticamente ao preencher FIREBASE_CONFIG abaixo) -->
  <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-auth-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore-compat.js"></script>

  <script>
    // =========================================================================
    // CONFIGURAÇÃO DO FIREBASE (COLE SUAS CHAVES AQUI PARA SINCRONIZAR NA NUVEM)
    // Enquanto apiKey estiver vazia, o sistema funciona em modo local no aparelho.
    // =========================================================================
    const FIREBASE_CONFIG = {
      apiKey: "",
      authDomain: "",
      projectId: "",
      storageBucket: "",
      messagingSenderId: "",
      appId: ""
    };

    const STORAGE_KEY = "crononotas_equipe_2026_2027_v1";
    const SESSION_KEY = "crononotas_session_uid_v1";
    const OWNER_ID = "u_gabriel";

    // Meses permitidos: Dezembro 2026 (2026-11) até Dezembro 2027 (2027-11)
    const ALLOWED_MONTHS = [
      { year: 2026, month: 11, label: "Dezembro 2026" },
      { year: 2027, month: 0, label: "Janeiro 2027" },
      { year: 2027, month: 1, label: "Fevereiro 2027" },
      { year: 2027, month: 2, label: "Março 2027" },
      { year: 2027, month: 3, label: "Abril 2027" },
      { year: 2027, month: 4, label: "Maio 2027" },
      { year: 2027, month: 5, label: "Junho 2027" },
      { year: 2027, month: 6, label: "Julho 2027" },
      { year: 2027, month: 7, label: "Agosto 2027" },
      { year: 2027, month: 8, label: "Setembro 2027" },
      { year: 2027, month: 9, label: "Outubro 2027" },
      { year: 2027, month: 10, label: "Novembro 2027" },
      { year: 2027, month: 11, label: "Dezembro 2027" }
    ];

    // Feriados Nacionais, Estaduais (SP), Municipais (Suzano) e Pontos Facultativos (Dez/2026 e 2027)
    const HOLIDAYS = {
      // Dezembro 2026
      "2026-12-24": { type: "Ponto Facultativo", title: "Véspera de Natal (Ponto Facultativo após 13h/14h)" },
      "2026-12-25": { type: "Feriado Nacional", title: "Natal" },
      "2026-12-31": { type: "Ponto Facultativo", title: "Véspera de Ano-Novo (Ponto Facultativo após 13h/14h)" },

      // 2027
      "2027-01-01": { type: "Feriado Nacional", title: "Confraternização Universal (Ano-Novo)" },
      "2027-01-20": { type: "Feriado Municipal", title: "São Sebastião (Padroeiro — Suzano/SP)" },
      "2027-02-08": { type: "Ponto Facultativo", title: "Carnaval (Segunda-feira — Ponto Facultativo)" },
      "2027-02-09": { type: "Ponto Facultativo", title: "Carnaval (Terça-feira — Ponto Facultativo)" },
      "2027-02-10": { type: "Ponto Facultativo", title: "Quarta-feira de Cinzas (Ponto Facultativo até 14h)" },
      "2027-03-26": { type: "Feriado Nacional", title: "Paixão de Cristo (Sexta-feira Santa)" },
      "2027-04-02": { type: "Feriado Municipal", title: "Emancipação Político-Administrativa de Suzano" },
      "2027-04-21": { type: "Feriado Nacional", title: "Tiradentes" },
      "2027-05-01": { type: "Feriado Nacional", title: "Dia Mundial do Trabalho" },
      "2027-05-27": { type: "Ponto Facultativo", title: "Corpus Christi (Ponto Facultativo)" },
      "2027-07-09": { type: "Feriado Estadual", title: "Revolução Constitucionalista de 1932 (SP)" },
      "2027-09-07": { type: "Feriado Nacional", title: "Independência do Brasil" },
      "2027-10-12": { type: "Feriado Nacional", title: "Nossa Senhora Aparecida" },
      "2027-10-28": { type: "Ponto Facultativo", title: "Dia do Servidor Público (Ponto Facultativo)" },
      "2027-11-02": { type: "Feriado Nacional", title: "Finados" },
      "2027-11-15": { type: "Feriado Nacional", title: "Proclamação da República" },
      "2027-11-20": { type: "Feriado Nacional", title: "Dia Nacional de Zumbi e da Consciência Negra" },
      "2027-12-24": { type: "Ponto Facultativo", title: "Véspera de Natal (Ponto Facultativo após 13h/14h)" },
      "2027-12-25": { type: "Feriado Nacional", title: "Natal" },
      "2027-12-31": { type: "Ponto Facultativo", title: "Véspera de Ano-Novo (Ponto Facultativo após 13h/14h)" }
    };

    const PALETTE = [
      "#3b82f6", "#ec4899", "#10b981", "#f59e0b", "#8b5cf6",
      "#06b6d4", "#f97316", "#84cc16", "#e11d48", "#14b8a6",
      "#6366f1", "#a855f7", "#22c55e", "#eab308", "#0ea5e9",
      "#d946ef", "#f43f5e", "#64748b", "#0d9488", "#fb923c"
    ];

    const INITIAL_TEAM = [
      { id: "u_gabriel", name: "Gabriel", jobRole: "Proprietário / Coordenação", sysRole: "owner", email: "", color: PALETTE[0], active: true },
      { id: "u_aldenan", name: "Aldenan", jobRole: "Agente Social", sysRole: "collab", email: "", color: PALETTE[1], active: true },
      { id: "u_ana", name: "Ana", jobRole: "Auxiliar Enfermagem", sysRole: "collab", email: "", color: PALETTE[2], active: true },
      { id: "u_angel", name: "Angel", jobRole: "Agente de Saúde", sysRole: "collab", email: "", color: PALETTE[3], active: true },
      { id: "u_cilene", name: "Cilene", jobRole: "Agente Social", sysRole: "collab", email: "", color: PALETTE[4], active: true },
      { id: "u_cleciana", name: "Cleciana", jobRole: "Agente Social", sysRole: "collab", email: "", color: PALETTE[5], active: true },
      { id: "u_deise", name: "Deise", jobRole: "Auxiliar Enfermagem", sysRole: "collab", email: "", color: PALETTE[6], active: true },
      { id: "u_diogo", name: "Diogo", jobRole: "Agente de Saúde", sysRole: "collab", email: "", color: PALETTE[7], active: true },
      { id: "u_giliard", name: "Giliard", jobRole: "Agente de Saúde", sysRole: "collab", email: "", color: PALETTE[8], active: true },
      { id: "u_jair", name: "Jair", jobRole: "Agente de Saúde", sysRole: "collab", email: "", color: PALETTE[9], active: true },
      { id: "u_kaique", name: "Kaique", jobRole: "Auxiliar Enfermagem", sysRole: "collab", email: "", color: PALETTE[10], active: true },
      { id: "u_renata", name: "Renata", jobRole: "Agente de Saúde", sysRole: "collab", email: "", color: PALETTE[11], active: true },
      { id: "u_rosimeire", name: "Rosimeire", jobRole: "Assistente Social", sysRole: "collab", email: "", color: PALETTE[12], active: true },
      { id: "u_sheila", name: "Sheila", jobRole: "Psicóloga", sysRole: "collab", email: "", color: PALETTE[13], active: true },
      { id: "u_talita", name: "Talita", jobRole: "Médica", sysRole: "collab", email: "", color: PALETTE[14], active: true },
      { id: "u_yasmin", name: "Yasmin", jobRole: "Auxiliar Enfermagem", sysRole: "collab", email: "", color: PALETTE[15], active: true }
    ];

    function buildInitialState() {
      return {
        users: INITIAL_TEAM,
        // localAuthHashes[userId] = { email, passHash } (somente no modo teste local)
        localAuth: {},
        schedules: {
          u_gabriel: {
            "2026-12-03": {
              text: "Visita ao Hospital + @Sheila + @Talita",
              shift: "Manhã",
              status: "confirmado",
              mentions: ["u_sheila", "u_talita"],
              lastEditedAt: "23/11 19:00"
            },
            "2026-12-10": {
              text: "Busca ativa e acompanhamento territorial com @Aldenan e @Rosimeire",
              shift: "Manhã e Tarde",
              status: "confirmado",
              mentions: ["u_aldenan", "u_rosimeire"],
              lastEditedAt: "23/11 19:05"
            }
          },
          u_sheila: {
            "2026-12-03": {
              text: "Atendimento compartilhado no Hospital com @Gabriel e @Talita",
              shift: "Manhã",
              status: "confirmado",
              mentions: ["u_gabriel", "u_talita"],
              lastEditedAt: "23/11 19:10"
            }
          }
        },
        statusPosts: [
          {
            id: "st_init_1",
            userId: "u_sheila",
            text: "Hoje: Atendimentos psicológicos e alinhamento com @Gabriel e @Rosimeire.\nSemana: organizar agenda de Dezembro/2026.",
            updatedAt: "Hoje, 19:10"
          },
          {
            id: "st_init_2",
            userId: "u_gabriel",
            text: "Hoje: Revisão do cronograma de Dezembro/2026 e 2027 com toda a equipe.\nSemana: confirmar visitas externas.",
            updatedAt: "Hoje, 19:00"
          }
        ],
        alerts: [
          {
            id: "al_init_1",
            type: "mention",
            targetUserId: "u_gabriel",
            fromUserId: "u_sheila",
            dateKey: "2026-12-03",
            message: "Sheila (Psicóloga) marcou você em 03/12/2026: 'Atendimento compartilhado no Hospital'.",
            time: "Hoje, 19:10",
            read: false
          }
        ],
        chatMessages: [
          {
            id: "msg_init_1",
            fromUserId: "u_sheila",
            contextDateKey: "2026-12-03",
            text: "Pessoal, confirmando nossa saída para o Hospital no dia 03/12 às 08h30.",
            time: "19:12"
          }
        ]
      };
    }

    let useFirebase = false;
    let fbAuth = null;
    let fbDb = null;

    if (FIREBASE_CONFIG.apiKey && typeof firebase !== "undefined") {
      try {
        firebase.initializeApp(FIREBASE_CONFIG);
        fbAuth = firebase.auth();
        fbDb = firebase.firestore();
        useFirebase = true;
      } catch (e) {
        console.warn("Firebase não inicializado, usando armazenamento local:", e);
      }
    }

    let state = loadLocalState();
    let monthIndex = 0; // 0 = Dezembro 2026
    let loggedUserId = null;
    let viewingUserId = null;
    let selectedDateKey = "2026-12-03";
    let commonFilterActive = false;
    let selectedCommonUserId = null;
    let activeChatDateKey = null;

    function loadLocalState() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY);
        if (raw) return JSON.parse(raw);
      } catch (e) {}
      const init = buildInitialState();
      saveLocalState(init);
      return init;
    }

    function saveLocalState(target = state) {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(target));
      } catch (e) {}
    }

    async function persistState() {
      saveLocalState(state);
      if (useFirebase && fbDb) {
        try {
          await fbDb.collection("crononotas").doc("equipe_principal").set(state, { merge: true });
        } catch (err) {
          console.error("Erro ao sincronizar com Firebase:", err);
        }
      }
    }

    function simpleHash(str) {
      let h = 2166136261;
      for (let i = 0; i < str.length; i++) {
        h ^= str.charCodeAt(i);
        h += (h << 1) + (h << 4) + (h << 7) + (h << 8) + (h << 24);
      }
      return (h >>> 0).toString(16);
    }

    function getUserById(id) {
      return state.users.find((u) => u.id === id) || { id, name: "Participante", jobRole: "", sysRole: "collab", color: "#64748b", active: true };
    }

    function getActiveUsers() {
      return state.users.filter((u) => u.active);
    }

    function populateLoginSelect() {
      const sel = document.getElementById("loginMemberSelect");
      sel.innerHTML = getActiveUsers()
        .map((u) => `<option value="${u.id}">${u.name} — ${u.jobRole}</option>`)
        .join("");
      syncLoginEmailFromMember();

      const badge = document.getElementById("backendModeBadge");
      badge.textContent = useFirebase ? "Nuvem Conectada" : "Modo Local / GitHub";
    }

    function syncLoginEmailFromMember() {
      const uid = document.getElementById("loginMemberSelect").value;
      const user = getUserById(uid);
      const savedAuth = state.localAuth && state.localAuth[uid];
      document.getElementById("loginEmailInput").value = (savedAuth && savedAuth.email) || user.email || "";
    }

    async function handleEmailLogin() {
      const uid = document.getElementById("loginMemberSelect").value;
      const email = document.getElementById("loginEmailInput").value.trim().toLowerCase();
      const password = document.getElementById("loginPasswordInput").value;
      const errEl = document.getElementById("loginErrorMsg");

      errEl.classList.add("hidden");
      if (!email || !email.includes("@")) {
        errEl.textContent = "Informe um endereço de e-mail válido.";
        errEl.classList.remove("hidden");
        return;
      }
      if (!password || password.length < 6) {
        errEl.textContent = "Digite uma senha pessoal com pelo menos 6 caracteres.";
        errEl.classList.remove("hidden");
        return;
      }

      if (useFirebase && fbAuth) {
        try {
          try {
            await fbAuth.signInWithEmailAndPassword(email, password);
          } catch (signInErr) {
            if (signInErr.code === "auth/user-not-found" || signInErr.code === "auth/invalid-credential") {
              await fbAuth.createUserWithEmailAndPassword(email, password);
            } else {
              throw signInErr;
            }
          }
          const user = getUserById(uid);
          user.email = email;
          await persistState();
        } catch (fbErr) {
          errEl.textContent = "Erro de autenticação: " + fbErr.message;
          errEl.classList.remove("hidden");
          return;
        }
      } else {
        if (!state.localAuth) state.localAuth = {};
        const existing = state.localAuth[uid];
        const passHash = simpleHash(password);

        if (existing) {
          if (existing.email !== email || existing.passHash !== passHash) {
            errEl.textContent = "E-mail ou senha incorretos para este participante.";
            errEl.classList.remove("hidden");
            return;
          }
        } else {
          state.localAuth[uid] = { email, passHash };
          const user = getUserById(uid);
          user.email = email;
          saveLocalState();
        }
      }

      loggedUserId = uid;
      viewingUserId = uid;
      localStorage.setItem(SESSION_KEY, uid);
      document.getElementById("loginPasswordInput").value = "";
      document.getElementById("loginScreen").classList.add("hidden");
      document.getElementById("appShell").classList.remove("hidden");
      initAppUI();
    }

    function logoutUser() {
      if (useFirebase && fbAuth) fbAuth.signOut();
      loggedUserId = null;
      localStorage.removeItem(SESSION_KEY);
      document.getElementById("appShell").classList.add("hidden");
      document.getElementById("loginScreen").classList.remove("hidden");
      populateLoginSelect();
    }

    function initAppUI() {
      const monthSel = document.getElementById("monthYearSelect");
      monthSel.innerHTML = ALLOWED_MONTHS.map((m, idx) => `<option value="${idx}">${m.label}</option>`).join("");
      monthSel.value = String(monthIndex);

      if (useFirebase && fbDb) {
        document.getElementById("topSyncBadge").textContent = "Nuvem Ativa";
        fbDb.collection("crononotas").doc("equipe_principal").onSnapshot((doc) => {
          if (doc.exists) {
            const remote = doc.data();
            if (remote && remote.users) {
              state = { ...state, ...remote };
              saveLocalState(state);
              renderAll();
            }
          }
        });
      }

      renderAll();
    }

    function formatDateKey(year, month, day) {
      return `${year}-${String(month + 1).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
    }

    function formatDateLabel(dateKey) {
      if (!dateKey) return "Geral";
      const [y, m, d] = dateKey.split("-").map(Number);
      const dt = new Date(y, m - 1, d);
      const dias = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"];
      return `${dias[dt.getDay()]}, ${String(d).padStart(2, "0")}/${String(m).padStart(2, "0")}/${y}`;
    }

    function nowTimeLabel() {
      const dt = new Date();
      return `Hoje, ${String(dt.getHours()).padStart(2, "0")}:${String(dt.getMinutes()).padStart(2, "0")}`;
    }

    function selectMonthFromDropdown(idxStr) {
      monthIndex = Number(idxStr);
      const cur = ALLOWED_MONTHS[monthIndex];
      selectedDateKey = formatDateKey(cur.year, cur.month, 1);
      renderSchedule();
      renderDayDrawer();
    }

    function changeMonth(delta) {
      const next = monthIndex + delta;
      if (next < 0 || next >= ALLOWED_MONTHS.length) return;
      monthIndex = next;
      document.getElementById("monthYearSelect").value = String(monthIndex);
      const cur = ALLOWED_MONTHS[monthIndex];
      selectedDateKey = formatDateKey(cur.year, cur.month, 1);
      renderSchedule();
      renderDayDrawer();
    }

    function viewParticipantSchedule(uid) {
      viewingUserId = uid;
      renderAll();
    }

    function toggleCommonFilter() {
      commonFilterActive = !commonFilterActive;
      if (commonFilterActive && !selectedCommonUserId) {
        const other = getActiveUsers().find((u) => u.id !== loggedUserId);
        selectedCommonUserId = other ? other.id : null;
      }
      renderAll();
    }

    function clearFilters() {
      commonFilterActive = false;
      selectedCommonUserId = null;
      viewingUserId = loggedUserId;
      document.getElementById("participantSearch").value = "";
      document.getElementById("roleFilterSelect").value = "ALL";
      renderAll();
    }

    function isDayInCommon(dateKey, otherId) {
      const myEntry = (state.schedules[loggedUserId] || {})[dateKey];
      const otherEntry = (state.schedules[otherId] || {})[dateKey];

      const iMentioned = myEntry && myEntry.status !== "cancelado" && (myEntry.mentions || []).includes(otherId);
      const theyMentioned = otherEntry && otherEntry.status !== "cancelado" && (otherEntry.mentions || []).includes(loggedUserId);
      const bothActive =
        myEntry && myEntry.status !== "cancelado" && (myEntry.text || "").trim() &&
        otherEntry && otherEntry.status !== "cancelado" && (otherEntry.text || "").trim();

      return Boolean(iMentioned || theyMentioned || bothActive);
    }

    function getIncomingMentionsForDay(targetUid, dateKey) {
      const matches = [];
      getActiveUsers().forEach((u) => {
        if (u.id === targetUid) return;
        const entry = (state.schedules[u.id] || {})[dateKey];
        if (entry && (entry.mentions || []).includes(targetUid)) {
          matches.push({ author: u, entry });
        }
      });
      return matches;
    }

    function renderTopHeader() {
      const loggedUser = getUserById(loggedUserId);
      document.getElementById("loggedUserDisplay").innerHTML = `<strong>${loggedUser.name}</strong>`;
      const rolePill = document.getElementById("loggedRolePill");
      if (loggedUser.sysRole === "owner") {
        rolePill.textContent = "Proprietário";
        rolePill.className = "role-pill";
      } else {
        rolePill.textContent = loggedUser.jobRole || "Colaborador";
        rolePill.className = "role-pill collab";
      }

      const viewed = getUserById(viewingUserId);
      const viewingLabel = document.getElementById("viewingLabel");
      const backBtn = document.getElementById("backToMineBtn");

      if (viewingUserId === loggedUserId) {
        viewingLabel.innerHTML = `Meu cronograma: <strong>${viewed.name}</strong> (${viewed.jobRole})`;
        backBtn.classList.add("hidden");
      } else {
        viewingLabel.innerHTML = `Vendo agenda de: <strong>${viewed.name}</strong> (${viewed.jobRole}) — leitura`;
        backBtn.classList.remove("hidden");
      }
    }

    function renderParticipantsBar() {
      const q = (document.getElementById("participantSearch").value || "").trim().toLowerCase();
      const roleFilter = document.getElementById("roleFilterSelect").value;
      document.getElementById("commonToggleBtn").classList.toggle("active", commonFilterActive);

      const list = getActiveUsers().filter((u) => {
        const matchText = !q || u.name.toLowerCase().includes(q) || (u.jobRole || "").toLowerCase().includes(q);
        const matchRole = roleFilter === "ALL" || u.jobRole === roleFilter;
        return matchText && matchRole;
      });

      document.getElementById("participantsScroll").innerHTML = list
        .map((u) => {
          const isView = u.id === viewingUserId;
          const isCommon = commonFilterActive && u.id === selectedCommonUserId;
          return `
            <button class="p-pill ${isView ? "selected-view" : ""} ${isCommon ? "selected-common" : ""}" onclick="handleParticipantClick('${u.id}')">
              <span class="p-dot" style="background:${u.color}"></span>
              <span><strong>${u.name}</strong></span>
              <span class="p-role-tag">${u.jobRole}</span>
            </button>
          `;
        })
        .join("");
    }

    function handleParticipantClick(uid) {
      if (commonFilterActive) {
        selectedCommonUserId = uid;
        renderSchedule();
      } else {
        viewParticipantSchedule(uid);
      }
    }

    function renderSchedule() {
      const cur = ALLOWED_MONTHS[monthIndex];
      document.getElementById("monthYearSelect").value = String(monthIndex);

      const firstDay = new Date(cur.year, cur.month, 1);
      const startDow = firstDay.getDay();
      const daysInMonth = new Date(cur.year, cur.month + 1, 0).getDate();
      const prevMonthDays = new Date(cur.year, cur.month, 0).getDate();

      const cells = [];
      for (let i = startDow - 1; i >= 0; i--) {
        const d = prevMonthDays - i;
        const pm = cur.month === 0 ? 11 : cur.month - 1;
        const py = cur.month === 0 ? cur.year - 1 : cur.year;
        cells.push({ year: py, month: pm, day: d, inMonth: false });
      }
      for (let d = 1; d <= daysInMonth; d++) {
        cells.push({ year: cur.year, month: cur.month, day: d, inMonth: true });
      }
      let nextDay = 1;
      while (cells.length % 7 !== 0) {
        const nm = cur.month === 11 ? 0 : cur.month + 1;
        const ny = cur.month === 11 ? cur.year + 1 : cur.year;
        cells.push({ year: ny, month: nm, day: nextDay++, inMonth: false });
      }

      const commonBox = document.getElementById("commonSummaryBox");
      const commonKeys = new Set();
      if (commonFilterActive && selectedCommonUserId) {
        const otherUser = getUserById(selectedCommonUserId);
        cells.forEach((c) => {
          if (!c.inMonth) return;
          const dk = formatDateKey(c.year, c.month, c.day);
          if (isDayInCommon(dk, selectedCommonUserId)) commonKeys.add(dk);
        });
        const sorted = Array.from(commonKeys).sort();
        commonBox.classList.remove("hidden");
        commonBox.innerHTML = `
          <div><strong>Dias em comum com ${otherUser.name} (${otherUser.jobRole})</strong> — ${sorted.length} dia(s) neste mês:</div>
          <div class="common-list">
            ${
              sorted.length
                ? sorted.map((dk) => `<span class="common-tag" onclick="selectDay('${dk}')">${formatDateLabel(dk)}</span>`).join("")
                : `<span style="color:var(--text-secondary);">Nenhum dia em comum registrado neste mês.</span>`
            }
          </div>
        `;
      } else {
        commonBox.classList.add("hidden");
      }

      const targetSched = state.schedules[viewingUserId] || {};
      let html = "";

      for (let w = 0; w < cells.length; w += 7) {
        const weekNum = w / 7 + 1;
        html += `<div class="week-row"><div class="week-label">Sem ${weekNum}</div>`;

        for (let dIdx = 0; dIdx < 7; dIdx++) {
          const c = cells[w + dIdx];
          const dk = formatDateKey(c.year, c.month, c.day);
          const entry = targetSched[dk];
          const holiday = HOLIDAYS[dk];
          const incoming = getIncomingMentionsForDay(viewingUserId, dk);
          const hasText = entry && entry.text && entry.text.trim().length > 0;
          const isCommon = commonFilterActive && selectedCommonUserId && c.inMonth && commonKeys.has(dk);
          const isDimmed = commonFilterActive && selectedCommonUserId && c.inMonth && !isCommon;

          let cls = ["day-square"];
          if (!c.inMonth) cls.push("other-month");
          if (dk === selectedDateKey) cls.push("selected-day");
          if (holiday) cls.push("holiday-day");
          if (isCommon) cls.push("common-highlight");
          if (isDimmed) cls.push("dimmed");
          if (entry && entry.status === "cancelado") cls.push("cancelled-day");

          const mentionChips = (entry && entry.mentions ? entry.mentions : [])
            .map((uid) => `<span class="mention-chip">@${getUserById(uid).name}</span>`)
            .join("");

          html += `
            <div class="${cls.join(" ")}" onclick="selectDay('${dk}')">
              <div class="day-top">
                <span class="day-num">${c.day}</span>
                <div class="day-badges">
                  ${holiday ? `<span class="badge-holiday">${holiday.type === "Ponto Facultativo" ? "Facult." : "Feriado"}</span>` : ""}
                  ${incoming.length ? `<span class="badge-incoming">+${incoming.length} @</span>` : ""}
                  ${entry && entry.status === "cancelado" ? `<span class="badge-cancel">Cancelado</span>` : ""}
                  ${entry && entry.lastEditedAt && entry.status !== "cancelado" ? `<span class="badge-edit">Editado</span>` : ""}
                </div>
              </div>
              ${holiday ? `<div class="holiday-mini-name">${holiday.title}</div>` : ""}
              <div class="day-note-preview ${hasText ? "" : "empty"}">
                ${hasText ? escapeHtml(entry.text) : "Sem anotação"}
              </div>
              ${mentionChips ? `<div class="day-mentions">${mentionChips}</div>` : ""}
            </div>
          `;
        }
        html += `</div>`;
      }

      document.getElementById("weeksContainer").innerHTML = html;
    }

    function selectDay(dateKey) {
      selectedDateKey = dateKey;
      renderSchedule();
      renderDayDrawer();
    }

    function renderDayDrawer() {
      const viewedUser = getUserById(viewingUserId);
      const isMine = viewingUserId === loggedUserId;
      const entry = (state.schedules[viewingUserId] || {})[selectedDateKey];
      const holiday = HOLIDAYS[selectedDateKey];
      const incoming = getIncomingMentionsForDay(viewingUserId, selectedDateKey);

      document.getElementById("drawerDayTitle").textContent = formatDateLabel(selectedDateKey);
      document.getElementById("drawerDaySub").textContent = `Agenda de ${viewedUser.name} (${viewedUser.jobRole})`;

      const editBtn = document.getElementById("drawerEditBtn");
      editBtn.classList.toggle("hidden", !isMine);

      const hBox = document.getElementById("drawerHolidayBox");
      if (holiday) {
        hBox.classList.remove("hidden");
        hBox.innerHTML = `<strong>🟣 ${holiday.type}:</strong> ${holiday.title}`;
      } else {
        hBox.classList.add("hidden");
      }

      const ownerActEl = document.getElementById("drawerOwnerActivity");
      if (entry && (entry.text || "").trim()) {
        const stClass =
          entry.status === "cancelado"
            ? "st-cancelado"
            : entry.status === "pendente"
            ? "st-pendente"
            : "st-confirmado";
        const stText =
          entry.status === "cancelado"
            ? "Cancelado / Ausência"
            : entry.status === "pendente"
            ? "Pendente"
            : "Confirmado";

        ownerActEl.innerHTML = `
          <div class="activity-block-head">
            <span style="color:var(--text-secondary);">🕒 ${entry.shift || "Dia todo"}</span>
            <span class="status-pill-tag ${stClass}">${stText}</span>
          </div>
          <div style="font-size:0.86rem; white-space:pre-line;">${escapeHtml(entry.text)}</div>
          ${entry.lastEditedAt ? `<div style="font-size:0.7rem; color:var(--text-secondary); margin-top:6px;">Atualizado: ${entry.lastEditedAt}</div>` : ""}
        `;
      } else {
        ownerActEl.innerHTML = `
          <div style="font-size:0.82rem; color:var(--text-secondary);">
            Nenhuma atividade registrada neste dia.${isMine ? " Toque em <strong>Editar Dia</strong> para adicionar." : ""}
          </div>
        `;
      }

      const incEl = document.getElementById("drawerIncomingMentions");
      if (!incoming.length) {
        incEl.innerHTML = `<div style="font-size:0.79rem; color:var(--text-secondary);">Nenhum colega marcou ${viewedUser.name} nesta data.</div>`;
      } else {
        incEl.innerHTML = incoming
          .map(
            ({ author, entry: e }) => `
            <div class="activity-block" style="border-left:3px solid ${author.color};">
              <div class="activity-block-head">
                <strong>${author.name} (${author.jobRole})</strong>
                <span style="font-size:0.7rem; color:var(--text-secondary);">${e.shift || "Dia todo"}</span>
              </div>
              <div style="font-size:0.82rem;">${escapeHtml(e.text)}</div>
            </div>
          `
          )
          .join("");
      }
    }

    function openEditModalForSelectedDay() {
      if (viewingUserId !== loggedUserId) return;
      const entry = (state.schedules[loggedUserId] || {})[selectedDateKey] || {
        text: "",
        shift: "Dia todo",
        status: "confirmado",
        mentions: []
      };
      const holiday = HOLIDAYS[selectedDateKey];

      document.getElementById("modalDayTitle").textContent = formatDateLabel(selectedDateKey);
      document.getElementById("modalOwnerInfo").textContent = `Editando meu cronograma (${getUserById(loggedUserId).name})`;

      const hBanner = document.getElementById("modalHolidayBanner");
      if (holiday) {
        hBanner.classList.remove("hidden");
        hBanner.innerHTML = `<strong>🟣 Atenção — ${holiday.type}:</strong> ${holiday.title}`;
      } else {
        hBanner.classList.add("hidden");
      }

      document.getElementById("modalShiftSelect").value = entry.shift || "Dia todo";
      document.getElementById("modalStatusSelect").value = entry.status || "confirmado";
      document.getElementById("modalNoteTextarea").value = entry.text || "";

      document.getElementById("modalMentionPicker").innerHTML = getActiveUsers()
        .filter((u) => u.id !== loggedUserId)
        .map(
          (u) => `<button type="button" class="mention-pick-btn" onclick="insertMentionInModal('${u.name}')">@${u.name} <span style="color:var(--text-secondary);">(${u.jobRole})</span></button>`
        )
        .join("");

      document.getElementById("dayModalBackdrop").classList.add("open");
    }

    function insertMentionInModal(name) {
      const ta = document.getElementById("modalNoteTextarea");
      const prefix = ta.value && !ta.value.endsWith(" ") && !ta.value.endsWith("\n") ? " " : "";
      ta.value += `${prefix}@${name} `;
      ta.focus();
    }

    async function saveDayModal() {
      if (viewingUserId !== loggedUserId) return;
      const text = document.getElementById("modalNoteTextarea").value.trim();
      const shift = document.getElementById("modalShiftSelect").value;
      const status = document.getElementById("modalStatusSelect").value;

      const detectedMentions = getActiveUsers()
        .filter((u) => u.id !== loggedUserId)
        .filter((u) => new RegExp(`@${escapeRegex(u.name)}\\b`, "i").test(text))
        .map((u) => u.id);

      if (!state.schedules[loggedUserId]) state.schedules[loggedUserId] = {};
      const timeLabel = nowTimeLabel();

      state.schedules[loggedUserId][selectedDateKey] = {
        text,
        shift,
        status,
        mentions: detectedMentions,
        lastEditedAt: timeLabel
      };

      const actor = getUserById(loggedUserId);
      detectedMentions.forEach((targetId) => {
        state.alerts.unshift({
          id: "al_" + Date.now() + "_" + targetId,
          type: status === "cancelado" ? "change" : "mention",
          targetUserId: targetId,
          fromUserId: loggedUserId,
          dateKey: selectedDateKey,
          message:
            status === "cancelado"
              ? `${actor.name} (${actor.jobRole}) marcou CANCELADO em ${formatDateLabel(selectedDateKey)}: "${text}"`
              : `${actor.name} (${actor.jobRole}) marcou você em ${formatDateLabel(selectedDateKey)} (${shift}): "${text}"`,
          time: timeLabel,
          read: false
        });
      });

      closeDayModal();
      renderAll();
      await persistState();
    }

    function closeDayModal() {
      document.getElementById("dayModalBackdrop").classList.remove("open");
    }

    function openChatForSelectedDay() {
      activeChatDateKey = selectedDateKey;
      switchTab("alerts");
      renderChat();
    }

    // STATUS DIÁRIO
    function insertMentionIntoStatus() {
      const other = getActiveUsers().find((u) => u.id !== loggedUserId);
      const ta = document.getElementById("statusInput");
      ta.value += (ta.value && !ta.value.endsWith(" ") ? " " : "") + (other ? `@${other.name} ` : "@Colega ");
      ta.focus();
    }

    async function publishDailyStatus() {
      const ta = document.getElementById("statusInput");
      const text = ta.value.trim();
      if (!text) return;

      state.statusPosts = state.statusPosts.filter((p) => p.userId !== loggedUserId);
      state.statusPosts.unshift({
        id: "st_" + Date.now(),
        userId: loggedUserId,
        text,
        updatedAt: nowTimeLabel()
      });

      ta.value = "";
      renderStatusFeed();
      await persistState();
    }

    function renderStatusFeed() {
      const sel = document.getElementById("statusFilterUser");
      const cur = sel.value || "ALL";
      sel.innerHTML =
        `<option value="ALL">Toda a equipe</option>` +
        getActiveUsers()
          .map((u) => `<option value="${u.id}" ${u.id === cur ? "selected" : ""}>${u.name} (${u.jobRole})</option>`)
          .join("");

      const posts = state.statusPosts.filter((p) => {
        const u = getUserById(p.userId);
        if (!u.active) return false;
        return cur === "ALL" || p.userId === cur;
      });

      document.getElementById("statusFeedList").innerHTML = posts.length
        ? posts
            .map((p, idx) => {
              const author = getUserById(p.userId);
              return `
                <div class="status-feed-card ${idx === 0 ? "top-recent" : ""}">
                  <div class="status-card-head">
                    <div style="display:flex; align-items:center; gap:7px; flex-wrap:wrap;">
                      <span class="p-dot" style="background:${author.color}"></span>
                      <strong>${author.name}</strong>
                      <span class="p-role-tag">${author.jobRole}</span>
                      ${idx === 0 ? `<span class="badge-edit" style="background:var(--success-soft); color:#6ee7b7;">Mais recente</span>` : ""}
                    </div>
                    <span style="font-size:0.74rem; color:var(--text-secondary);">${p.updatedAt}</span>
                  </div>
                  <div style="font-size:0.86rem; white-space:pre-line;">${escapeHtml(p.text)}</div>
                </div>
              `;
            })
            .join("")
        : `<div class="status-feed-card" style="color:var(--text-secondary); font-size:0.84rem;">Nenhum status publicado ainda.</div>`;
    }

    // ALERTAS & CHAT
    function renderAlertsAndBadge() {
      const myAlerts = state.alerts.filter((a) => a.targetUserId === loggedUserId);
      const unread = myAlerts.filter((a) => !a.read).length;
      const badge = document.getElementById("alertsBadge");
      badge.textContent = unread;
      badge.classList.toggle("hidden", unread === 0);

      document.getElementById("alertsList").innerHTML = myAlerts.length
        ? myAlerts
            .map(
              (a) => `
              <div class="alert-card ${a.type === "mention" ? "mention-alert" : "change-alert"}">
                <div>
                  <div style="font-size:0.84rem; font-weight:${a.read ? "500" : "700"};">${escapeHtml(a.message)}</div>
                  <div style="font-size:0.72rem; color:var(--text-secondary); margin-top:3px;">${a.time}</div>
                </div>
                <button class="btn-mini" onclick="activeChatDateKey='${a.dateKey || ""}'; renderChat(); document.getElementById('chatInput').focus();">Conversar</button>
              </div>
            `
            )
            .join("")
        : `<div class="alert-card" style="font-size:0.82rem; color:var(--text-secondary);">Nenhuma notificação no momento.</div>`;
    }

    async function markAllAlertsRead() {
      state.alerts.forEach((a) => {
        if (a.targetUserId === loggedUserId) a.read = true;
      });
      renderAlertsAndBadge();
      await persistState();
    }

    function renderChat() {
      document.getElementById("chatContextBadge").textContent = activeChatDateKey
        ? `Assunto: ${formatDateLabel(activeChatDateKey)}`
        : "Assunto: Geral da Equipe";

      const box = document.getElementById("chatMessages");
      box.innerHTML = state.chatMessages.length
        ? state.chatMessages
            .map((m) => {
              const s = getUserById(m.fromUserId);
              return `
                <div class="msg-item">
                  <div class="msg-head">
                    <strong style="color:${s.color}">${s.name} (${s.jobRole})</strong>
                    <span>${m.contextDateKey ? formatDateLabel(m.contextDateKey) + " • " : ""}${m.time}</span>
                  </div>
                  <div>${escapeHtml(m.text)}</div>
                </div>
              `;
            })
            .join("")
        : `<div style="font-size:0.8rem; color:var(--text-secondary);">Sem mensagens ainda.</div>`;
      box.scrollTop = box.scrollHeight;
    }

    async function sendChatMessage(e) {
      e.preventDefault();
      const input = document.getElementById("chatInput");
      const text = input.value.trim();
      if (!text) return;

      const dt = new Date();
      state.chatMessages.push({
        id: "msg_" + Date.now(),
        fromUserId: loggedUserId,
        contextDateKey: activeChatDateKey,
        text,
        time: `${String(dt.getHours()).padStart(2, "0")}:${String(dt.getMinutes()).padStart(2, "0")}`
      });
      input.value = "";
      renderChat();
      await persistState();
    }

    // EQUIPE / PROPRIETÁRIO
    function renderTeamTab() {
      const me = getUserById(loggedUserId);
      document.getElementById("ownerControls").classList.toggle("hidden", me.sysRole !== "owner");

      const active = getActiveUsers();
      document.getElementById("activeMembersCount").textContent = active.length;

      document.getElementById("membersList").innerHTML = active
        .map((u) => {
          const canRemove = me.sysRole === "owner" && u.sysRole !== "owner";
          return `
            <div class="member-row">
              <div style="display:flex; align-items:center; gap:7px; flex-wrap:wrap;">
                <span class="p-dot" style="background:${u.color}"></span>
                <strong>${u.name}</strong>
                <span class="p-role-tag">${u.jobRole}</span>
                ${u.email ? `<span style="font-size:0.72rem; color:var(--text-secondary);">(${u.email})</span>` : `<span style="font-size:0.72rem; color:var(--warning);">(Aguardando 1º acesso)</span>`}
              </div>
              <div style="display:flex; gap:6px;">
                <button class="btn-mini" onclick="switchTab('schedule'); viewParticipantSchedule('${u.id}')">Ver agenda</button>
                ${canRemove ? `<button class="btn-mini" style="background:var(--danger-soft); color:#fca5a5; border-color:rgba(239,68,68,0.4);" onclick="removeCollaborator('${u.id}')">Remover</button>` : ""}
              </div>
            </div>
          `;
        })
        .join("");
    }

    async function addCollaborator() {
      const me = getUserById(loggedUserId);
      if (me.sysRole !== "owner") return;

      const name = document.getElementById("newMemberName").value.trim();
      const jobRole = document.getElementById("newMemberRole").value.trim() || "Colaborador";
      const email = document.getElementById("newMemberEmail").value.trim().toLowerCase();
      if (!name) return;

      if (getActiveUsers().length >= 20) {
        alert("Limite de 20 participantes ativos atingido.");
        return;
      }

      state.users.push({
        id: "u_" + Date.now(),
        name,
        jobRole,
        sysRole: "collab",
        email,
        color: PALETTE[state.users.length % PALETTE.length],
        active: true
      });

      document.getElementById("newMemberName").value = "";
      document.getElementById("newMemberRole").value = "";
      document.getElementById("newMemberEmail").value = "";
      renderAll();
      await persistState();
    }

    async function removeCollaborator(uid) {
      const me = getUserById(loggedUserId);
      if (me.sysRole !== "owner" || uid === OWNER_ID) return;
      const target = state.users.find((u) => u.id === uid);
      if (target) {
        target.active = false;
        if (viewingUserId === uid) viewingUserId = loggedUserId;
        if (selectedCommonUserId === uid) selectedCommonUserId = null;
        renderAll();
        await persistState();
      }
    }

    function switchTab(tab) {
      ["schedule", "status", "alerts", "team"].forEach((t) => {
        document.getElementById("tab-" + t).classList.toggle("hidden", t !== tab);
        document.getElementById("nav-" + t).classList.toggle("active", t === tab);
      });
      if (tab === "alerts") renderChat();
    }

    function escapeHtml(str) {
      return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
    }

    function escapeRegex(str) {
      return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    }

    function renderAll() {
      renderTopHeader();
      renderParticipantsBar();
      renderSchedule();
      renderDayDrawer();
      renderStatusFeed();
      renderAlertsAndBadge();
      renderChat();
      renderTeamTab();
    }

    // Boot
    populateLoginSelect();
    const savedSessionUid = localStorage.getItem(SESSION_KEY);
    if (savedSessionUid && getActiveUsers().some((u) => u.id === savedSessionUid)) {
      loggedUserId = savedSessionUid;
      viewingUserId = savedSessionUid;
      document.getElementById("loginScreen").classList.add("hidden");
      document.getElementById("appShell").classList.remove("hidden");
      initAppUI();
    }
  </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print("Arquivo index.html criado com sucesso.")