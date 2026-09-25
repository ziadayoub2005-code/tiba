import os

base64_path = "/Users/mac/Desktop/tiba/tiba_logo_base64.txt"
with open(base64_path, "r") as f:
    logo_b64 = f.read().strip()

html_content = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>منصة استمارة بحث التخرج - معاهد طيبة العليا</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=Amiri:wght@400;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #2563eb;
      --primary-hover: #1d4ed8;
      --accent: #38bdf8;
      --surface-dark: #0b1120;
      --surface-card: #0f172a;
      --surface-panel: #1e293b;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --border-dark: #334155;
      --success: #10b981;
      --danger: #ef4444;
      --warning: #f59e0b;
      --purple: #8b5cf6;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
      -webkit-tap-highlight-color: transparent;
    }}

    body {{
      font-family: 'Cairo', system-ui, -apple-system, sans-serif;
      background-color: var(--surface-dark);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    /* Global Navbar */
    header.app-navbar {{
      background: rgba(15, 23, 42, 0.96);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border-dark);
      padding: 10px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
      gap: 12px;
    }}

    .navbar-brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      user-select: none;
    }}

    .navbar-brand .brand-icon {{
      width: 40px;
      height: 40px;
      min-width: 40px;
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
    }}

    .navbar-brand h1 {{
      font-size: 1.05rem;
      font-weight: 800;
      color: #fff;
      line-height: 1.2;
    }}

    .navbar-brand span.subtitle {{
      font-size: 0.72rem;
      color: var(--text-muted);
      display: block;
      font-weight: 500;
    }}

    .navbar-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    /* Role Pill Badge */
    .role-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 0.78rem;
      font-weight: 700;
      border: 1px solid transparent;
      transition: all 0.2s;
    }}

    .role-badge.student {{
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.3);
    }}

    .role-badge.admin {{
      background: rgba(139, 92, 246, 0.2);
      color: #c084fc;
      border-color: rgba(139, 92, 246, 0.4);
    }}

    /* Buttons */
    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 7px 14px;
      font-size: 0.85rem;
      font-weight: 700;
      font-family: inherit;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      border: 1px solid transparent;
      user-select: none;
      white-space: nowrap;
    }}

    .btn:active {{
      transform: scale(0.97);
    }}

    .btn-primary {{
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
    }}
    .btn-primary:hover {{
      background: linear-gradient(135deg, #1d4ed8, #1e40af);
      box-shadow: 0 6px 18px rgba(37, 99, 235, 0.45);
    }}

    .btn-admin {{
      background: linear-gradient(135deg, #7c3aed, #6d28d9);
      color: #fff;
      box-shadow: 0 4px 12px rgba(124, 58, 237, 0.35);
    }}
    .btn-admin:hover {{
      background: linear-gradient(135deg, #6d28d9, #5b21b6);
    }}

    .btn-secondary {{
      background: #1e293b;
      color: #cbd5e1;
      border-color: #334155;
    }}
    .btn-secondary:hover {{
      background: #334155;
      color: #fff;
    }}

    .btn-outline {{
      background: transparent;
      color: #cbd5e1;
      border-color: #475569;
    }}
    .btn-outline:hover {{
      background: rgba(255, 255, 255, 0.08);
      color: #fff;
    }}

    .btn-sm {{
      padding: 5px 10px;
      font-size: 0.78rem;
      border-radius: 6px;
    }}

    /* ========================================================
       VIEW 1: TEMPLATES GALLERY (STUDENT DISCOVERY)
       ======================================================== */
    .view-gallery {{
      flex: 1;
      max-width: 1200px;
      width: 100%;
      margin: 0 auto;
      padding: 30px 20px 60px 20px;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }}

    .gallery-hero {{
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.95));
      border: 1px solid #334155;
      border-radius: 16px;
      padding: 28px 24px;
      text-align: center;
      position: relative;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }}

    .gallery-hero h2 {{
      font-size: 1.6rem;
      font-weight: 900;
      color: #fff;
      margin-bottom: 8px;
    }}

    .gallery-hero p {{
      color: #94a3b8;
      font-size: 0.95rem;
      max-width: 600px;
      margin: 0 auto 20px auto;
      line-height: 1.6;
    }}

    .search-filter-box {{
      max-width: 680px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .search-input-wrapper {{
      position: relative;
      width: 100%;
    }}

    .search-input-wrapper svg {{
      position: absolute;
      right: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: #64748b;
    }}

    .search-input {{
      width: 100%;
      background: #0f172a;
      border: 1.5px solid #334155;
      border-radius: 12px;
      padding: 12px 44px 12px 16px;
      color: #fff;
      font-family: inherit;
      font-size: 0.95rem;
      transition: all 0.2s;
    }}
    .search-input:focus {{
      outline: none;
      border-color: #38bdf8;
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
    }}

    .dept-filter-pills {{
      display: flex;
      gap: 8px;
      justify-content: center;
      flex-wrap: wrap;
    }}

    .filter-pill {{
      padding: 6px 14px;
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 700;
      color: #94a3b8;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .filter-pill:hover, .filter-pill.active {{
      background: #2563eb;
      color: #fff;
      border-color: #3b82f6;
    }}

    /* Template Cards Grid */
    .templates-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 20px;
    }}
    @media (min-width: 640px) {{
      .templates-grid {{
        grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      }}
    }}

    .template-card {{
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 14px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
      overflow: hidden;
    }}

    .template-card:hover {{
      transform: translateY(-4px);
      border-color: #3b82f6;
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.4);
    }}

    .template-card-header {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
    }}

    .card-dept-icon {{
      width: 44px;
      height: 44px;
      min-width: 44px;
      border-radius: 10px;
      background: rgba(37, 99, 235, 0.12);
      border: 1px solid rgba(37, 99, 235, 0.3);
      color: #38bdf8;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .card-meta {{
      flex: 1;
    }}

    .card-dept-tag {{
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 700;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.1);
      padding: 2px 8px;
      border-radius: 4px;
    }}

    .status-pill {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 9999px;
      letter-spacing: 0.2px;
      line-height: 1.3;
    }}

    .status-pill.status-published {{
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.35);
    }}

    .status-pill.status-draft {{
      background: rgba(245, 158, 11, 0.15);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.35);
    }}

    .card-title {{
      font-size: 1.05rem;
      font-weight: 800;
      color: #f8fafc;
      line-height: 1.35;
    }}

    .card-details {{
      background: #1e293b;
      border-radius: 8px;
      padding: 10px 12px;
      font-size: 0.8rem;
      color: #94a3b8;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .card-detail-item {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .card-detail-item span.val {{
      color: #e2e8f0;
      font-weight: 600;
    }}

    .template-card-footer {{
      display: flex;
      gap: 8px;
      margin-top: auto;
    }}

    /* ========================================================
       VIEW 2: WORKSPACE (STUDENT FILLER / ADMIN BUILDER)
       ======================================================== */
    .app-workspace {{
      display: none;
      flex: 1;
      height: calc(100vh - 61px);
      overflow: hidden;
      position: relative;
    }}
    .app-workspace.active {{
      display: flex;
    }}

    /* Mobile Segmented Switcher */
    .mobile-tab-bar {{
      display: none;
      background: #0f172a;
      border-bottom: 1px solid #1e293b;
      padding: 8px 12px;
      position: sticky;
      top: 61px;
      z-index: 90;
    }}

    .segmented-switch {{
      display: flex;
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 10px;
      padding: 3px;
      gap: 3px;
      width: 100%;
    }}

    .segmented-btn {{
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 8px 12px;
      border: none;
      border-radius: 8px;
      background: transparent;
      color: #94a3b8;
      font-family: inherit;
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .segmented-btn.active {{
      background: #2563eb;
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.4);
    }}

    /* Sidebar / Control Panel */
    aside.control-panel {{
      width: 440px;
      min-width: 440px;
      max-width: 440px;
      background: #0f172a;
      border-left: 1px solid var(--border-dark);
      display: flex;
      flex-direction: column;
      height: 100%;
      overflow-y: auto;
      scrollbar-width: thin;
      scrollbar-color: #334155 #0f172a;
      z-index: 40;
    }}

    .panel-section {{
      padding: 16px 18px;
      border-bottom: 1px solid #1e293b;
    }}

    .section-title {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.92rem;
      font-weight: 800;
      color: #f1f5f9;
      margin-bottom: 12px;
    }}

    .section-title svg {{
      color: var(--accent);
      flex-shrink: 0;
    }}

    /* Permanent Student Instructions Box in Sidebar */
    .student-instructions-card {{
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(6, 95, 70, 0.15));
      border: 1.5px solid rgba(16, 185, 129, 0.4);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
    }}

    .instructions-card-header {{
      display: flex;
      align-items: center;
      gap: 8px;
      color: #34d399;
      font-weight: 900;
      font-size: 1rem;
    }}

    .instructions-list {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      font-size: 0.82rem;
      color: #e2e8f0;
      line-height: 1.5;
    }}

    .instructions-list-item {{
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }}

    .instructions-list-item span.icon {{
      color: #34d399;
      font-weight: bold;
    }}

    /* Admin Action Banner */
    .admin-action-banner {{
      background: rgba(139, 92, 246, 0.12);
      border: 1px solid rgba(139, 92, 246, 0.35);
      border-radius: 10px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .form-group {{
      margin-bottom: 12px;
    }}
    .form-group:last-child {{
      margin-bottom: 0;
    }}

    .form-label {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.8rem;
      font-weight: 700;
      color: #cbd5e1;
      margin-bottom: 5px;
    }}

    .form-label span.optional {{
      color: #64748b;
      font-weight: normal;
      font-size: 0.72rem;
    }}

    .form-control {{
      width: 100%;
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 8px;
      color: #fff;
      font-family: inherit;
      font-size: 0.86rem;
      padding: 8px 11px;
      transition: all 0.2s;
    }}

    .form-control:focus {{
      outline: none;
      border-color: #38bdf8;
      box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2);
    }}

    /* Stepper & Presets */
    .row-controls-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin-top: 8px;
    }}

    .stepper-container {{
      display: flex;
      align-items: center;
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 8px;
      overflow: hidden;
    }}

    .stepper-btn {{
      background: transparent;
      border: none;
      color: #cbd5e1;
      width: 42px;
      height: 40px;
      font-size: 1.25rem;
      font-weight: bold;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.15s;
    }}
    .stepper-btn:hover {{
      background: #334155;
      color: #fff;
    }}

    .stepper-input {{
      flex: 1;
      background: transparent;
      border: none;
      color: #fff;
      text-align: center;
      font-size: 0.95rem;
      font-weight: 800;
      min-width: 40px;
    }}
    .stepper-input:focus {{
      outline: none;
    }}

    .presets-group {{
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin-top: 10px;
    }}

    .preset-pill {{
      padding: 5px 11px;
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 20px;
      font-size: 0.76rem;
      color: #94a3b8;
      cursor: pointer;
      font-weight: 700;
      transition: all 0.15s;
    }}
    .preset-pill:hover, .preset-pill.active {{
      background: #2563eb;
      color: #fff;
      border-color: #3b82f6;
    }}

    /* Columns Manager (Admin) */
    .columns-list {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 12px;
    }}

    .column-item {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: #1e293b;
      border: 1px solid #334155;
      padding: 6px 10px;
      border-radius: 8px;
    }}

    .column-item input.col-name-input {{
      flex: 1;
      background: transparent;
      border: 1px solid transparent;
      border-radius: 4px;
      color: #fff;
      font-family: inherit;
      font-size: 0.84rem;
      font-weight: 600;
      padding: 4px 6px;
      min-width: 0;
    }}
    .column-item input.col-name-input:focus {{
      background: #0f172a;
      border-color: #38bdf8;
      outline: none;
    }}

    .column-actions {{
      display: flex;
      align-items: center;
      gap: 4px;
      flex-shrink: 0;
    }}

    .col-icon-btn {{
      background: transparent;
      border: none;
      color: #94a3b8;
      width: 28px;
      height: 28px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s;
    }}
    .col-icon-btn:hover {{
      background: #334155;
      color: #f1f5f9;
    }}
    .col-icon-btn.delete-col:hover {{
      background: rgba(239, 68, 68, 0.2);
      color: #ef4444;
    }}

    /* Logo Control Box */
    .logo-control-box {{
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 10px;
      padding: 12px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    .logo-preview-row {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .logo-thumbnail {{
      width: 60px;
      height: 60px;
      min-width: 60px;
      background: #fff;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 4px;
      border: 1px solid #475569;
      overflow: hidden;
    }}

    .logo-thumbnail img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }}

    .logo-buttons {{
      display: flex;
      flex-direction: column;
      gap: 6px;
      flex: 1;
    }}

    /* Main Preview Canvas Area */
    main.canvas-area {{
      flex: 1;
      background: #111827;
      background-image: 
        radial-gradient(#1f2937 1px, transparent 1px),
        radial-gradient(#1f2937 1px, #111827 1px);
      background-size: 20px 20px;
      background-position: 0 0, 10px 10px;
      position: relative;
      overflow-y: auto;
      overflow-x: auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 16px 16px 80px 16px;
      scrollbar-width: thin;
      scrollbar-color: #334155 #111827;
      -webkit-overflow-scrolling: touch;
    }}

    /* Top Instruction Banner for Student (Always visible in any template) */
    .student-top-guide-bar {{
      width: 100%;
      max-width: 210mm;
      background: linear-gradient(135deg, rgba(15, 23, 42, 0.98), rgba(30, 41, 59, 0.95));
      border: 1.5px solid rgba(56, 189, 248, 0.45);
      border-radius: 14px;
      padding: 14px 18px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45), 0 0 0 1px rgba(56, 189, 248, 0.15);
    }}

    .guide-bar-content {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      line-height: 1.5;
    }}

    .guide-bar-icon-wrap {{
      width: 38px;
      height: 38px;
      min-width: 38px;
      border-radius: 10px;
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.35);
      color: #38bdf8;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
    }}

    .guide-bar-title {{
      font-size: 0.95rem;
      font-weight: 800;
      color: #38bdf8;
      margin-bottom: 3px;
    }}

    .guide-bar-instructions {{
      font-size: 0.85rem;
      color: #cbd5e1;
    }}

    .guide-bar-instructions strong {{
      color: #fff;
    }}

    .guide-bar-content {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 0.85rem;
      color: #e2e8f0;
      line-height: 1.4;
    }}

    .guide-bar-tag {{
      background: rgba(16, 185, 129, 0.2);
      color: #34d399;
      border: 1px solid rgba(16, 185, 129, 0.4);
      padding: 3px 10px;
      border-radius: 6px;
      font-weight: 800;
      font-size: 0.78rem;
      white-space: nowrap;
    }}

    /* Zoom Bar */
    .zoom-toolbar {{
      position: sticky;
      top: 10px;
      z-index: 50;
      background: rgba(15, 23, 42, 0.92);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 30px;
      padding: 5px 12px;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.45);
      margin-bottom: 14px;
      flex-wrap: wrap;
      justify-content: center;
    }}

    .zoom-text {{
      font-size: 0.8rem;
      font-weight: 700;
      color: #cbd5e1;
      min-width: 44px;
      text-align: center;
    }}

    /* Paper Viewport & Scale Container (Perfect Centering, Zero Cutoff) */
    .paper-viewport {{
      width: 100%;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      min-height: calc(100vh - 180px);
      overflow-x: hidden;
      padding: 0 4px;
    }}

    .paper-scale-container {{
      position: relative;
      margin: 0 auto;
      flex-shrink: 0;
    }}

    .paper-wrapper {{
      position: absolute;
      top: 0;
      right: 0;
      transform-origin: top right;
      transition: transform 0.15s ease-out;
      width: 210mm;
      height: 297mm;
    }}

    /* The Real A4 Sheet */
    .a4-page {{
      width: 210mm;
      height: 297mm;
      min-height: 297mm;
      max-height: 297mm;
      background: #ffffff;
      color: #000000;
      box-shadow: 0 14px 45px rgba(0, 0, 0, 0.5);
      position: relative;
      display: flex;
      flex-direction: column;
      padding: 13mm 14mm;
      box-sizing: border-box;
      overflow: hidden;
      font-family: 'Amiri', 'Cairo', 'Traditional Arabic', serif;
    }}

    /* Academic Double Official Border */
    .a4-page::before {{
      content: "";
      position: absolute;
      top: 6mm;
      left: 6mm;
      right: 6mm;
      bottom: 6mm;
      border: 2.5px solid #000;
      pointer-events: none;
    }}

    .a4-page::after {{
      content: "";
      position: absolute;
      top: 8mm;
      left: 8mm;
      right: 8mm;
      bottom: 8mm;
      border: 1px solid #000;
      pointer-events: none;
    }}

    /* Corner Ornaments */
    .corner-decor {{
      position: absolute;
      width: 14px;
      height: 14px;
      border: 2px solid #000;
      pointer-events: none;
      z-index: 2;
    }}
    .corner-tl {{ top: 6.5mm; left: 6.5mm; border-right: none; border-bottom: none; }}
    .corner-tr {{ top: 6.5mm; right: 6.5mm; border-left: none; border-bottom: none; }}
    .corner-bl {{ bottom: 6.5mm; left: 6.5mm; border-right: none; border-top: none; }}
    .corner-br {{ bottom: 6.5mm; right: 6.5mm; border-left: none; border-top: none; }}

    /* Page Content Structure */
    .page-content {{
      position: relative;
      z-index: 5;
      display: flex;
      flex-direction: column;
      height: 100%;
      justify-content: space-between;
    }}

    /* Header */
    .form-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 10px;
      user-select: none;
    }}

    .header-institute-col {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .institute-logo-img {{
      max-height: 58px;
      max-width: 110px;
      object-fit: contain;
      display: block;
    }}

    .institute-text-lines {{
      text-align: right;
      line-height: 1.25;
    }}

    .institute-text-lines .inst-title {{
      font-size: 13pt;
      font-weight: 700;
      color: #000;
      font-family: 'Amiri', 'Cairo', serif;
    }}

    .institute-text-lines .inst-sub {{
      font-size: 10pt;
      color: #111;
      font-weight: 600;
    }}

    .institute-text-lines .inst-dept {{
      font-size: 9.5pt;
      color: #222;
      font-weight: 600;
    }}

    .header-left-badge {{
      text-align: left;
      font-size: 9.5pt;
      line-height: 1.35;
      font-weight: 600;
    }}

    .header-left-badge .year-badge {{
      display: inline-block;
      border: 1px solid #000;
      padding: 3px 8px;
      font-size: 9pt;
      font-weight: bold;
      border-radius: 4px;
      background: #fafafa;
    }}

    /* Title */
    .form-title-wrapper {{
      text-align: center;
      margin: 6px 0 14px 0;
      position: relative;
    }}

    .form-main-title {{
      font-size: 18.5pt;
      font-weight: 800;
      color: #000;
      line-height: 1.3;
      padding: 0 10px;
      display: inline-block;
      outline: none;
      font-family: 'Amiri', 'Cairo', serif;
      user-select: none;
    }}

    .form-title-divider {{
      width: 82%;
      margin: 5px auto 0 auto;
      border-bottom: 2px solid #000;
      position: relative;
    }}

    .form-title-divider::after {{
      content: "";
      position: absolute;
      top: 3px;
      left: 10%;
      right: 10%;
      border-bottom: 1px solid #000;
    }}

    /* Project Meta Information (Fixed/Official Dotted Lines) */
    .project-meta-box {{
      margin: 8px 0 14px 0;
      display: flex;
      flex-direction: column;
      gap: 9px;
      user-select: none;
    }}

    .meta-row {{
      display: flex;
      align-items: baseline;
      font-size: 11.5pt;
      font-weight: 700;
      line-height: 1.4;
    }}

    .meta-label {{
      white-space: nowrap;
      color: #000;
      margin-left: 10px;
      font-weight: 800;
      font-size: 11.5pt;
    }}

    .meta-line-container {{
      flex: 1;
      position: relative;
      min-height: 22px;
      display: flex;
      align-items: center;
    }}

    .meta-value-text {{
      position: relative;
      z-index: 2;
      padding: 0 4px;
      color: #0f172a;
      font-weight: 700;
      font-size: 11pt;
      outline: none;
    }}

    .meta-dotted-line {{
      position: absolute;
      bottom: 4px;
      left: 0;
      right: 0;
      border-bottom: 1.5px dotted #333;
      z-index: 1;
    }}

    /* ========================================================
       TABLE STYLING: STRICT RIGHT-TO-LEFT ALIGNMENT
       ======================================================== */
    .table-container {{
      width: 100%;
      margin: 6px 0 12px 0;
      flex: 1;
      display: flex;
      flex-direction: column;
    }}

    table.students-table {{
      width: 100%;
      border-collapse: collapse;
      table-layout: fixed;
      font-size: 10.5pt;
      border: 2px solid #000;
      direction: rtl;
    }}

    table.students-table th, 
    table.students-table td {{
      border: 1px solid #000;
      line-height: 1.25;
      vertical-align: middle;
      box-sizing: border-box;
      word-wrap: break-word;
      overflow-wrap: break-word;
      direction: rtl !important;
      text-align: right !important; /* All columns align right */
      padding: 4px 10px !important; /* Clean right padding */
      unicode-bidi: plaintext !important; /* Starts typing at the right border */
    }}

    /* Table Header */
    table.students-table th {{
      background-color: #f1f5f9;
      color: #000;
      font-weight: 800;
      font-size: 11pt;
      padding: 6px 10px !important;
      border-bottom: 2px solid #000;
      font-family: 'Amiri', 'Cairo', serif;
      text-align: right !important;
    }}

    /* Sequence Column (م) is centered */
    table.students-table th.col-seq-cell,
    table.students-table td.col-seq-cell {{
      text-align: center !important;
      padding: 4px 2px !important;
    }}

    /* Table Cells (Editable by student from right to left) */
    table.students-table td {{
      font-weight: 600;
      outline: none;
      height: 24px;
      background: #ffffff;
      cursor: text;
    }}

    table.students-table td:focus {{
      background: #eff6ff !important;
      outline: 1.5px dashed #2563eb !important;
    }}

    /* Signatures Section */
    .form-footer-signatures {{
      margin-top: 12px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      padding: 4px 20px 2px 20px;
      user-select: none;
    }}

    .signature-block {{
      text-align: center;
      min-width: 160px;
    }}

    .signature-title {{
      font-size: 11.5pt;
      font-weight: 800;
      color: #000;
      margin-bottom: 18px;
    }}

    .signature-name {{
      font-size: 12.5pt;
      font-weight: 800;
      color: #000;
      font-family: 'Amiri', 'Cairo', serif;
    }}

    .signature-dots {{
      letter-spacing: 2px;
      color: #444;
      font-size: 10pt;
    }}

    /* Toast Notification */
    .edit-hint-toast {{
      position: fixed;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(8px);
      border: 1px solid #334155;
      border-radius: 20px;
      padding: 8px 16px;
      color: #94a3b8;
      font-size: 0.78rem;
      pointer-events: none;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4);
      z-index: 80;
      white-space: nowrap;
    }}

    /* Modals */
    .modal-backdrop {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(4px);
      z-index: 999;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }}
    .modal-backdrop.active {{
      display: flex;
    }}

    .modal-card {{
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 14px;
      max-width: 480px;
      width: 100%;
      padding: 22px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
      text-align: right;
    }}

    .modal-card h3 {{
      font-size: 1.15rem;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
      color: #fff;
    }}

    .modal-card p {{
      font-size: 0.88rem;
      color: #cbd5e1;
      line-height: 1.6;
      margin-bottom: 14px;
    }}

    .password-input-wrap {{
      position: relative;
      display: flex;
      align-items: center;
    }}

    .password-toggle-btn {{
      position: absolute;
      left: 10px;
      background: transparent;
      border: none;
      color: #94a3b8;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 4px;
    }}
    .password-toggle-btn:hover {{
      color: #fff;
    }}

    .print-tip-item {{
      background: #1e293b;
      padding: 10px 12px;
      border-radius: 8px;
      margin-bottom: 8px;
      font-size: 0.82rem;
      color: #94a3b8;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .print-tip-item strong {{
      color: #f1f5f9;
    }}

    /* Media Print */
    @media print {{
      @page {{
        size: A4 portrait;
        margin: 0;
      }}

      html, body {{
        background: #ffffff !important;
        color: #000000 !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 210mm !important;
        height: 297mm !important;
        overflow: visible !important;
      }}

      header.app-navbar,
      aside.control-panel,
      .mobile-tab-bar,
      .zoom-toolbar,
      .edit-hint-toast,
      .modal-backdrop,
      .view-gallery,
      .student-top-guide-bar,
      .no-print {{
        display: none !important;
      }}

      .app-workspace {{
        display: block !important;
        height: auto !important;
        overflow: visible !important;
      }}

      main.canvas-area {{
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
        overflow: visible !important;
        display: block !important;
        height: auto !important;
        width: 210mm !important;
      }}

      .paper-viewport {{
        display: block !important;
        min-height: auto !important;
        height: auto !important;
      }}

      .paper-viewport,
      .paper-scale-container,
      .paper-wrapper {{
        display: block !important;
        position: static !important;
        transform: none !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 210mm !important;
        height: 297mm !important;
        overflow: visible !important;
      }}

      .a4-page {{
        box-shadow: none !important;
        width: 210mm !important;
        height: 297mm !important;
        max-height: 297mm !important;
        min-height: 297mm !important;
        margin: 0 !important;
        page-break-after: avoid !important;
        page-break-inside: avoid !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}

      table.students-table th {{
        background-color: #f1f5f9 !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}
    }}

    /* ========================================================
       RESPONSIVE BREAKPOINTS (ALL SCREEN SIZES)
       ======================================================== */
    @media (min-width: 1025px) {{
      aside.control-panel {{
        display: flex !important;
      }}
      main.canvas-area {{
        display: flex !important;
      }}
      .mobile-tab-bar {{
        display: none !important;
      }}
    }}

    @media (max-width: 1024px) {{
      header.app-navbar {{
        padding: 10px 14px;
      }}

      .mobile-tab-bar {{
        display: block;
      }}

      .app-workspace {{
        height: calc(100vh - 110px);
      }}

      aside.control-panel {{
        width: 100%;
        min-width: 100%;
        max-width: 100%;
        border-left: none;
        display: block;
      }}

      main.canvas-area {{
        display: none;
        width: 100%;
        padding: 14px 10px 60px 10px;
      }}

      body.show-preview-mode aside.control-panel {{
        display: none;
      }}
      body.show-preview-mode main.canvas-area {{
        display: flex;
      }}
    }}

    @media (max-width: 768px) {{
      /* Top Navbar Mobile Optimization */
      header.app-navbar {{
        padding: 8px 10px !important;
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 8px !important;
      }}

      .navbar-brand {{
        width: 100% !important;
        justify-content: space-between !important;
      }}

      .navbar-brand h1 {{
        font-size: 0.95rem !important;
        line-height: 1.2 !important;
      }}
      .navbar-brand span.subtitle {{
        display: none !important;
      }}

      .navbar-actions {{
        width: 100% !important;
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        gap: 4px !important;
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
      }}

      .navbar-actions .btn {{
        padding: 6px 8px !important;
        font-size: 0.75rem !important;
        white-space: nowrap !important;
        flex: 1 !important;
      }}

      .navbar-actions #btnPrintPdf {{
        flex: 1.5 !important;
        padding: 7px 10px !important;
        font-size: 0.82rem !important;
      }}

      .role-badge {{
        padding: 4px 8px !important;
        font-size: 0.72rem !important;
        white-space: nowrap !important;
      }}

      /* Gallery Mobile Spacing */
      .view-gallery {{
        padding: 14px 10px 50px 10px !important;
        gap: 14px !important;
      }}

      .gallery-hero {{
        padding: 16px 12px !important;
        border-radius: 12px !important;
      }}

      .gallery-hero h2 {{
        font-size: 1.25rem !important;
      }}

      .gallery-hero p {{
        font-size: 0.84rem !important;
        margin-bottom: 14px !important;
      }}

      .dept-filter-pills {{
        gap: 5px !important;
      }}

      .filter-pill {{
        padding: 5px 9px !important;
        font-size: 0.72rem !important;
      }}

      /* Admin Action Banner in Gallery on Mobile (Fixing Buttons Overflow) */
      #adminGalleryActions {{
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 12px !important;
        padding: 12px 14px !important;
        text-align: center !important;
      }}

      #adminGalleryActions > div:first-child {{
        justify-content: center !important;
        font-size: 0.82rem !important;
      }}

      #adminGalleryActions > div:last-child {{
        display: flex !important;
        flex-direction: column !important;
        gap: 8px !important;
        width: 100% !important;
      }}

      #adminGalleryActions button {{
        width: 100% !important;
        justify-content: center !important;
        padding: 9px 12px !important;
      }}

      /* Template Cards Mobile */
      .templates-grid {{
        grid-template-columns: 1fr !important;
        gap: 14px !important;
      }}

      .template-card {{
        padding: 16px !important;
      }}

      /* Canvas & Guide Banner Mobile */
      main.canvas-area {{
        padding: 8px 4px 60px 4px !important;
        overflow-x: hidden !important;
      }}

      .student-top-guide-bar {{
        padding: 10px 12px !important;
        margin-bottom: 12px !important;
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 10px !important;
        border-radius: 10px !important;
      }}

      .guide-bar-title {{
        font-size: 0.88rem !important;
      }}

      .guide-bar-instructions {{
        font-size: 0.78rem !important;
        line-height: 1.45 !important;
      }}

      .student-top-guide-bar button {{
        width: 100% !important;
        justify-content: center !important;
      }}

      .zoom-toolbar {{
        padding: 4px 8px !important;
        gap: 5px !important;
        margin-bottom: 10px !important;
      }}

      .zoom-toolbar .btn {{
        font-size: 0.72rem !important;
        padding: 3px 8px !important;
      }}

      .mobile-tab-bar {{
        top: 53px;
        padding: 6px 10px;
      }}
      .app-workspace {{
        height: calc(100vh - 105px);
      }}
      .panel-section {{
        padding: 14px;
      }}
      .edit-hint-toast {{
        display: none;
      }}
    }}

    @media (max-width: 380px) {{
      .navbar-brand .brand-icon {{
        width: 30px !important;
        height: 30px !important;
        min-width: 30px !important;
      }}
      .navbar-brand h1 {{
        font-size: 0.85rem !important;
      }}
      .navbar-actions .btn {{
        padding: 5px 6px !important;
        font-size: 0.7rem !important;
      }}
    }}
  
    /* ========================================================
       STUDENT & ADMIN WORKSPACE LAYOUT (ROLE DRIVEN)
       ======================================================== */
    /* Student Mode: Entire right sidebar is completely removed! Student gets 100% full screen preview! */
    body.role-student aside.control-panel {{
      display: none !important;
    }}
    body.role-student .mobile-tab-bar {{
      display: none !important;
    }}
    body.role-student main.canvas-area {{
      display: flex !important;
      width: 100% !important;
      flex: 1 1 100% !important;
    }}

    /* Admin Mode: Sidebar is enabled */
    body.role-admin aside.control-panel {{
      display: flex !important;
    }}
    @media (max-width: 1024px) {{
      body.role-admin .mobile-tab-bar {{
        display: block !important;
      }}
      body.role-admin:not(.show-preview-mode) aside.control-panel {{
        display: block !important;
      }}
      body.role-admin:not(.show-preview-mode) main.canvas-area {{
        display: none !important;
      }}
      body.role-admin.show-preview-mode aside.control-panel {{
        display: none !important;
      }}
      body.role-admin.show-preview-mode main.canvas-area {{
        display: flex !important;
      }}
    }}

    /* ========================================================
       SWEETALERT 2 STYLE CONFIRMATION MODAL & TOAST
       ======================================================== */
    .swal-backdrop {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(11, 17, 32, 0.88);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      z-index: 9999;
      align-items: center;
      justify-content: center;
      padding: 16px;
      opacity: 0;
      transition: opacity 0.2s ease-out;
    }}
    .swal-backdrop.active {{
      display: flex;
      opacity: 1;
    }}

    .swal-card {{
      background: #0f172a;
      border: 1.5px solid #334155;
      border-radius: 22px;
      max-width: 440px;
      width: 100%;
      padding: 30px 24px 24px 24px;
      text-align: center;
      box-shadow: 0 30px 70px rgba(0, 0, 0, 0.75), 0 0 0 1px rgba(255, 255, 255, 0.06);
      transform: scale(0.85);
      transition: transform 0.28s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}
    .swal-backdrop.active .swal-card {{
      transform: scale(1);
    }}

    .swal-icon-pulse {{
      width: 74px;
      height: 74px;
      border: 4px solid #f59e0b;
      border-radius: 50%;
      margin: 0 auto 16px auto;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #f59e0b;
      position: relative;
      animation: swalRingPulse 1.8s infinite;
    }}

    @keyframes swalRingPulse {{
      0% {{
        box-shadow: 0 0 0 0 rgba(245, 158, 11, 0.45);
      }}
      70% {{
        box-shadow: 0 0 0 16px rgba(245, 158, 11, 0);
      }}
      100% {{
        box-shadow: 0 0 0 0 rgba(245, 158, 11, 0);
      }}
    }}

    .swal-icon-pulse span {{
      font-size: 40px;
      font-weight: 900;
      line-height: 1;
      font-family: system-ui, -apple-system, sans-serif;
    }}

    .swal-title {{
      font-size: 1.25rem;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 10px;
      line-height: 1.3;
    }}

    .swal-desc {{
      font-size: 0.9rem;
      color: #94a3b8;
      line-height: 1.6;
      margin-bottom: 22px;
    }}

    .swal-desc .warn-highlight {{
      display: block;
      margin-top: 6px;
      color: #f87171;
      font-weight: 700;
      font-size: 0.85rem;
    }}

    .swal-buttons-row {{
      display: flex;
      gap: 10px;
      justify-content: center;
    }}

    .swal-btn-danger {{
      background: linear-gradient(135deg, #ef4444, #dc2626);
      color: #ffffff;
      border: none;
      padding: 10px 20px;
      border-radius: 10px;
      font-family: inherit;
      font-size: 0.9rem;
      font-weight: 800;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 4px 14px rgba(239, 68, 68, 0.4);
      transition: all 0.2s;
    }}
    .swal-btn-danger:hover {{
      background: linear-gradient(135deg, #dc2626, #b91c1c);
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(239, 68, 68, 0.55);
    }}

    .swal-btn-dismiss {{
      background: #1e293b;
      color: #cbd5e1;
      border: 1px solid #334155;
      padding: 10px 18px;
      border-radius: 10px;
      font-family: inherit;
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .swal-btn-dismiss:hover {{
      background: #334155;
      color: #ffffff;
    }}

    /* SweetAlert Success Toast */
    .swal-toast {{
      position: fixed;
      top: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(-30px);
      background: #0f172a;
      border: 1.5px solid #10b981;
      border-radius: 14px;
      padding: 12px 22px;
      display: flex;
      align-items: center;
      gap: 12px;
      box-shadow: 0 12px 35px rgba(0, 0, 0, 0.55);
      z-index: 2000;
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
      pointer-events: none;
    }}
    .swal-toast.show {{
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }}

    .swal-toast-icon {{
      width: 32px;
      height: 32px;
      min-width: 32px;
      border-radius: 50%;
      background: rgba(16, 185, 129, 0.18);
      color: #10b981;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
      font-weight: 900;
    }}

    .swal-toast-title {{
      font-size: 0.9rem;
      font-weight: 800;
      color: #ffffff;
    }}

    .swal-toast-msg {{
      font-size: 0.8rem;
      color: #94a3b8;
    }}

  </style>
</head>
<body>

  <!-- Top Global Navbar -->
  <header class="app-navbar no-print">
    <div class="navbar-brand" id="brandHomeBtn">
      <div class="brand-icon">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path>
          <path d="M6 6h10"></path>
          <path d="M6 10h10"></path>
          <path d="M6 14h6"></path>
        </svg>
      </div>
      <div>
        <h1>منصة استمارة بحث التخرج</h1>
        <span class="subtitle">معاهد طيبة العليا • تصميم رسمي متوافق مع مقاس A4</span>
      </div>
    </div>

    <div class="navbar-actions">
      <!-- Role indicator -->
      <span class="role-badge student" id="roleBadge">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c0 2 2 3 6 3s6-1 6-3v-5"></path></svg>
        <span id="roleBadgeText">وضع الطالب</span>
      </span>

      <!-- Switch to Gallery / All Departments -->
      <button type="button" class="btn btn-secondary btn-sm" id="btnBrowseGallery" title="تصفح جميع الأقسام والاستمارات">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
        <span class="btn-navbar-text">أقسام الاستمارات</span>
      </button>



      <!-- Clear Data -->
      <button type="button" class="btn btn-outline btn-sm workspace-btn" id="btnClearData" title="تفريغ جدول الطلاب" style="display:none;">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
        <span class="btn-navbar-text">تفريغ الجدول</span>
      </button>

      <!-- Admin Login / Logout Trigger -->
      <button type="button" class="btn btn-outline btn-sm" id="btnAuthToggle">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
        <span id="authBtnText">دخول الإدارة</span>
      </button>

      <!-- Print Button (Primary for student) -->
      <button type="button" class="btn btn-primary workspace-btn" id="btnPrintPdf" style="display:none;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="6 9 6 2 18 2 18 9"></polyline>
          <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path>
          <rect x="6" y="14" width="12" height="8"></rect>
        </svg>
        <span>طباعة / حفظ PDF</span>
      </button>
    </div>
  </header>

  <!-- Mobile Segmented Tabs Bar (Active when in Workspace on screens < 1024px) -->
  <div class="mobile-tab-bar no-print" id="mobileTabBar" style="display:none;">
    <div class="segmented-switch">
      <button type="button" class="segmented-btn active" id="tabBtnEdit">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="3" y1="15" x2="21" y2="15"></line></svg>
        <span>التحكم في الجدول</span>
      </button>
      <button type="button" class="segmented-btn" id="tabBtnPreview">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
        <span>معاينة الاستمارة (A4)</span>
      </button>
    </div>
  </div>

  <!-- ========================================================
       SCREEN 1: TEMPLATES GALLERY FOR STUDENTS & ADMIN
       ======================================================== -->
  <section class="view-gallery" id="viewGallery">
    <div class="gallery-hero">
      <h2>نماذج استمارات أبحاث التخرج المعتمدة</h2>
      <p>اختر الاستمارة المعتمدة لقسمك، واكتب بياناتك وبيانات فريقك مباشرة داخل الجدول من اليمين إلى اليسار، ثم اطبعها بضغطة زر واحدة.</p>

      <div class="search-filter-box">
        <div class="search-input-wrapper">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" class="search-input" id="gallerySearchInput" placeholder="ابحث باسم القسم أو عنوان الاستمارة...">
        </div>

        <div class="dept-filter-pills" id="deptFilterPills">
          <button type="button" class="filter-pill active" data-filter="all">جميع الأقسام</button>
          <button type="button" class="filter-pill" data-filter="نظم معلومات الأعمال">نظم معلومات الأعمال</button>
          <button type="button" class="filter-pill" data-filter="علوم الحاسب">علوم الحاسب</button>
          <button type="button" class="filter-pill" data-filter="إدارة الأعمال">إدارة ومحاسبة</button>
          <button type="button" class="filter-pill" data-filter="هندسة">هندسة</button>
        </div>
      </div>
    </div>

    <!-- Admin Top Bar in Gallery -->
    <div id="adminGalleryActions" style="display:none; justify-content:space-between; align-items:center; background:#1e293b; padding:12px 18px; border-radius:10px; border:1px solid #334155;">
      <div style="font-weight:700; color:#c084fc; display:flex; align-items:center; gap:8px;">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
        أنت الآن في وضع الإدارة (Admin) — يمكنك إنشاء وتعديل ونشر القوالب للطلاب
      </div>
      <div style="display:flex; gap:8px; flex-wrap:wrap;">
        <button type="button" class="btn btn-outline btn-sm" id="btnAdminDeleteAll" style="color:#ef4444; border-color:rgba(239,68,68,0.4);" title="حذف جميع القوالب دفعة واحدة">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6"></path><line x1="10" y1="11" x2="10" y2="17"></line><line x1="14" y1="11" x2="14" y2="17"></line></svg>
          حذف كافة القوالب
        </button>
        <button type="button" class="btn btn-outline btn-sm" id="btnAdminChangePass">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
          كلمة المرور
        </button>
        <button type="button" class="btn btn-admin btn-sm" id="btnAdminCreateNew">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
          + إنشاء قالب جديد ونشره
        </button>
      </div>
    </div>

    <!-- Templates Grid Cards -->
    <div class="templates-grid" id="templatesGrid">
      <!-- Injected by JavaScript -->
    </div>
  </section>

  <!-- ========================================================
       SCREEN 2: FORM WORKSPACE (STUDENT & ADMIN)
       ======================================================== -->
  <div class="app-workspace" id="appWorkspace">

    <!-- Right Side: Control Panel -->
    <aside class="control-panel no-print" id="controlPanel">

      <!-- Back to Gallery link inside panel -->
      <div style="padding: 12px 18px; background:#0b1120; border-bottom:1px solid #1e293b; display:flex; justify-content:space-between; align-items:center;">
        <button type="button" class="btn btn-outline btn-sm" id="btnBackToGalleryFromPanel">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          تغيير القسم / الاستمارة
        </button>
        <span style="font-size:0.75rem; color:#94a3b8;" id="panelActiveDeptBadge">قسم نظم معلومات الأعمال</span>
      </div>

      <!-- PERMANENT STUDENT INSTRUCTIONS CARD IN SIDEBAR -->
      <div class="panel-section" id="studentBannerSec">
        <div class="student-instructions-card">
          <div class="instructions-card-header">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            <span>تعليمات الطالب المعتمدة:</span>
          </div>
          <div class="instructions-list">
            <div class="instructions-list-item">
              <span class="icon">١.</span>
              <div>القالب معتمد ورسمي ومقفل بالكامل للحفاظ على تنسيق المعهد (لا يتطلب أي تعديل تصميم).</div>
            </div>
            <div class="instructions-list-item">
              <span class="icon">٢.</span>
              <div><strong>اضغط مباشرة على أي خانة داخل جدول الطلاب</strong> لكتابة الكود والاسم ورقم التليفون.</div>
            </div>
            <div class="instructions-list-item">
              <span class="icon">٣.</span>
              <div>الكتابة داخل الجدول تتم <strong>من اليمين إلى اليسار</strong> بشكل تلقائي ونظامي.</div>
            </div>
            <div class="instructions-list-item">
              <span class="icon">٤.</span>
              <div>بمجرد الانتهاء، اضغط فقط على زر <strong>"طباعة / حفظ PDF"</strong> بالأعلى.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Admin Publish Banner (shown only to admins) -->
      <div class="panel-section" id="adminBannerSec" style="display:none;">
        <div class="admin-action-banner">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; gap:8px;">
            <div style="font-size:0.85rem; font-weight:800; color:#c084fc; display:flex; align-items:center; gap:6px;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>
              <span>تحرير القالب وضبط النشر</span>
            </div>
            <span id="panelPublishStatusBadge" class="status-pill status-draft">مسودة</span>
          </div>
          <p id="panelPublishStatusDesc" style="font-size:0.78rem; color:#cbd5e1; line-height:1.5; margin-bottom:10px;">
            يمكنك كمسؤول تعديل بيانات وتنسيق القالب وحفظه كمسودة خاصة، أو نشره وإيقاف نشره للطلاب في أي وقت.
          </p>
          <div style="display:flex; flex-direction:column; gap:8px;">
            <div style="display:flex; gap:8px;">
              <button type="button" class="btn btn-primary btn-sm" id="btnSaveTemplateChanges" style="flex:1;" title="حفظ جميع التعديلات الحالية في القالب">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"></path><polyline points="17 21 17 13 7 13 7 21"></polyline><polyline points="7 3 7 8 15 8"></polyline></svg>
                حفظ التعديلات
              </button>
              <button type="button" class="btn btn-outline btn-sm" id="btnChangePassInPanel" title="تغيير كلمة مرور الإدارة">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
              </button>
            </div>
            <button type="button" class="btn btn-sm" id="btnTogglePublishInPanel" style="width:100%;">
              <!-- Injected dynamically by updateAdminBannerUI() -->
            </button>
          </div>
        </div>
      </div>

      <!-- Section: Rows & Students (Available to BOTH Student & Admin) -->
      <div class="panel-section">
        <div class="section-title">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="3" y1="15" x2="21" y2="15"></line></svg>
          صفوف جدول الطلاب (حجم الفريق)
        </div>

        <div class="form-group">
          <label class="form-label">عدد صفوف الجدول:</label>
          <div class="stepper-container">
            <button type="button" class="stepper-btn" id="btnDecRow">-</button>
            <input type="number" class="stepper-input" id="inputRowCount" value="15" min="1" max="40">
            <button type="button" class="stepper-btn" id="btnIncRow">+</button>
          </div>
        </div>

        <div class="row-controls-grid">
          <button type="button" class="btn btn-secondary btn-sm" id="btnAddRow">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
            + إضافة صف
          </button>
          <button type="button" class="btn btn-secondary btn-sm" id="btnDeleteRow">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line></svg>
            - حذف صف
          </button>
        </div>

        <div class="presets-group">
          <span style="font-size: 0.74rem; color: #64748b; margin-left: 4px; align-self: center;">اختيار سريع:</span>
          <button type="button" class="preset-pill" data-rows="5">5</button>
          <button type="button" class="preset-pill" data-rows="10">10</button>
          <button type="button" class="preset-pill active" data-rows="15">15 (افتراضي)</button>
          <button type="button" class="preset-pill" data-rows="20">20</button>
          <button type="button" class="preset-pill" data-rows="25">25</button>
          <button type="button" class="preset-pill" data-rows="30">30</button>
        </div>
      </div>

      <!-- ========================================================
           ADMIN ONLY CONTROLS (COMPLETELY HIDDEN FOR STUDENTS)
           ======================================================== -->
      <div id="adminDesignControls" style="display:none;">

        <!-- Admin: Project Data Inputs -->
        <div class="panel-section">
          <div class="section-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
            [خاص بالإدارة] بيانات المشروع المنشورة
          </div>

          <div class="form-group">
            <label class="form-label">
              <span>رقم المشروع:</span>
              <span class="optional">(اتركه فارغاً لنقاط اليد)</span>
            </label>
            <input type="text" class="form-control" id="inputProjectNo" placeholder="مثال: 104">
          </div>

          <div class="form-group">
            <label class="form-label">
              <span>اسم المشروع:</span>
              <span class="optional">(اتركه فارغاً لنقاط اليد)</span>
            </label>
            <input type="text" class="form-control" id="inputProjectName" placeholder="مثال: نظام ذكي لأتمتة خدمة العملاء">
          </div>

          <div class="form-group">
            <label class="form-label">
              <span>اسم الدكتور المشرف:</span>
              <span class="optional">(اتركه فارغاً لنقاط اليد)</span>
            </label>
            <input type="text" class="form-control" id="inputSupervisor" placeholder="مثال: أ.د/ إبراهيم سليم">
          </div>

          <div class="form-group">
            <label class="form-label">العام الجامعي:</label>
            <input type="text" class="form-control" id="inputAcademicYear" value="العام الجامعي 2024 / 2025">
          </div>
        </div>

        <!-- Admin: Form Title & Department Info -->
        <div class="panel-section">
          <div class="section-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
            [خاص بالإدارة] عنوان الاستمارة والقسم
          </div>

          <div class="form-group">
            <label class="form-label">عنوان الاستمارة الرئيسي:</label>
            <input type="text" class="form-control" id="inputFormTitle" value="استمارة بحث تخرج نظم معلومات الأعمال">
          </div>
          <div class="form-group">
            <label class="form-label">اسم المؤسسة (السطر 1):</label>
            <input type="text" class="form-control" id="inputInstLine1" value="معاهد طيبة العليا">
          </div>
          <div class="form-group">
            <label class="form-label">اسم المعهد (السطر 2):</label>
            <input type="text" class="form-control" id="inputInstLine2" value="المعهد العالي لتكنولوجيا الإدارة والمعلومات">
          </div>
          <div class="form-group">
            <label class="form-label">القسم العلمي (السطر 3):</label>
            <input type="text" class="form-control" id="inputInstLine3" value="قسم نظم معلومات الأعمال">
          </div>
        </div>

        <!-- Admin: Columns Management -->
        <div class="panel-section">
          <div class="section-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="3" x2="12" y2="21"></line><line x1="8" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="16" y2="21"></line><line x1="3" y1="9" x2="21" y2="9"></line><line x1="3" y1="15" x2="21" y2="15"></line></svg>
            [خاص بالإدارة] إدارة وتخصيص الأعمدة
          </div>

          <div class="columns-list" id="columnsContainer">
            <!-- Rendered by JS -->
          </div>

          <div style="display: flex; gap: 8px;">
            <button type="button" class="btn btn-secondary btn-sm" id="btnAddColumn" style="flex: 1;">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
              + إضافة عمود جديد
            </button>
            <button type="button" class="btn btn-outline btn-sm" id="btnResetColumns" title="إعادة الأعمدة إلى 4 أعمدة افتراضية">
              الأعمدة الافتراضية
            </button>
          </div>
        </div>

        <!-- Admin: Logo Management -->
        <div class="panel-section">
          <div class="section-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
            [خاص بالإدارة] إعدادات الشعار
          </div>

          <div class="logo-control-box">
            <div class="logo-preview-row">
              <div class="logo-thumbnail">
                <img id="logoPreviewThumb" src="data:image/png;base64,{logo_b64}" alt="شعار المعهد">
              </div>
              <div class="logo-buttons">
                <input type="file" id="logoFileInput" accept="image/*" style="display: none;">
                <button type="button" class="btn btn-secondary btn-sm" onclick="document.getElementById('logoFileInput').click()">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="17 8 12 3 7 8"></polyline><line x1="12" y1="3" x2="12" y2="15"></line></svg>
                  رفع شعار جديد
                </button>
                <div style="display: flex; gap: 6px;">
                  <button type="button" class="btn btn-outline btn-sm" id="btnToggleLogo" style="flex:1;">
                    إخفاء الشعار
                  </button>
                  <button type="button" class="btn btn-outline btn-sm" id="btnResetLogo" title="إعادة شعار معاهد طيبة الافتراضي">
                    الشعار الأصلي
                  </button>
                </div>
              </div>
            </div>

            <div class="form-group" style="margin-top: 4px;">
              <label class="form-label">
                <span>حجم الشعار</span>
                <span id="logoSizeVal" style="color:#38bdf8;">58px</span>
              </label>
              <input type="range" class="form-control" id="logoSizeSlider" min="35" max="95" value="58" style="padding: 2px;">
            </div>
          </div>
        </div>

        <!-- Admin: Signatures & Department Head -->
        <div class="panel-section">
          <div class="section-title">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m18 2 4 4-10 10H8v-4L18 2z"></path><path d="m14 6 4 4"></path><path d="M4 22h16"></path></svg>
            [خاص بالإدارة] رئيس القسم والتوقيعات
          </div>

          <div class="form-group">
            <label class="form-label">صفة التوقيع الأيمن:</label>
            <input type="text" class="form-control" id="inputSignRightTitle" value="أستاذ المادة المشرف">
          </div>
          <div class="form-group">
            <label class="form-label">صفة التوقيع الأيسر:</label>
            <input type="text" class="form-control" id="inputSignLeftTitle" value="رئيس القسم">
          </div>
          <div class="form-group">
            <label class="form-label">اسم رئيس القسم:</label>
            <input type="text" class="form-control" id="inputHeadName" value="أ.د/ إبراهيم سليم">
          </div>
        </div>

      </div> <!-- End Admin Design Controls -->

    </aside>

    <!-- Left Side: Interactive Canvas & A4 Page -->
    <main class="canvas-area" id="canvasArea">

      <!-- Always Visible Student Instructions Banner Above the Form -->
      <div class="student-top-guide-bar no-print" id="studentTopGuideBar">
        <div class="guide-bar-content">
          <div class="guide-bar-icon-wrap">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6"></path><path d="M10 22h4"></path><path d="M12 2a7 7 0 0 0-7 7c0 2.38 1.19 4.47 3 5.74V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.26c1.81-1.27 3-3.36 3-5.74a7 7 0 0 0-7-7z"></path></svg>
          </div>
          <div>
            <div class="guide-bar-title">تعليمات هامة للطلاب:</div>
            <div class="guide-bar-instructions">
              <strong>١. اكتب بياناتك مباشرة:</strong> اضغط داخل أي خانة في جدول الطلاب واكتب الاسم ورقم الكود ورقم التليفون (الكتابة تبدأ تلقائياً <strong>من اليمين إلى اليسار</strong>).<br>
              <strong>٢. القالب معتمد ومقفل:</strong> جميع بيانات المعهد والعناوين الرسمية مقفلة لحماية التنسيق الأكاديمي المعتمد لمعهدك.<br>
              <strong>٣. الطباعة والحفظ:</strong> بمجرد الانتهاء من ملء بياناتك، اضغط فقط على زر <strong>«طباعة / حفظ PDF»</strong> للاحتفاظ بنسختك المعتمدة.
            </div>
          </div>
        </div>
        <button type="button" class="btn btn-primary" onclick="document.getElementById('btnPrintPdf').click()" style="align-self: center; white-space: nowrap;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
          طباعة / حفظ PDF
        </button>
      </div>

      <!-- Zoom and Display Controls Toolbar -->
      <div class="zoom-toolbar no-print">
        <button type="button" class="col-icon-btn" id="btnZoomOut" title="تصغير">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
        </button>
        <span class="zoom-text" id="zoomLabel">85%</span>
        <button type="button" class="col-icon-btn" id="btnZoomIn" title="تكبير">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
        </button>

        <div style="width: 1px; height: 16px; background: rgba(255,255,255,0.15);"></div>

        <button type="button" class="btn btn-outline btn-sm" id="btnZoomFit" style="border-radius: 20px; font-size: 0.76rem; padding: 4px 10px;">
          ملاءمة الشاشة
        </button>
        <button type="button" class="btn btn-outline btn-sm" id="btnZoomReset" style="border-radius: 20px; font-size: 0.76rem; padding: 4px 10px;">
          100%
        </button>
      </div>

      <!-- Proportional Paper Viewport -->
      <div class="paper-viewport" id="paperViewport">
        <div class="paper-scale-container" id="paperScaleContainer">
          <div class="paper-wrapper" id="paperWrapper">
            <div class="a4-page" id="a4Page">
            
            <!-- Corner Ornaments -->
            <div class="corner-decor corner-tl"></div>
            <div class="corner-decor corner-tr"></div>
            <div class="corner-decor corner-bl"></div>
            <div class="corner-decor corner-br"></div>

            <!-- Document Content Flow -->
            <div class="page-content">

              <!-- 1. Header with Logo & Institute Titles -->
              <div class="form-header">
                <div class="header-institute-col">
                  <img id="formLogoImg" class="institute-logo-img" src="data:image/png;base64,{logo_b64}" alt="شعار المعهد">
                  <div class="institute-text-lines">
                    <div class="inst-title" id="previewInstLine1">معاهد طيبة العليا</div>
                    <div class="inst-sub" id="previewInstLine2">المعهد العالي لتكنولوجيا الإدارة والمعلومات</div>
                    <div class="inst-dept" id="previewInstLine3">قسم نظم معلومات الأعمال</div>
                  </div>
                </div>

                <div class="header-left-badge">
                  <div style="font-size: 9pt; color: #444; margin-bottom: 2px;">وزارة التعليم العالي</div>
                  <div class="year-badge" id="previewAcademicYear">العام الجامعي 2024 / 2025</div>
                </div>
              </div>

              <!-- 2. Form Main Title with Official Underline -->
              <div class="form-title-wrapper">
                <div class="form-main-title" id="previewFormTitle" contenteditable="false" spellcheck="false">
                  استمارة بحث تخرج نظم معلومات الأعمال
                </div>
                <div class="form-title-divider"></div>
              </div>

              <!-- 3. Project Metadata with Dotted Lines (Student cannot edit, Admin can edit) -->
              <div class="project-meta-box">
                <div class="meta-row">
                  <span class="meta-label">رقم المشروع:</span>
                  <div class="meta-line-container">
                    <span class="meta-value-text" id="previewProjectNo" contenteditable="false" spellcheck="false"></span>
                    <div class="meta-dotted-line"></div>
                  </div>
                </div>

                <div class="meta-row">
                  <span class="meta-label">اسم المشروع:</span>
                  <div class="meta-line-container">
                    <span class="meta-value-text" id="previewProjectName" contenteditable="false" spellcheck="false"></span>
                    <div class="meta-dotted-line"></div>
                  </div>
                </div>

                <div class="meta-row">
                  <span class="meta-label">اسم الدكتور المشرف:</span>
                  <div class="meta-line-container">
                    <span class="meta-value-text" id="previewSupervisor" contenteditable="false" spellcheck="false"></span>
                    <div class="meta-dotted-line"></div>
                  </div>
                </div>
              </div>

              <!-- 4. Students Table (The ONLY part student can type into, strictly Right-to-Left) -->
              <div class="table-container">
                <table class="students-table" id="studentsTable">
                  <thead id="tableHead">
                    <!-- Header Row rendered dynamically -->
                  </thead>
                  <tbody id="tableBody">
                    <!-- Table Rows rendered dynamically -->
                  </tbody>
                </table>
              </div>

              <!-- 5. Bottom Signatures & Department Head -->
              <div class="form-footer-signatures">
                <div class="signature-block">
                  <div class="signature-title" id="previewSignRightTitle">أستاذ المادة المشرف</div>
                  <div class="signature-dots">......................................</div>
                </div>

                <div class="signature-block">
                  <div class="signature-title" id="previewSignLeftTitle">رئيس القسم</div>
                  <div class="signature-name" id="previewHeadName">أ.د/ إبراهيم سليم</div>
                </div>
              </div>

            </div> <!-- End page-content -->
          </div> <!-- End a4-page -->
        </div> <!-- End paper-wrapper -->
      </div> <!-- End paper-scale-container -->
    </div> <!-- End paper-viewport -->

      <div class="edit-hint-toast no-print">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
        <span>اضغط على أي خانة في جدول الطلاب واكتب من اليمين لليسار، ثم اطبع!</span>
      </div>

    </main>
  </div>

  <!-- Secure Admin Login Modal (SHA-256 Protected) -->
  <div class="modal-backdrop" id="adminLoginModal">
    <div class="modal-card">
      <h3>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
        تسجيل دخول مسؤول النظام (Admin)
      </h3>
      <p>أدخل كلمة مرور المسؤول لفتح صلاحيات تعديل وتصميم ونشر القوالب لجميع الطلاب:</p>
      
      <div class="form-group" style="margin-bottom: 14px;">
        <label class="form-label">كلمة المرور المشفرة:</label>
        <div class="password-input-wrap">
          <input type="password" class="form-control" id="adminPasswordInput" placeholder="أدخل كلمة مرور الإدارة..." style="padding-left: 36px;">
          <button type="button" class="password-toggle-btn" id="btnTogglePassVisibility" title="إظهار / إخفاء كلمة المرور">
            <svg id="eyeIcon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
          </button>
        </div>
        <div id="loginFeedbackMsg" style="font-size:0.75rem; color:#f87171; margin-top:6px; display:none;"></div>

      </div>

      <div style="display:flex; gap:10px; justify-content:flex-end;">
        <button type="button" class="btn btn-outline" id="btnCloseLoginModal">إلغاء</button>
        <button type="button" class="btn btn-admin" id="btnSubmitAdminLogin">
          دخول كمسؤول
        </button>
      </div>
    </div>
  </div>

  <!-- Change Admin Password Modal -->
  <div class="modal-backdrop" id="changePassModal">
    <div class="modal-card">
      <h3>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2"><path d="M21 2l-2 2m-1.5 6.1L19 12l2-2-4-4-1.9 1.5M10.5 14.5L3 22l4-4 3.5-3.5"></path></svg>
        تغيير كلمة مرور الإدارة (Admin)
      </h3>
      <p>يمكنك تعيين كلمة مرور جديدة لحماية لوحة الإدارة. يتم تشفيرها تلقائياً بتقنية SHA-256 وحفظها في المتصفح.</p>

      <div class="form-group">
        <label class="form-label">كلمة المرور الحالية:</label>
        <input type="password" class="form-control" id="inputOldPass" placeholder="أدخل كلمة المرور الحالية">
      </div>
      <div class="form-group">
        <label class="form-label">كلمة المرور الجديدة:</label>
        <input type="password" class="form-control" id="inputNewPass" placeholder="أدخل كلمة المرور الجديدة">
      </div>
      <div class="form-group">
        <label class="form-label">تأكيد كلمة المرور الجديدة:</label>
        <input type="password" class="form-control" id="inputConfirmPass" placeholder="أعد إدخال كلمة المرور الجديدة">
      </div>

      <div id="changePassFeedback" style="font-size:0.78rem; margin-bottom:10px; display:none;"></div>

      <div style="display:flex; gap:10px; justify-content:flex-end;">
        <button type="button" class="btn btn-outline" id="btnCloseChangePass">إلغاء</button>
        <button type="button" class="btn btn-primary" id="btnSaveNewPass">حفظ كلمة المرور</button>
      </div>
    </div>
  </div>

  <!-- Universal SweetAlert 2 Style Confirmation Modal (For Delete & Clear) -->
  <div class="swal-backdrop" id="swalConfirmModal">
    <div class="swal-card">
      <div class="swal-icon-pulse">
        <span>!</span>
      </div>
      <h3 class="swal-title" id="swalConfirmTitle">تأكيد الإجراء</h3>
      <div class="swal-desc" id="swalConfirmDesc">
        هل أنت متأكد من تنفيذ هذا الإجراء؟
      </div>
      <div class="swal-buttons-row">
        <button type="button" class="swal-btn-danger" id="swalConfirmBtn">
          نعم، تأكيد
        </button>
        <button type="button" class="swal-btn-dismiss" id="swalCancelBtn">
          إلغاء الأمر
        </button>
      </div>
    </div>
  </div>

  <!-- SweetAlert Success Toast -->
  <div class="swal-toast" id="swalToast">
    <div class="swal-toast-icon">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
    </div>
    <div>
      <div class="swal-toast-title">تم بنجاح!</div>
      <div class="swal-toast-msg">تم تفريغ كافة بيانات الجدول وأصبح جاهزاً لإدخال بيانات جديدة.</div>
    </div>
  </div>

  <!-- Print Advice Modal -->
  <div class="modal-backdrop" id="printModal">
    <div class="modal-card">
      <h3>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#38bdf8" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
        تعليمات طباعة استمارة رسمية مثالية (A4)
      </h3>
      <p>لضمان ظهور الاستمارة بصفحة واحدة متناسقة وبأعلى جودة رسمية في نافذة الطباعة:</p>
      
      <div class="print-tip-item">
        <span style="color:#10b981; font-weight:bold;">1.</span>
        <div><strong>الوجهة (Destination):</strong> اختر "حفظ بتنسيق PDF" أو طابعتك.</div>
      </div>
      <div class="print-tip-item">
        <span style="color:#10b981; font-weight:bold;">2.</span>
        <div><strong>الهوامش (Margins):</strong> اختر <strong>"بلا" (None)</strong> أو "الافتراضي".</div>
      </div>
      <div class="print-tip-item">
        <span style="color:#10b981; font-weight:bold;">3.</span>
        <div><strong>رسومات الخلفية (Background graphics):</strong> تأكد من <strong>تفعيل الخيار</strong> لظهور ألوان العناوين والإطارات.</div>
      </div>

      <div style="display: flex; gap: 10px; margin-top: 18px; justify-content: flex-end;">
        <button type="button" class="btn btn-outline" id="btnCloseModal">إلغاء</button>
        <button type="button" class="btn btn-primary" id="btnConfirmPrint">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
          متابعة للطباعة الآن
        </button>
      </div>
    </div>
  </div>

  <script>
    const DEFAULT_LOGO_B64 = "data:image/png;base64,{logo_b64}";

    // Cryptographic SHA-256 implementation
    async function sha256(str) {{
      const encoder = new TextEncoder();
      const data = encoder.encode(str);
      const hashBuffer = await crypto.subtle.digest('SHA-256', data);
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    }}

    // Secure SHA-256 hash for Admin authentication
    const DEFAULT_ADMIN_HASH = "9ec12179bb48a8a0986b2eb22b0a62802f3481409862cd6509b8b2becf66a52f";

    function getAdminHash() {{
      return localStorage.getItem("tiba_admin_hash_v2") || DEFAULT_ADMIN_HASH;
    }}

    // Preloaded Official Department Templates
    const INITIAL_TEMPLATES = [
      {{
        id: "bis_default",
        dept: "نظم معلومات الأعمال",
        published: true,
        formTitle: "استمارة بحث تخرج نظم معلومات الأعمال",
        instLine1: "معاهد طيبة العليا",
        instLine2: "المعهد العالي لتكنولوجيا الإدارة والمعلومات",
        instLine3: "قسم نظم معلومات الأعمال",
        academicYear: "العام الجامعي 2024 / 2025",
        projectNo: "",
        projectName: "",
        supervisor: "",
        signRightTitle: "أستاذ المادة المشرف",
        signLeftTitle: "رئيس القسم",
        headName: "أ.د/ إبراهيم سليم",
        logoVisible: true,
        logoSize: 58,
        logoData: DEFAULT_LOGO_B64,
        columns: [
          {{ id: "col_seq", name: "م", width: "7%", autoSeq: true }},
          {{ id: "col_code", name: "كود الطالب", width: "23%", autoSeq: false }},
          {{ id: "col_name", name: "اسم الطالب", width: "42%", autoSeq: false }},
          {{ id: "col_phone", name: "رقم التليفون", width: "28%", autoSeq: false }}
        ],
        rowCount: 15
      }},
      {{
        id: "cs_default",
        dept: "علوم الحاسب",
        published: true,
        formTitle: "استمارة تسجيل مشروع تخرج علوم الحاسب",
        instLine1: "معاهد طيبة العليا",
        instLine2: "المعهد العالي لعلوم الحاسب وتكنولوجيا المعلومات",
        instLine3: "قسم علوم الحاسب",
        academicYear: "العام الجامعي 2024 / 2025",
        projectNo: "",
        projectName: "",
        supervisor: "",
        signRightTitle: "المشرف الأكاديمي",
        signLeftTitle: "رئيس مجلس القسم",
        headName: "أ.د/ عادل عبد الفتاح",
        logoVisible: true,
        logoSize: 58,
        logoData: DEFAULT_LOGO_B64,
        columns: [
          {{ id: "col_seq", name: "م", width: "7%", autoSeq: true }},
          {{ id: "col_code", name: "كود الطالب", width: "20%", autoSeq: false }},
          {{ id: "col_name", name: "اسم الطالب", width: "38%", autoSeq: false }},
          {{ id: "col_track", name: "مسار التخصص (Track)", width: "17%", autoSeq: false }},
          {{ id: "col_phone", name: "رقم التليفون", width: "18%", autoSeq: false }}
        ],
        rowCount: 15
      }},
      {{
        id: "business_default",
        dept: "إدارة الأعمال",
        published: true,
        formTitle: "استمارة بحث تخرج إدارة الأعمال والمحاسبة",
        instLine1: "معاهد طيبة العليا",
        instLine2: "المعهد العالي لتكنولوجيا الإدارة والمعلومات",
        instLine3: "قسم العلوم التجارية والإدارية",
        academicYear: "العام الجامعي 2024 / 2025",
        projectNo: "",
        projectName: "",
        supervisor: "",
        signRightTitle: "أستاذ المادة المشرف",
        signLeftTitle: "رئيس القسم",
        headName: "أ.د/ محمد عبد السلام",
        logoVisible: true,
        logoSize: 58,
        logoData: DEFAULT_LOGO_B64,
        columns: [
          {{ id: "col_seq", name: "م", width: "7%", autoSeq: true }},
          {{ id: "col_code", name: "كود الطالب", width: "22%", autoSeq: false }},
          {{ id: "col_name", name: "اسم الطالب", width: "40%", autoSeq: false }},
          {{ id: "col_dept_track", name: "الشعبة", width: "15%", autoSeq: false }},
          {{ id: "col_phone", name: "رقم التليفون", width: "16%", autoSeq: false }}
        ],
        rowCount: 15
      }},
      {{
        id: "eng_default",
        dept: "هندسة",
        formTitle: "استمارة تسجيل مشروع تخرج هندسة الحاسبات والتحكم",
        instLine1: "معاهد طيبة العليا",
        instLine2: "معهد طيبة العالي للهندسة",
        instLine3: "قسم هندسة الحاسبات ونظم التحكم",
        academicYear: "العام الجامعي 2024 / 2025",
        projectNo: "",
        projectName: "",
        supervisor: "",
        signRightTitle: "المشرف على المشروع",
        signLeftTitle: "رئيس القسم",
        headName: "أ.د/ خالد الشافعي",
        logoVisible: true,
        logoSize: 58,
        logoData: DEFAULT_LOGO_B64,
        columns: [
          {{ id: "col_seq", name: "م", width: "7%", autoSeq: true }},
          {{ id: "col_code", name: "كود الطالب", width: "23%", autoSeq: false }},
          {{ id: "col_name", name: "اسم الطالب", width: "42%", autoSeq: false }},
          {{ id: "col_phone", name: "رقم التليفون", width: "28%", autoSeq: false }}
        ],
        rowCount: 15
      }}
    ];

    // Current State
    let templates = [];
    let currentRole = "student"; // "student" or "admin"
    let currentTemplate = null;
    let appState = {{
      tableData: [],
      rowCount: 15
    }};
    let currentZoom = 0.85;

    // Load templates from localStorage
    function loadTemplates() {{
      try {{
        const stored = localStorage.getItem("tiba_templates_v2");
        if (stored !== null) {{
          templates = JSON.parse(stored);
          let modified = false;
          templates.forEach(t => {{
            if (typeof t.published === 'undefined') {{
              t.published = true;
              modified = true;
            }}
          }});
          if (modified) saveTemplates();
        }} else {{
          templates = JSON.parse(JSON.stringify(INITIAL_TEMPLATES));
          saveTemplates();
        }}
      }} catch (e) {{
        templates = JSON.parse(JSON.stringify(INITIAL_TEMPLATES));
      }}
    }}

    function saveTemplates() {{
      try {{
        localStorage.setItem("tiba_templates_v2", JSON.stringify(templates));
      }} catch (e) {{}}
    }}

    // Switch Views
    function showGalleryView() {{
      document.getElementById('viewGallery').style.display = 'flex';
      document.getElementById('appWorkspace').classList.remove('active');
      document.getElementById('mobileTabBar').style.display = 'none';
      document.querySelectorAll('.workspace-btn').forEach(btn => btn.style.display = 'none');
      renderGallery();
    }}

    function showWorkspaceView() {{
      document.getElementById('viewGallery').style.display = 'none';
      document.getElementById('appWorkspace').classList.add('active');
      if (window.innerWidth <= 1024) {{
        document.getElementById('mobileTabBar').style.display = 'block';
      }}
      document.querySelectorAll('.workspace-btn').forEach(btn => btn.style.display = 'inline-flex');
      
      applyRolePermissions();
      updateAdminBannerUI();
      syncInputsFromState();
      renderPreview();
      
      setTimeout(() => {{
        fitToScreen();
      }}, 80);
    }}

    // Apply Role UI Controls
    function applyRolePermissions() {{
      const roleBadge = document.getElementById('roleBadge');
      const roleText = document.getElementById('roleBadgeText');
      const authBtnText = document.getElementById('authBtnText');
      const studentBanner = document.getElementById('studentBannerSec');
      const adminBanner = document.getElementById('adminBannerSec');
      const adminGalleryActions = document.getElementById('adminGalleryActions');
      const adminDesignControls = document.getElementById('adminDesignControls');
      const studentTopGuide = document.getElementById('studentTopGuideBar');
      const controlPanel = document.getElementById('controlPanel');
      const mobileTabBar = document.getElementById('mobileTabBar');
      
      const previewTitle = document.getElementById('previewFormTitle');
      const previewProjectNo = document.getElementById('previewProjectNo');
      const previewProjectName = document.getElementById('previewProjectName');
      const previewSupervisor = document.getElementById('previewSupervisor');

      if (currentRole === 'admin') {{
        document.body.classList.add('role-admin');
        document.body.classList.remove('role-student');

        roleBadge.className = 'role-badge admin';
        roleText.innerText = 'وضع الإدارة (Admin)';
        authBtnText.innerText = 'خروج من الإدارة';
        studentBanner.style.display = 'none';
        adminBanner.style.display = 'block';
        adminGalleryActions.style.display = 'flex';
        adminDesignControls.style.display = 'block';
        studentTopGuide.style.display = 'none';
        updateAdminBannerUI();

        if (controlPanel) controlPanel.style.display = 'flex';
        if (window.innerWidth <= 1024 && mobileTabBar) {{
          mobileTabBar.style.display = 'block';
        }}

        // Admin can edit all headers directly in preview
        previewTitle.contentEditable = 'true';
        previewProjectNo.contentEditable = 'true';
        previewProjectName.contentEditable = 'true';
        previewSupervisor.contentEditable = 'true';
      }} else {{
        // Student Mode: STRICTLY LOCKED, NO SIDEBAR, ONLY PREVIEW CANVAS!
        document.body.classList.add('role-student');
        document.body.classList.remove('role-admin');

        roleBadge.className = 'role-badge student';
        roleText.innerText = 'وضع الطالب';
        authBtnText.innerText = 'دخول الإدارة';
        studentBanner.style.display = 'none';
        adminBanner.style.display = 'none';
        adminGalleryActions.style.display = 'none';
        adminDesignControls.style.display = 'none';
        studentTopGuide.style.display = 'flex';

        if (controlPanel) controlPanel.style.display = 'none';
        if (mobileTabBar) mobileTabBar.style.display = 'none';

        // Student CANNOT edit anything outside the table!
        previewTitle.contentEditable = 'false';
        previewProjectNo.contentEditable = 'false';
        previewProjectName.contentEditable = 'false';
        previewSupervisor.contentEditable = 'false';
      }}
    }}

    // Render Gallery
    let activeFilter = 'all';
    function renderGallery() {{
      const grid = document.getElementById('templatesGrid');
      const searchVal = document.getElementById('gallerySearchInput').value.trim().toLowerCase();
      grid.innerHTML = '';

      // Students only see published templates (published !== false)
      const roleTemplates = (currentRole === 'admin') 
        ? templates 
        : templates.filter(t => t.published !== false);

      const filtered = roleTemplates.filter(t => {{
        const matchesFilter = (activeFilter === 'all' || t.dept.includes(activeFilter));
        const matchesSearch = (!searchVal || t.formTitle.toLowerCase().includes(searchVal) || t.dept.toLowerCase().includes(searchVal));
        return matchesFilter && matchesSearch;
      }});

      if (filtered.length === 0) {{
        if (roleTemplates.length === 0) {{
          if (currentRole === 'admin') {{
            grid.innerHTML = `
              <div style="grid-column: 1/-1; text-align: center; padding: 50px 20px; background: rgba(15, 23, 42, 0.7); border: 2px dashed #475569; border-radius: 16px;">
                <div style="width: 56px; height: 56px; margin: 0 auto 14px auto; background: rgba(148, 163, 184, 0.1); border-radius: 14px; display: flex; align-items: center; justify-content: center; color: #94a3b8;">
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: 800; color: #fff; margin-bottom: 8px;">لا توجد أي قوالب حالياً</h3>
                <p style="font-size: 0.88rem; color: #94a3b8; max-width: 480px; margin: 0 auto 16px auto; line-height: 1.6;">
                  تم تفريغ كافة القوالب. يمكنك كمسؤول إنشاء قالب استمارة جديد الآن وضبط بياناته ونشره للطلاب.
                </p>
                <div style="display:flex; justify-content:center;">
                  <button type="button" class="btn btn-admin" onclick="document.getElementById('btnAdminCreateNew').click()">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                    + إنشاء قالب جديد
                  </button>
                </div>
              </div>
            `;
          }} else {{
            grid.innerHTML = `
              <div style="grid-column: 1/-1; text-align: center; padding: 60px 20px; background: rgba(15, 23, 42, 0.7); border: 2px dashed #334155; border-radius: 16px;">
                <div style="width: 60px; height: 60px; margin: 0 auto 14px auto; background: rgba(56, 189, 248, 0.12); border-radius: 16px; display: flex; align-items: center; justify-content: center; color: #38bdf8;">
                  <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                </div>
                <h3 style="font-size: 1.35rem; font-weight: 800; color: #38bdf8; margin-bottom: 8px;">لا توجد استمارات متاحة حالياً</h3>
                <p style="font-size: 0.95rem; color: #cbd5e1; max-width: 520px; margin: 0 auto; line-height: 1.7;">
                  لم تقم إدارة المعهد بنشر أي استمارة بحث حتى الآن. يرجى الانتظار حتى تقوم إدارة المعهد بنشر القوالب المعتمدة لقسمك.
                </p>
              </div>
            `;
          }}
          return;
        }}

        grid.innerHTML = `
          <div style="grid-column: 1/-1; text-align: center; padding: 40px; color: #94a3b8;">
            <p style="font-size: 1.1rem; font-weight: 700;">لا توجد استمارات مطابقة للبحث</p>
            <p style="font-size: 0.85rem; margin-top: 6px;">جرب تغيير كلمة البحث أو اختيار "جميع الأقسام".</p>
          </div>
        `;
        return;
      }}

      filtered.forEach(tmpl => {{
        const isPublished = (tmpl.published !== false);
        const card = document.createElement('div');
        card.className = 'template-card';
        card.innerHTML = `
          <div>
            <div class="template-card-header">
              <div class="card-dept-icon">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z"></path><path d="M6 6h10"></path><path d="M6 10h10"></path></svg>
              </div>
              <div class="card-meta">
                <div style="display:flex; justify-content:space-between; align-items:center; gap:6px; margin-bottom:6px; flex-wrap:wrap;">
                  <span class="card-dept-tag">${{tmpl.dept}}</span>
                  ${{currentRole === 'admin' ? `
                    <span class="status-pill ${{isPublished ? 'status-published' : 'status-draft'}}">
                      ${{isPublished ? `
                        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        منشور للطلاب
                      ` : `
                        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"></circle><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"></line></svg>
                        مسودة (غير منشور)
                      `}}
                    </span>
                  ` : ''}}
                </div>
                <h3 class="card-title">${{tmpl.formTitle}}</h3>
              </div>
            </div>

            <div class="card-details" style="margin-top: 14px;">
              <div class="card-detail-item">
                <span>المعهد:</span>
                <span class="val">${{tmpl.instLine2}}</span>
              </div>
              <div class="card-detail-item">
                <span>رئيس القسم:</span>
                <span class="val">${{tmpl.headName}}</span>
              </div>
              <div class="card-detail-item">
                <span>أعمدة الجدول:</span>
                <span class="val">${{tmpl.columns.map(c => c.name).join(' • ')}}</span>
              </div>
            </div>
          </div>

          ${{currentRole === 'admin' ? `
            <div style="margin-top: 14px; padding-top: 12px; border-top: 1px dashed #334155;">
              <button type="button" class="btn btn-sm" onclick="event.stopPropagation(); togglePublishTemplate('${{tmpl.id}}');" style="width:100%; justify-content:center; padding:9px 12px; font-weight:800; font-size:0.88rem; border-radius:8px; display:flex; align-items:center; gap:8px; cursor:pointer; transition:all 0.2s ease; ${{isPublished ? 'background:rgba(245,158,11,0.14); color:#fbbf24; border:1.5px solid #f59e0b;' : 'background:rgba(16,185,129,0.16); color:#34d399; border:1.5px solid #10b981;'}}">
                ${{isPublished ? `
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="10" y1="15" x2="10" y2="9"></line><line x1="14" y1="15" x2="14" y2="9"></line></svg>
                  <span>توقيف العرض (معروض للطلاب حالياً)</span>
                ` : `
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                  <span>تشغيل العرض (نشر وإتاحة للطلاب)</span>
                `}}
              </button>
            </div>
          ` : ''}}

          <div class="template-card-footer" style="margin-top: 10px;">
            <button type="button" class="btn btn-primary" style="flex:1;" onclick="selectTemplate('${{tmpl.id}}')">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>${{currentRole === 'admin' ? 'تعديل وتحرير القالب' : 'اختيار هذه الاستمارة وتعبئتها'}}</span>
            </button>
            ${{currentRole === 'admin' ? `
              <button type="button" class="btn btn-outline btn-sm" onclick="event.stopPropagation(); deleteTemplate('${{tmpl.id}}');" title="حذف هذا القالب نهائياً" style="padding: 8px 12px;">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6"></path></svg>
              </button>
            ` : ''}}
          </div>
        `;
        grid.appendChild(card);
      }});
    }}

    // Select Template and open workspace
    window.selectTemplate = function(templateId) {{
      const found = templates.find(t => t.id === templateId);
      if (!found) return;
      if (currentRole !== 'admin' && found.published === false) {{
        showSwalToast('استمارة غير متاحة', 'هذا القالب مسودة خاصة ولم يتم نشره للطلاب بعد.');
        return;
      }}
      currentTemplate = JSON.parse(JSON.stringify(found));
      
      appState.rowCount = currentTemplate.rowCount || 15;
      document.getElementById('panelActiveDeptBadge').innerText = currentTemplate.dept;
      showWorkspaceView();
    }};

    // Toggle Publish/Display Status for a Template
    window.togglePublishTemplate = function(templateId) {{
      const tmpl = templates.find(t => t.id === templateId);
      if (!tmpl) return;
      tmpl.published = (tmpl.published === false) ? true : false;
      saveTemplates();
      if (currentTemplate && currentTemplate.id === templateId) {{
        currentTemplate.published = tmpl.published;
        updateAdminBannerUI();
      }}
      renderGallery();
      if (tmpl.published) {{
        showSwalToast('تم تشغيل العرض للطلاب!', 'تم تفعيل وعرض الاستمارة وأصبحت مرئية لكافة الطلاب بنجاح.');
      }} else {{
        showSwalToast('تم توقيف العرض!', 'تم توقيف عرض الاستمارة وأصبحت مخفية عن الطلاب تماماً.');
      }}
    }};

    // Update Admin Banner UI in Workspace
    function updateAdminBannerUI() {{
      const badge = document.getElementById('panelPublishStatusBadge');
      const desc = document.getElementById('panelPublishStatusDesc');
      const toggleBtn = document.getElementById('btnTogglePublishInPanel');
      if (!badge || !desc || !toggleBtn || !currentTemplate) return;

      const isPub = currentTemplate.published !== false;
      if (isPub) {{
        badge.className = 'status-pill status-published';
        badge.innerHTML = `
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
          معروض للطلاب حالياً
        `;
        desc.innerText = 'هذا القالب معروض ومتاح حالياً لجميع الطلاب في قائمة الاستمارات الرسمية.';
        toggleBtn.className = 'btn btn-sm';
        toggleBtn.style.background = 'rgba(245,158,11,0.15)';
        toggleBtn.style.color = '#fbbf24';
        toggleBtn.style.border = '1.5px solid #f59e0b';
        toggleBtn.style.fontWeight = '800';
        toggleBtn.style.padding = '10px';
        toggleBtn.innerHTML = `
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="10" y1="15" x2="10" y2="9"></line><line x1="14" y1="15" x2="14" y2="9"></line></svg>
          توقيف العرض (إخفاء عن الطلاب)
        `;
      }} else {{
        badge.className = 'status-pill status-draft';
        badge.innerHTML = `
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"></line></svg>
          العرض متوقف (مخفي عن الطلاب)
        `;
        desc.innerText = 'هذا القالب متوقف عرضه ومخفي عن الطلاب، يمكنك تعديله ثم تشغيل العرض متى أردت.';
        toggleBtn.className = 'btn btn-sm';
        toggleBtn.style.background = '#10b981';
        toggleBtn.style.color = '#ffffff';
        toggleBtn.style.border = '1.5px solid #10b981';
        toggleBtn.style.fontWeight = '800';
        toggleBtn.style.padding = '10px';
        toggleBtn.innerHTML = `
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          تشغيل العرض (إتاحة للطلاب فوراً)
        `;
      }}
    }}

    window.deleteTemplate = function(templateId) {{
      const tmpl = templates.find(t => t.id === templateId);
      const title = tmpl ? tmpl.formTitle : 'هذه الاستمارة';
      showSwalConfirm({{
        title: 'حذف استمارة البحث نهائياً',
        desc: `هل أنت متأكد من حذف <strong>«${{title}}»</strong> نهائياً من قائمة القوالب؟<br><span class="warn-highlight">تنبيه: لن يتمكن الطلاب من الوصول إلى هذا القالب بعد حذفه!</span>`,
        confirmText: 'نعم، احذف القالب الآن',
        cancelText: 'تراجع',
        onConfirm: () => {{
          templates = templates.filter(t => t.id !== templateId);
          saveTemplates();
          renderGallery();
          showSwalToast('تم حذف القالب!', 'تمت إزالة الاستمارة من قائمة قوالب الطلاب بنجاح.');
        }}
      }});
    }};

    // Sync State to Control Panel
    function syncInputsFromState() {{
      if (!currentTemplate) return;
      document.getElementById('inputFormTitle').value = currentTemplate.formTitle;
      document.getElementById('inputAcademicYear').value = currentTemplate.academicYear;
      document.getElementById('inputInstLine1').value = currentTemplate.instLine1;
      document.getElementById('inputInstLine2').value = currentTemplate.instLine2;
      document.getElementById('inputInstLine3').value = currentTemplate.instLine3;
      document.getElementById('inputSignRightTitle').value = currentTemplate.signRightTitle;
      document.getElementById('inputSignLeftTitle').value = currentTemplate.signLeftTitle;
      document.getElementById('inputHeadName').value = currentTemplate.headName;
      document.getElementById('logoSizeSlider').value = currentTemplate.logoSize;
      document.getElementById('logoSizeVal').innerText = currentTemplate.logoSize + "px";

      document.getElementById('inputProjectNo').value = currentTemplate.projectNo || "";
      document.getElementById('inputProjectName').value = currentTemplate.projectName || "";
      document.getElementById('inputSupervisor').value = currentTemplate.supervisor || "";
      document.getElementById('inputRowCount').value = appState.rowCount;

      updateLogoPreviewUI();
      renderColumnsList();
      updatePresetPills();
    }}

    function updateLogoPreviewUI() {{
      if (!currentTemplate) return;
      const logoEl = document.getElementById('formLogoImg');
      const thumbEl = document.getElementById('logoPreviewThumb');
      const toggleBtn = document.getElementById('btnToggleLogo');

      if (currentTemplate.logoVisible && currentTemplate.logoData) {{
        logoEl.style.display = 'block';
        logoEl.src = currentTemplate.logoData;
        logoEl.style.maxHeight = currentTemplate.logoSize + 'px';
        thumbEl.src = currentTemplate.logoData;
        thumbEl.style.opacity = '1';
        toggleBtn.innerText = 'إخفاء الشعار';
      }} else {{
        logoEl.style.display = 'none';
        thumbEl.style.opacity = '0.3';
        toggleBtn.innerText = 'إظهار الشعار';
      }}
    }}

    // Render Preview
    function renderPreview() {{
      if (!currentTemplate) return;

      document.getElementById('previewFormTitle').innerText = currentTemplate.formTitle;
      document.getElementById('previewAcademicYear').innerText = currentTemplate.academicYear;
      document.getElementById('previewInstLine1').innerText = currentTemplate.instLine1;
      document.getElementById('previewInstLine2').innerText = currentTemplate.instLine2;
      document.getElementById('previewInstLine3').innerText = currentTemplate.instLine3;

      document.getElementById('previewProjectNo').innerText = currentTemplate.projectNo || "";
      document.getElementById('previewProjectName').innerText = currentTemplate.projectName || "";
      document.getElementById('previewSupervisor').innerText = currentTemplate.supervisor || "";

      document.getElementById('previewSignRightTitle').innerText = currentTemplate.signRightTitle;
      document.getElementById('previewSignLeftTitle').innerText = currentTemplate.signLeftTitle;
      document.getElementById('previewHeadName').innerText = currentTemplate.headName;

      renderTable();
    }}

    // Render Table - Strictly Right-To-Left Writing & Alignment!
    function renderTable() {{
      if (!currentTemplate) return;
      const thead = document.getElementById('tableHead');
      const tbody = document.getElementById('tableBody');

      const cols = currentTemplate.columns;

      let headHtml = '<tr>';
      cols.forEach(col => {{
        const isSeq = (col.autoSeq || col.id === 'col_seq');
        const thClass = isSeq ? 'col-seq-cell' : '';
        headHtml += `<th style="width: ${{col.width || 'auto'}};" class="${{thClass}}">${{col.name}}</th>`;
      }});
      headHtml += '</tr>';
      thead.innerHTML = headHtml;

      while (appState.tableData.length < appState.rowCount) {{
        appState.tableData.push({{}});
      }}

      let bodyHtml = '';
      const count = parseInt(appState.rowCount, 10) || 15;

      let cellHeight = '23px';
      let fontSize = '10pt';
      if (count > 25) {{
        cellHeight = '18px';
        fontSize = '8.5pt';
      }} else if (count > 18) {{
        cellHeight = '20px';
        fontSize = '9pt';
      }} else if (count <= 10) {{
        cellHeight = '30px';
        fontSize = '11pt';
      }}

      for (let r = 0; r < count; r++) {{
        const rowData = appState.tableData[r] || {{}};
        bodyHtml += `<tr style="height: ${{cellHeight}};">`;

        cols.forEach(col => {{
          const isSeq = (col.autoSeq || col.id === 'col_seq');
          let cellVal = rowData[col.id] || '';
          if (isSeq) {{
            cellVal = (r + 1).toString();
          }}

          // Sequence column is centered and read-only.
          // All other columns are editable by the student, aligning strictly from RIGHT to LEFT!
          if (isSeq) {{
            bodyHtml += `<td class="col-seq-cell" 
                             style="height: ${{cellHeight}}; font-size: ${{fontSize}};" 
                             contenteditable="false">${{cellVal}}</td>`;
          }} else {{
            bodyHtml += `<td style="height: ${{cellHeight}}; font-size: ${{fontSize}};" 
                             contenteditable="true" 
                             data-row="${{r}}" 
                             data-col="${{col.id}}" 
                             spellcheck="false">${{cellVal}}</td>`;
          }}
        }});

        bodyHtml += '</tr>';
      }}

      tbody.innerHTML = bodyHtml;

      // Event listener for in-table editing (persists student data)
      tbody.querySelectorAll('td[contenteditable="true"]').forEach(td => {{
        td.addEventListener('input', (e) => {{
          const r = parseInt(e.target.dataset.row, 10);
          const colId = e.target.dataset.col;
          if (!appState.tableData[r]) {{
            appState.tableData[r] = {{}};
          }}
          appState.tableData[r][colId] = e.target.innerText;
        }});
      }});
    }}

    // Render Admin Columns List
    function renderColumnsList() {{
      if (!currentTemplate) return;
      const container = document.getElementById('columnsContainer');
      container.innerHTML = '';

      currentTemplate.columns.forEach((col, index) => {{
        const div = document.createElement('div');
        div.className = 'column-item';
        div.innerHTML = `
          <div style="font-size:0.75rem; color:#64748b; font-weight:bold; min-width:20px;">#${{index + 1}}</div>
          <input type="text" class="col-name-input" value="${{col.name}}" data-index="${{index}}">
          <div class="column-actions">
            ${{index > 0 ? `<button type="button" class="col-icon-btn move-col-up" data-index="${{index}}" title="تحريك لليمين">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="18 15 12 9 6 15"></polyline></svg>
            </button>` : ''}}
            ${{index < currentTemplate.columns.length - 1 ? `<button type="button" class="col-icon-btn move-col-down" data-index="${{index}}" title="تحريك لليسار">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>` : ''}}
            <button type="button" class="col-icon-btn delete-col" data-index="${{index}}" title="حذف هذا العمود" ${{currentTemplate.columns.length <= 1 ? 'disabled style="opacity:0.3;"' : ''}}>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </button>
          </div>
        `;
        container.appendChild(div);
      }});

      container.querySelectorAll('.col-name-input').forEach(input => {{
        input.addEventListener('input', (e) => {{
          const idx = parseInt(e.target.dataset.index, 10);
          currentTemplate.columns[idx].name = e.target.value;
          renderPreview();
        }});
      }});

      container.querySelectorAll('.move-col-up').forEach(btn => {{
        btn.addEventListener('click', () => {{
          const idx = parseInt(btn.dataset.index, 10);
          if (idx > 0) {{
            const temp = currentTemplate.columns[idx];
            currentTemplate.columns[idx] = currentTemplate.columns[idx - 1];
            currentTemplate.columns[idx - 1] = temp;
            recalculateColumnWidths();
            renderColumnsList();
            renderPreview();
          }}
        }});
      }});

      container.querySelectorAll('.move-col-down').forEach(btn => {{
        btn.addEventListener('click', () => {{
          const idx = parseInt(btn.dataset.index, 10);
          if (idx < currentTemplate.columns.length - 1) {{
            const temp = currentTemplate.columns[idx];
            currentTemplate.columns[idx] = currentTemplate.columns[idx + 1];
            currentTemplate.columns[idx + 1] = temp;
            recalculateColumnWidths();
            renderColumnsList();
            renderPreview();
          }}
        }});
      }});

      container.querySelectorAll('.delete-col').forEach(btn => {{
        btn.addEventListener('click', () => {{
          if (currentTemplate.columns.length <= 1) return;
          const idx = parseInt(btn.dataset.index, 10);
          currentTemplate.columns.splice(idx, 1);
          recalculateColumnWidths();
          renderColumnsList();
          renderPreview();
        }});
      }});
    }}

    function recalculateColumnWidths() {{
      if (!currentTemplate) return;
      const cols = currentTemplate.columns;
      if (cols.length === 0) return;

      const hasSeq = cols.some(c => c.autoSeq || c.id === 'col_seq');
      let seqWidth = hasSeq ? 7 : 0;
      let remainingPercent = 100 - seqWidth;

      const otherCols = cols.filter(c => !(c.autoSeq || c.id === 'col_seq'));
      if (otherCols.length === 0) {{
        cols[0].width = '100%';
        return;
      }}

      let weights = {{}};
      otherCols.forEach(c => {{
        if (c.id === 'col_code') weights[c.id] = 23;
        else if (c.id === 'col_name') weights[c.id] = 42;
        else if (c.id === 'col_phone') weights[c.id] = 28;
        else weights[c.id] = 25;
      }});

      let totalWeight = 0;
      otherCols.forEach(c => totalWeight += weights[c.id]);

      cols.forEach(c => {{
        if (c.autoSeq || c.id === 'col_seq') {{
          c.width = '7%';
        }} else {{
          let percent = (weights[c.id] / totalWeight) * remainingPercent;
          c.width = percent.toFixed(1) + '%';
        }}
      }});
    }}

    function updatePresetPills() {{
      document.querySelectorAll('.preset-pill').forEach(pill => {{
        if (parseInt(pill.dataset.rows, 10) === parseInt(appState.rowCount, 10)) {{
          pill.classList.add('active');
        }} else {{
          pill.classList.remove('active');
        }}
      }});
    }}

    // Zoom & Screen Fit (Precise Mobile Layout)
    function setZoom(zoom) {{
      currentZoom = Math.min(Math.max(zoom, 0.20), 1.5);
      
      const baseWidthPx = 210 * 3.7795275591;
      const baseHeightPx = 297 * 3.7795275591;
      const scaledWidth = Math.round(baseWidthPx * currentZoom);
      const scaledHeight = Math.round(baseHeightPx * currentZoom);

      const scaleContainer = document.getElementById('paperScaleContainer');
      const wrapper = document.getElementById('paperWrapper');
      const viewport = document.getElementById('paperViewport');

      if (scaleContainer) {{
        scaleContainer.style.width = scaledWidth + 'px';
        scaleContainer.style.height = scaledHeight + 'px';
      }}

      if (wrapper) {{
        wrapper.style.transform = `scale(${{currentZoom}})`;
      }}

      if (viewport) {{
        viewport.style.minHeight = (scaledHeight + 20) + 'px';
      }}

      document.getElementById('zoomLabel').innerText = Math.round(currentZoom * 100) + '%';
    }}

    function fitToScreen() {{
      const container = document.getElementById('canvasArea');
      if (!container || container.clientWidth === 0) return;
      
      const isMobile = window.innerWidth <= 768;
      const margin = isMobile ? 12 : 48;
      const availableWidth = container.clientWidth - margin;
      
      const paperPxWidth = 210 * 3.7795275591;
      let fit = availableWidth / paperPxWidth;
      
      fit = Math.min(Math.max(fit, 0.22), 1.15);
      setZoom(fit);
    }}

    // Universal SweetAlert Confirmation & Toast Helpers
    let swalConfirmCallback = null;

    function showSwalConfirm(options) {{
      document.getElementById('swalConfirmTitle').innerText = options.title || 'تأكيد الحذف';
      document.getElementById('swalConfirmDesc').innerHTML = options.desc || 'هل أنت متأكد من تنفيذ هذه الخطوة؟';
      
      const confirmBtn = document.getElementById('swalConfirmBtn');
      confirmBtn.innerHTML = `
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="3 6 5 6 21 6"></polyline>
          <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
        </svg>
        ${{options.confirmText || 'نعم، تأكيد الحذف'}}
      `;
      document.getElementById('swalCancelBtn').innerText = options.cancelText || 'إلغاء الأمر';
      
      swalConfirmCallback = options.onConfirm;

      const modal = document.getElementById('swalConfirmModal');
      modal.style.display = 'flex';
      requestAnimationFrame(() => {{
        modal.classList.add('active');
      }});
    }}

    function closeSwalConfirm() {{
      const modal = document.getElementById('swalConfirmModal');
      modal.classList.remove('active');
      setTimeout(() => {{
        modal.style.display = 'none';
      }}, 200);
      swalConfirmCallback = null;
    }}

    function showSwalToast(title, msg) {{
      const toast = document.getElementById('swalToast');
      if (title) toast.querySelector('.swal-toast-title').innerText = title;
      if (msg) toast.querySelector('.swal-toast-msg').innerText = msg;
      toast.classList.add('show');
      setTimeout(() => {{
        toast.classList.remove('show');
      }}, 3200);
    }}

    // Secure Failed login attempt tracking & Persistent Lockout
    let failedAttempts = 0;
    let lockUntilTime = parseInt(localStorage.getItem("tiba_lockout_time") || "0", 10);

    // Initialization & Event Binding
    function init() {{
      loadTemplates();
      showGalleryView();

      // Navigation
      document.getElementById('brandHomeBtn').addEventListener('click', showGalleryView);
      document.getElementById('btnBrowseGallery').addEventListener('click', showGalleryView);
      document.getElementById('btnBackToGalleryFromPanel').addEventListener('click', showGalleryView);

      // Search & Filters
      document.getElementById('gallerySearchInput').addEventListener('input', renderGallery);
      document.querySelectorAll('#deptFilterPills .filter-pill').forEach(pill => {{
        pill.addEventListener('click', () => {{
          document.querySelectorAll('#deptFilterPills .filter-pill').forEach(p => p.classList.remove('active'));
          pill.classList.add('active');
          activeFilter = pill.dataset.filter;
          renderGallery();
        }});
      }});

      // Auth (Admin Login / Logout)
      const adminModal = document.getElementById('adminLoginModal');
      const feedbackEl = document.getElementById('loginFeedbackMsg');
      const passInput = document.getElementById('adminPasswordInput');

      document.getElementById('btnAuthToggle').addEventListener('click', () => {{
        if (currentRole === 'admin') {{
          currentRole = 'student';
          applyRolePermissions();
          if (document.getElementById('appWorkspace').classList.contains('active')) {{
            showWorkspaceView();
          }} else {{
            renderGallery();
          }}
        }} else {{
          passInput.value = '';
          feedbackEl.style.display = 'none';
          adminModal.classList.add('active');
          passInput.focus();
        }}
      }});

      document.getElementById('btnCloseLoginModal').addEventListener('click', () => {{
        adminModal.classList.remove('active');
      }});

      // Toggle password visibility
      document.getElementById('btnTogglePassVisibility').addEventListener('click', () => {{
        if (passInput.type === 'password') {{
          passInput.type = 'text';
        }} else {{
          passInput.type = 'password';
        }}
      }});

      // Submit Login
      async function handleAdminLogin() {{
        const now = Date.now();
        if (now < lockUntilTime) {{
          const remaining = Math.ceil((lockUntilTime - now) / 1000);
          feedbackEl.innerText = `تم حظر المحاولات مؤقتاً لتكرار الخطأ. انتظر ${{remaining}} ثانية.`;
          feedbackEl.style.display = 'block';
          return;
        }}

        const enteredPass = passInput.value.trim();
        if (!enteredPass) {{
          feedbackEl.innerText = 'يرجى إدخال كلمة المرور.';
          feedbackEl.style.display = 'block';
          return;
        }}

        const enteredHash = await sha256(enteredPass);
        const correctHash = getAdminHash();

        if (enteredHash === correctHash) {{
          failedAttempts = 0;
          lockUntilTime = 0;
          localStorage.removeItem("tiba_lockout_time");
          currentRole = 'admin';
          adminModal.classList.remove('active');
          applyRolePermissions();
          if (document.getElementById('appWorkspace').classList.contains('active')) {{
            showWorkspaceView();
          }} else {{
            renderGallery();
          }}
        }} else {{
          failedAttempts++;
          if (failedAttempts >= 3) {{
            lockUntilTime = Date.now() + 60000;
            localStorage.setItem("tiba_lockout_time", lockUntilTime.toString());
            feedbackEl.innerText = 'تم تجاوز عدد المحاولات المسموح بها! تم حظر المحاولات مؤقتاً لمدة 60 ثانية.';
          }} else {{
            feedbackEl.innerText = `كلمة المرور غير صحيحة. تبقى ${{3 - failedAttempts}} محاولات فقط.`;
          }}
          feedbackEl.style.display = 'block';
          passInput.value = '';
          passInput.focus();
        }}
      }}

      document.getElementById('btnSubmitAdminLogin').addEventListener('click', handleAdminLogin);
      passInput.addEventListener('keydown', (e) => {{
        if (e.key === 'Enter') handleAdminLogin();
      }});

      // Change Password Modal
      const changePassModal = document.getElementById('changePassModal');
      const changeFeedback = document.getElementById('changePassFeedback');

      const openChangePassModal = () => {{
        document.getElementById('inputOldPass').value = '';
        document.getElementById('inputNewPass').value = '';
        document.getElementById('inputConfirmPass').value = '';
        changeFeedback.style.display = 'none';
        changePassModal.classList.add('active');
      }};

      document.getElementById('btnAdminChangePass').addEventListener('click', openChangePassModal);
      const btnInPanel = document.getElementById('btnChangePassInPanel');
      if (btnInPanel) btnInPanel.addEventListener('click', openChangePassModal);

      document.getElementById('btnCloseChangePass').addEventListener('click', () => {{
        changePassModal.classList.remove('active');
      }});

      document.getElementById('btnSaveNewPass').addEventListener('click', async () => {{
        const oldPass = document.getElementById('inputOldPass').value.trim();
        const newPass = document.getElementById('inputNewPass').value.trim();
        const confirmPass = document.getElementById('inputConfirmPass').value.trim();

        const oldHash = await sha256(oldPass);
        if (oldHash !== getAdminHash()) {{
          changeFeedback.style.color = '#ef4444';
          changeFeedback.innerText = 'كلمة المرور الحالية غير صحيحة.';
          changeFeedback.style.display = 'block';
          return;
        }}

        if (!newPass || newPass.length < 4) {{
          changeFeedback.style.color = '#ef4444';
          changeFeedback.innerText = 'كلمة المرور الجديدة يجب ألا تقل عن 4 خانات.';
          changeFeedback.style.display = 'block';
          return;
        }}

        if (newPass !== confirmPass) {{
          changeFeedback.style.color = '#ef4444';
          changeFeedback.innerText = 'كلمة المرور الجديدة وتأكيدها غير متطابقين.';
          changeFeedback.style.display = 'block';
          return;
        }}

        const newHash = await sha256(newPass);
        localStorage.setItem("tiba_admin_hash_v2", newHash);
        changeFeedback.style.color = '#10b981';
        changeFeedback.innerText = 'تم تحديث كلمة المرور وتشفيرها بنجاح!';
        changeFeedback.style.display = 'block';

        setTimeout(() => {{
          changePassModal.classList.remove('active');
        }}, 1200);
      }});

      // Admin Delete All Templates
      const btnAdminDeleteAll = document.getElementById('btnAdminDeleteAll');
      if (btnAdminDeleteAll) {{
        btnAdminDeleteAll.addEventListener('click', () => {{
          showSwalConfirm({{
            title: 'حذف كافة القوالب نهائياً',
            desc: 'هل أنت متأكد من حذف جميع استمارات وقوالب البحث نهائياً من المنصة؟<br><span class="warn-highlight">تنبيه: لن يظهر أي قالب للطلاب حتى تقوم بإنشاء قوالب جديدة!</span>',
            confirmText: 'نعم، احذف كافة القوالب',
            cancelText: 'إلغاء',
            onConfirm: () => {{
              templates = [];
              saveTemplates();
              renderGallery();
              showSwalToast('تم حذف كافة القوالب!', 'تم تفريغ قائمة القوالب بالكامل.');
            }}
          }});
        }});
      }}

      // Admin Create New Template (Saved as Draft initially)
      document.getElementById('btnAdminCreateNew').addEventListener('click', () => {{
        const newTitle = prompt('أدخل عنوان استمارة البحث الجديدة:', 'استمارة بحث تخرج جديدة');
        if (!newTitle) return;
        const newDept = prompt('أدخل اسم القسم العلمي التابع له الاستمارة:', 'قسم نظم معلومات الأعمال');
        if (!newDept) return;

        const newTmpl = {{
          id: 'tmpl_' + Date.now(),
          dept: newDept.trim(),
          formTitle: newTitle.trim(),
          published: false, // Default is DRAFT (not published immediately)
          instLine1: "معاهد طيبة العليا",
          instLine2: "المعهد العالي لتكنولوجيا الإدارة والمعلومات",
          instLine3: newDept.trim(),
          academicYear: "العام الجامعي 2024 / 2025",
          projectNo: "",
          projectName: "",
          supervisor: "",
          signRightTitle: "أستاذ المادة المشرف",
          signLeftTitle: "رئيس القسم",
          headName: "أ.د/ إبراهيم سليم",
          logoVisible: true,
          logoSize: 58,
          logoData: DEFAULT_LOGO_B64,
          columns: [
            {{ id: "col_seq", name: "م", width: "7%", autoSeq: true }},
            {{ id: "col_code", name: "كود الطالب", width: "23%", autoSeq: false }},
            {{ id: "col_name", name: "اسم الطالب", width: "42%", autoSeq: false }},
            {{ id: "col_phone", name: "رقم التليفون", width: "28%", autoSeq: false }}
          ],
          rowCount: 15
        }};

        templates.unshift(newTmpl);
        saveTemplates();
        selectTemplate(newTmpl.id);
        showSwalToast('تم حفظ القالب كمسودة!', 'تم إنشاء القالب وحفظه كمسودة خاصة بالإدارة. يمكنك ضبطه ونشره للطلاب متى شئت.');
      }});

      // Admin Save Current Template Changes
      const btnSaveTemplateChanges = document.getElementById('btnSaveTemplateChanges');
      if (btnSaveTemplateChanges) {{
        btnSaveTemplateChanges.addEventListener('click', () => {{
          if (!currentTemplate) return;
          const idx = templates.findIndex(t => t.id === currentTemplate.id);
          if (idx !== -1) {{
            templates[idx] = JSON.parse(JSON.stringify(currentTemplate));
          }} else {{
            templates.push(JSON.parse(JSON.stringify(currentTemplate)));
          }}
          saveTemplates();
          showSwalToast('تم حفظ التعديلات!', 'تم حفظ بيانات وتنسيقات القالب بنجاح.');
        }});
      }}

      // Admin Toggle Publish from Panel
      const btnTogglePublishInPanel = document.getElementById('btnTogglePublishInPanel');
      if (btnTogglePublishInPanel) {{
        btnTogglePublishInPanel.addEventListener('click', () => {{
          if (!currentTemplate) return;
          togglePublishTemplate(currentTemplate.id);
        }});
      }}

      // Mobile Tabs
      const tabBtnEdit = document.getElementById('tabBtnEdit');
      const tabBtnPreview = document.getElementById('tabBtnPreview');

      tabBtnEdit.addEventListener('click', () => {{
        tabBtnEdit.classList.add('active');
        tabBtnPreview.classList.remove('active');
        document.body.classList.remove('show-preview-mode');
      }});

      tabBtnPreview.addEventListener('click', () => {{
        tabBtnPreview.classList.add('active');
        tabBtnEdit.classList.remove('active');
        document.body.classList.add('show-preview-mode');
        setTimeout(() => {{ fitToScreen(); }}, 50);
      }});

      // Admin Project Inputs & Direct Bindings
      document.getElementById('inputProjectNo').addEventListener('input', (e) => {{
        if (currentRole === 'admin' && currentTemplate) {{
          currentTemplate.projectNo = e.target.value;
          renderPreview();
        }}
      }});
      document.getElementById('inputProjectName').addEventListener('input', (e) => {{
        if (currentRole === 'admin' && currentTemplate) {{
          currentTemplate.projectName = e.target.value;
          renderPreview();
        }}
      }});
      document.getElementById('inputSupervisor').addEventListener('input', (e) => {{
        if (currentRole === 'admin' && currentTemplate) {{
          currentTemplate.supervisor = e.target.value;
          renderPreview();
        }}
      }});
      document.getElementById('inputAcademicYear').addEventListener('input', (e) => {{
        if (currentRole === 'admin' && currentTemplate) {{
          currentTemplate.academicYear = e.target.value;
          renderPreview();
        }}
      }});

      // In-preview Project editing for Admin only
      document.getElementById('previewProjectNo').addEventListener('input', (e) => {{
        if (currentRole === 'admin' && currentTemplate) {{
          currentTemplate.projectNo = e.target.innerText;
          document.getElementById('inputProjectNo').value = currentTemplate.projectNo;
        }}
      }});
      document.getElementById('previewProjectName').addEventListener('input', (e) => {{
        if (currentRole === 'admin' && currentTemplate) {{
          currentTemplate.projectName = e.target.innerText;
          document.getElementById('inputProjectName').value = currentTemplate.projectName;
        }}
      }});
      document.getElementById('previewSupervisor').addEventListener('input', (e) => {{
        if (currentRole === 'admin' && currentTemplate) {{
          currentTemplate.supervisor = e.target.innerText;
          document.getElementById('inputSupervisor').value = currentTemplate.supervisor;
        }}
      }});

      // Admin Design Bindings
      document.getElementById('previewFormTitle').addEventListener('input', (e) => {{
        if (currentRole === 'admin' && currentTemplate) {{
          currentTemplate.formTitle = e.target.innerText;
          document.getElementById('inputFormTitle').value = currentTemplate.formTitle;
        }}
      }});

      const bindAdminInput = (id, prop) => {{
        document.getElementById(id).addEventListener('input', (e) => {{
          if (currentTemplate) {{
            currentTemplate[prop] = e.target.value;
            renderPreview();
          }}
        }});
      }};

      bindAdminInput('inputFormTitle', 'formTitle');
      bindAdminInput('inputInstLine1', 'instLine1');
      bindAdminInput('inputInstLine2', 'instLine2');
      bindAdminInput('inputInstLine3', 'instLine3');
      bindAdminInput('inputSignRightTitle', 'signRightTitle');
      bindAdminInput('inputSignLeftTitle', 'signLeftTitle');
      bindAdminInput('inputHeadName', 'headName');

      // Row Stepper
      const rowCountInput = document.getElementById('inputRowCount');
      rowCountInput.addEventListener('change', (e) => {{
        let val = parseInt(e.target.value, 10);
        if (isNaN(val) || val < 1) val = 1;
        if (val > 45) val = 45;
        appState.rowCount = val;
        if (currentTemplate) currentTemplate.rowCount = val;
        rowCountInput.value = val;
        updatePresetPills();
        renderPreview();
      }});

      document.getElementById('btnIncRow').addEventListener('click', () => {{
        appState.rowCount = Math.min(45, (parseInt(appState.rowCount, 10) || 15) + 1);
        if (currentTemplate) currentTemplate.rowCount = appState.rowCount;
        rowCountInput.value = appState.rowCount;
        updatePresetPills();
        renderPreview();
      }});

      document.getElementById('btnDecRow').addEventListener('click', () => {{
        appState.rowCount = Math.max(1, (parseInt(appState.rowCount, 10) || 15) - 1);
        if (currentTemplate) currentTemplate.rowCount = appState.rowCount;
        rowCountInput.value = appState.rowCount;
        updatePresetPills();
        renderPreview();
      }});

      document.getElementById('btnAddRow').addEventListener('click', () => document.getElementById('btnIncRow').click());
      document.getElementById('btnDeleteRow').addEventListener('click', () => document.getElementById('btnDecRow').click());

      document.querySelectorAll('.preset-pill').forEach(pill => {{
        pill.addEventListener('click', () => {{
          appState.rowCount = parseInt(pill.dataset.rows, 10);
          if (currentTemplate) currentTemplate.rowCount = appState.rowCount;
          rowCountInput.value = appState.rowCount;
          updatePresetPills();
          renderPreview();
        }});
      }});

      // Admin Add Column
      document.getElementById('btnAddColumn').addEventListener('click', () => {{
        if (!currentTemplate) return;
        const colTitle = prompt('أدخل اسم العمود الجديد:', 'القسم');
        if (colTitle && colTitle.trim()) {{
          const newId = 'col_' + Date.now();
          currentTemplate.columns.push({{
            id: newId,
            name: colTitle.trim(),
            width: '20%',
            autoSeq: false
          }});
          recalculateColumnWidths();
          renderColumnsList();
          renderPreview();
        }}
      }});

      document.getElementById('btnResetColumns').addEventListener('click', () => {{
        showSwalConfirm({{
          title: 'إعادة تعيين الأعمدة الافتراضية',
          desc: 'هل تريد إعادة أعمدة الجدول إلى الأعمدة الرسمية الأصلية للمعهد؟<br><span class="warn-highlight">تنبيه: سيتم إعادة ضبط الأعمدة الأربعة الافتراضية.</span>',
          confirmText: 'نعم، إعادة ضبط الأعمدة',
          cancelText: 'إلغاء',
          onConfirm: () => {{
            currentTemplate.columns = JSON.parse(JSON.stringify(INITIAL_TEMPLATES[0].columns));
            recalculateColumnWidths();
            renderColumnsList();
            renderPreview();
            showSwalToast('تمت إعادة الضبط!', 'تمت إعادة الأعمدة إلى التوزيع الافتراضي.');
          }}
        }});
      }});

      // Admin Logo
      const fileInput = document.getElementById('logoFileInput');
      fileInput.addEventListener('change', (e) => {{
        const file = e.target.files[0];
        if (file && currentTemplate) {{
          const reader = new FileReader();
          reader.onload = (event) => {{
            currentTemplate.logoData = event.target.result;
            currentTemplate.logoVisible = true;
            updateLogoPreviewUI();
            renderPreview();
          }};
          reader.readAsDataURL(file);
        }}
      }});

      document.getElementById('btnToggleLogo').addEventListener('click', () => {{
        if (currentTemplate) {{
          currentTemplate.logoVisible = !currentTemplate.logoVisible;
          updateLogoPreviewUI();
        }}
      }});

      document.getElementById('btnResetLogo').addEventListener('click', () => {{
        if (currentTemplate) {{
          currentTemplate.logoData = DEFAULT_LOGO_B64;
          currentTemplate.logoVisible = true;
          updateLogoPreviewUI();
          renderPreview();
        }}
      }});

      document.getElementById('logoSizeSlider').addEventListener('input', (e) => {{
        if (currentTemplate) {{
          currentTemplate.logoSize = e.target.value;
          document.getElementById('logoSizeVal').innerText = currentTemplate.logoSize + 'px';
          updateLogoPreviewUI();
        }}
      }});

      // Zoom
      document.getElementById('btnZoomIn').addEventListener('click', () => setZoom(currentZoom + 0.1));
      document.getElementById('btnZoomOut').addEventListener('click', () => setZoom(currentZoom - 0.1));
      document.getElementById('btnZoomReset').addEventListener('click', () => setZoom(1.0));
      document.getElementById('btnZoomFit').addEventListener('click', fitToScreen);

      // SweetAlert Confirm & Cancel Modal Bindings
      document.getElementById('swalConfirmBtn').addEventListener('click', () => {{
        if (typeof swalConfirmCallback === 'function') {{
          const cb = swalConfirmCallback;
          swalConfirmCallback = null;
          cb();
        }}
        closeSwalConfirm();
      }});

      document.getElementById('swalCancelBtn').addEventListener('click', closeSwalConfirm);

      document.getElementById('swalConfirmModal').addEventListener('click', (e) => {{
        if (e.target.id === 'swalConfirmModal') closeSwalConfirm();
      }});

      // Clear Table Data Trigger with SweetAlert
      document.getElementById('btnClearData').addEventListener('click', () => {{
        showSwalConfirm({{
          title: 'هل أنت متأكد من تفريغ الجدول؟',
          desc: 'سيتم مسح جميع البيانات والأسماء التي أدخلتها في جدول الطلاب بالكامل.<br><span class="warn-highlight">تنبيه: لن تتمكن من التراجع عن هذه الخطوة بعد التأكيد!</span>',
          confirmText: 'نعم، تفريغ الجدول الآن',
          cancelText: 'إلغاء الأمر',
          onConfirm: () => {{
            appState.tableData = [];
            renderTable();
            showSwalToast('تم تفريغ الجدول بنجاح!', 'تم مسح كافة البيانات وأصبح الجدول فارغاً للكتابة.');
          }}
        }});
      }});

      // Print
      const printModal = document.getElementById('printModal');
      document.getElementById('btnPrintPdf').addEventListener('click', () => {{
        printModal.classList.add('active');
      }});

      document.getElementById('btnCloseModal').addEventListener('click', () => {{
        printModal.classList.remove('active');
      }});

      document.getElementById('btnConfirmPrint').addEventListener('click', () => {{
        printModal.classList.remove('active');
        setTimeout(() => {{ window.print(); }}, 200);
      }});

      printModal.addEventListener('click', (e) => {{
        if (e.target === printModal) printModal.classList.remove('active');
      }});
    }}

    window.addEventListener('DOMContentLoaded', init);

    let resizeTimer;
    window.addEventListener('resize', () => {{
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => {{
        if (document.getElementById('appWorkspace').classList.contains('active')) {{
          if (document.body.classList.contains('show-preview-mode') || window.innerWidth > 1024) {{
            fitToScreen();
          }}
        }}
      }}, 100);
    }});
  </script>
</body>
</html>'''

with open("/Users/mac/Desktop/tiba/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Masterpiece built! SHA-256 secure admin password, student instructions always visible. Size: {len(html_content)} bytes")
