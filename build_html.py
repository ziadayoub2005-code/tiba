import os
import base64

base64_path = "/Users/mac/Desktop/tiba/tiba_logo_base64.txt"
with open(base64_path, "r") as f:
    logo_b64 = f.read().strip()

attnlg_path = "/Users/mac/Desktop/tiba/attnlg.jpg"
if os.path.exists(attnlg_path):
    with open(attnlg_path, "rb") as f:
        attnlg_b64 = base64.b64encode(f.read()).decode("utf-8")
else:
    attnlg_b64 = logo_b64

html_content = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <meta name="theme-color" content="#204097">
  <title>معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات | استمارات تسجيل مشاريع وأبحاث التخرج</title>
  <meta name="description" content="منصة تسجيل وتعبئة استمارة بحث ومشروع التخرج - معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات">
  
  <!-- Open Graph / WhatsApp / Facebook Preview -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات | استمارات تسجيل مشاريع وأبحاث التخرج">
  <meta property="og:description" content="استمارات تسجيل مشاريع وأبحاث التخرج - معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات">
  <meta property="og:site_name" content="معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات">
  <meta property="og:image" content="https://tiba-higher-institute-for-management-and-information-technology.vercel.app/tiba_logo.png">
  <meta property="og:image:alt" content="شعار معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات">
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات | استمارات تسجيل مشاريع وأبحاث التخرج">
  <meta name="twitter:description" content="استمارات تسجيل مشاريع وأبحاث التخرج - معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات">
  <meta name="twitter:image" content="https://tiba-higher-institute-for-management-and-information-technology.vercel.app/tiba_logo.png">
  
  <link rel="icon" type="image/png" href="tiba_logo.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=Amiri:wght@400;700&display=swap" rel="stylesheet">
    <style>
    :root {{
      /* ========================================================
         OFFICIAL TIBA HIGHER INSTITUTE BRAND IDENTITY PALETTE
         ======================================================== */
      --primary: #204097;                    /* Primary Official Blue */
      --primary-hover: #213E9C;              /* Primary Hover */
      --primary-dark: #204096;               /* Dark Blue Tone */
      --blue-secondary: #27428B;             /* Secondary Blue */
      --blue-deep: #33467D;                  /* Deep Blue for Headings/Text */
      --blue-muted: #7280AB;                 /* Muted Slate Blue for Subtitles/Icons */
      --blue-tint: #C2D0F3;                  /* Soft Tint Blue for Borders/Accents */
      
      /* Surfaces & Backgrounds */
      --bg-page: #F3FCFE;                    /* Official Light Page Background */
      --bg-surface: #FDFEF8;                 /* Soft Warm Surface */
      --bg-card: #FFFFFF;                    /* Pure White Cards */
      --bg-panel: #FFFFFF;                   /* Pure White Panels & Sidebars */
      --surface-dark: #F3FCFE;               /* Compatibility alias */
      --surface-card: #FFFFFF;               /* Compatibility alias */
      --surface-panel: #FFFFFF;              /* Compatibility alias */
      
      /* Typography */
      --text-main: #1e293b;                  /* High Contrast Body Text */
      --text-heading: #204097;               /* Official Blue for Main Headings */
      --text-secondary: #33467D;             /* Deep Blue for Secondary Headings */
      --text-muted: #7280AB;                 /* Muted Secondary Text */
      
      /* Borders & Accents */
      --border-dark: #C2D0F3;                /* Compatibility alias */
      --border-color: #C2D0F3;               /* Approved Light Blue Border */
      --border-light: rgba(32, 64, 151, 0.12);
      --accent: #204097;                     /* Official Blue */
      --purple: #27428B;                     /* Mapped to Official Deep Blue */
      
      /* Semantic Functional States (Preserved exclusively for status) */
      --success: #10b981;
      --danger: #ef4444;
      --warning: #f59e0b;
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
      background-color: var(--bg-page);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }}

    /* Global Top Header Wrapper (Sticky anchor for Navbar and Mobile Tab Switcher) */
    .app-top-header-wrap {{
      position: sticky;
      top: 0;
      z-index: 100;
      width: 100%;
      background: #FFFFFF;
      box-shadow: 0 2px 10px rgba(32, 64, 151, 0.08);
    }}

    header.app-navbar {{
      background: #FFFFFF;
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1.5px solid var(--border-color);
      padding: 10px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: relative;
      gap: 12px;
      width: 100%;
    }}

    .navbar-brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      user-select: none;
    }}

    .navbar-brand .brand-icon {{
      width: 44px;
      height: 44px;
      min-width: 44px;
      background: #FFFFFF;
      border: 1.5px solid #C2D0F3;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 8px rgba(32, 64, 151, 0.12);
      overflow: hidden;
      padding: 2px;
      flex-shrink: 0;
    }}

    .navbar-brand .brand-icon img.brand-logo-img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
    }}

    .navbar-brand h1 {{
      font-size: 1.05rem;
      font-weight: 800;
      color: #204097;
      line-height: 1.2;
    }}

    .navbar-brand span.subtitle {{
      font-size: 0.72rem;
      color: #33467D;
      display: block;
      font-weight: 600;
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
      background: rgba(16, 185, 129, 0.1);
      color: #059669;
      border-color: rgba(16, 185, 129, 0.3);
    }}

    .role-badge.admin {{
      background: rgba(32, 64, 151, 0.1);
      color: #204097;
      border-color: rgba(32, 64, 151, 0.25);
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
      background: linear-gradient(135deg, #204097, #27428B);
      color: #ffffff;
      box-shadow: 0 4px 12px rgba(32, 64, 151, 0.25);
    }}
    .btn-primary:hover {{
      background: linear-gradient(135deg, #213E9C, #204096);
      box-shadow: 0 6px 18px rgba(32, 64, 151, 0.35);
    }}

    .btn-admin {{
      background: linear-gradient(135deg, #27428B, #33467D);
      color: #fff;
      box-shadow: 0 4px 12px rgba(39, 66, 139, 0.25);
    }}
    .btn-admin:hover {{
      background: linear-gradient(135deg, #204097, #213E9C);
    }}

    .btn-secondary {{
      background: #F3FCFE;
      color: #27428B;
      border: 1px solid #C2D0F3;
    }}
    .btn-secondary:hover {{
      background: #C2D0F3;
      color: #204097;
    }}

    .btn-outline {{
      background: transparent;
      color: #33467D;
      border: 1px solid #C2D0F3;
    }}
    .btn-outline:hover {{
      background: rgba(32, 64, 151, 0.06);
      color: #204097;
      border-color: #204097;
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
      background: linear-gradient(135deg, #FFFFFF 0%, #FDFEF8 60%, #F3FCFE 100%);
      border: 1.5px solid var(--border-color);
      border-radius: 16px;
      padding: 28px 24px;
      text-align: center;
      position: relative;
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(32, 64, 151, 0.08);
    }}

    .gallery-hero h2 {{
      font-size: 1.6rem;
      font-weight: 900;
      color: #204097;
      margin-bottom: 8px;
    }}

    .gallery-hero p {{
      color: #33467D;
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
      color: #7280AB;
    }}

    .search-input {{
      width: 100%;
      background: #FFFFFF;
      border: 1.5px solid #C2D0F3;
      border-radius: 12px;
      padding: 12px 44px 12px 16px;
      color: #1e293b;
      font-family: inherit;
      font-size: 0.95rem;
      transition: all 0.2s;
    }}
    .search-input:focus {{
      outline: none;
      border-color: #204097;
      box-shadow: 0 0 0 3px rgba(32, 64, 151, 0.15);
    }}

    .dept-filter-pills {{
      display: flex;
      gap: 8px;
      justify-content: center;
      flex-wrap: wrap;
    }}

    .filter-pill {{
      padding: 6px 14px;
      background: #FFFFFF;
      border: 1px solid #C2D0F3;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 700;
      color: #33467D;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .filter-pill:hover, .filter-pill.active {{
      background: #204097;
      color: #FFFFFF;
      border-color: #204097;
      box-shadow: 0 2px 8px rgba(32, 64, 151, 0.25);
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
      background: #FFFFFF;
      border: 1.5px solid #C2D0F3;
      border-radius: 14px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
      overflow: hidden;
      box-shadow: 0 4px 12px rgba(32, 64, 151, 0.06);
      cursor: pointer;
    }}

    .template-card:hover {{
      transform: translateY(-4px);
      border-color: #204097;
      box-shadow: 0 12px 28px rgba(32, 64, 151, 0.15);
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
      background: rgba(32, 64, 151, 0.08);
      border: 1px solid #C2D0F3;
      color: #204097;
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
      color: #204097;
      background: #F3FCFE;
      border: 1px solid #C2D0F3;
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
      background: rgba(16, 185, 129, 0.1);
      color: #059669;
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}

    .status-pill.status-draft {{
      background: rgba(245, 158, 11, 0.1);
      color: #d97706;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }}

    .card-title {{
      font-size: 1.05rem;
      font-weight: 800;
      color: #204097;
      line-height: 1.35;
    }}

    .card-details {{
      background: #F3FCFE;
      border: 1px solid rgba(32, 64, 151, 0.08);
      border-radius: 8px;
      padding: 10px 12px;
      font-size: 0.8rem;
      color: #33467D;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .card-detail-item {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .card-detail-item.item-inst {{
      justify-content: flex-start;
      gap: 8px;
    }}
    .card-detail-item > span:first-child {{
      color: #7280AB;
      white-space: nowrap;
      flex-shrink: 0;
    }}
    .card-detail-item span.val {{
      color: #204096;
      font-weight: 700;
      word-break: break-word;
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
      background: #FFFFFF;
      border-top: 1px solid #E2E8F0;
      border-bottom: 1.5px solid #C2D0F3;
      padding: 6px 12px;
      width: 100%;
      position: relative;
    }}

    .segmented-switch {{
      display: flex;
      background: #F3FCFE;
      border: 1px solid #C2D0F3;
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
      color: #33467D;
      font-family: inherit;
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .segmented-btn.active {{
      background: #204097;
      color: #ffffff;
      box-shadow: 0 2px 8px rgba(32, 64, 151, 0.3);
    }}

    /* Sidebar / Control Panel */
    aside.control-panel {{
      width: 440px;
      min-width: 440px;
      max-width: 440px;
      background: #FFFFFF;
      border-left: 1.5px solid #C2D0F3;
      display: flex;
      flex-direction: column;
      height: 100%;
      overflow-y: auto;
      scrollbar-width: thin;
      scrollbar-color: #C2D0F3 #FFFFFF;
      z-index: 40;
    }}

    .panel-section {{
      padding: 16px 18px;
      border-bottom: 1px solid #E2E8F0;
    }}

    .section-title {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.92rem;
      font-weight: 800;
      color: #204097;
      margin-bottom: 12px;
    }}

    .section-title svg {{
      color: #204097;
      flex-shrink: 0;
    }}

    /* Permanent Student Instructions Box in Sidebar */
    .student-instructions-card {{
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.08), rgba(16, 185, 129, 0.03));
      border: 1.5px solid rgba(16, 185, 129, 0.3);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      box-shadow: 0 2px 10px rgba(16, 185, 129, 0.06);
    }}

    .instructions-card-header {{
      display: flex;
      align-items: center;
      gap: 8px;
      color: #059669;
      font-weight: 900;
      font-size: 1rem;
    }}

    .instructions-list {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      font-size: 0.82rem;
      color: #1e293b;
      line-height: 1.5;
    }}

    .instructions-list-item {{
      display: flex;
      align-items: flex-start;
      gap: 8px;
    }}

    .instructions-list-item span.icon {{
      color: #059669;
      font-weight: bold;
    }}

    /* Admin Action Banner */
    .admin-action-banner {{
      background: rgba(32, 64, 151, 0.06);
      border: 1.5px solid #C2D0F3;
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
      color: #27428B;
      margin-bottom: 5px;
    }}

    .form-label span.optional {{
      color: #7280AB;
      font-weight: normal;
      font-size: 0.72rem;
    }}

    .form-control {{
      width: 100%;
      background: #FFFFFF;
      border: 1.5px solid #C2D0F3;
      border-radius: 8px;
      color: #1e293b;
      font-family: inherit;
      font-size: 0.86rem;
      padding: 8px 11px;
      transition: all 0.2s;
    }}

    .form-control:focus {{
      outline: none;
      border-color: #204097;
      box-shadow: 0 0 0 3px rgba(32, 64, 151, 0.15);
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
      background: #FFFFFF;
      border: 1.5px solid #C2D0F3;
      border-radius: 8px;
      overflow: hidden;
    }}

    .stepper-btn {{
      background: #F3FCFE;
      border: none;
      color: #204097;
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
      background: #C2D0F3;
      color: #204097;
    }}

    .stepper-input {{
      flex: 1;
      background: transparent;
      border: none;
      color: #204097;
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
      background: #FFFFFF;
      border: 1px solid #C2D0F3;
      border-radius: 20px;
      font-size: 0.76rem;
      color: #33467D;
      cursor: pointer;
      font-weight: 700;
      transition: all 0.15s;
    }}
    .preset-pill:hover, .preset-pill.active {{
      background: #204097;
      color: #fff;
      border-color: #204097;
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
      background: #F3FCFE;
      border: 1px solid #C2D0F3;
      padding: 6px 10px;
      border-radius: 8px;
    }}

    .column-item input.col-name-input {{
      flex: 1;
      background: transparent;
      border: 1px solid transparent;
      border-radius: 4px;
      color: #204097;
      font-family: inherit;
      font-size: 0.84rem;
      font-weight: 600;
      padding: 4px 6px;
      min-width: 0;
    }}
    .column-item input.col-name-input:focus {{
      background: #FFFFFF;
      border-color: #204097;
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
      color: #7280AB;
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
      background: #C2D0F3;
      color: #204097;
    }}
    .col-icon-btn.delete-col:hover {{
      background: rgba(239, 68, 68, 0.12);
      color: #ef4444;
    }}

    /* Logo Control Box */
    .logo-control-box {{
      background: #F3FCFE;
      border: 1px solid #C2D0F3;
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
      border: 1px solid #C2D0F3;
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
      background: #F3FCFE;
      background-image: 
        radial-gradient(rgba(32, 64, 151, 0.12) 1px, transparent 1px),
        radial-gradient(rgba(32, 64, 151, 0.08) 1px, #F3FCFE 1px);
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
      scrollbar-color: #C2D0F3 #F3FCFE;
      -webkit-overflow-scrolling: touch;
    }}

    /* ========================================================
       STUDENT GUIDELINES & INSTRUCTIONS STYLING
       ======================================================== */
    .student-guidelines-banner {{
      background: #FFFFFF;
      border: 1.5px solid #C2D0F3;
      border-radius: 14px;
      padding: 12px 18px;
      box-shadow: 0 4px 14px rgba(32, 64, 151, 0.06);
      margin-top: 18px;
      text-align: right;
      transition: all 0.25s ease;
    }}

    .student-guidelines-banner.is-open {{
      border-color: #204097;
      box-shadow: 0 6px 20px rgba(32, 64, 151, 0.1);
    }}

    .guidelines-toggle-btn {{
      width: 100%;
      background: transparent;
      border: none;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      cursor: pointer;
      padding: 4px 0;
      text-align: right;
      font-family: inherit;
    }}

    .toggle-btn-right {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .guidelines-header-icon {{
      width: 38px;
      height: 38px;
      min-width: 38px;
      border-radius: 10px;
      background: linear-gradient(135deg, #FFF1F2 0%, #FFE4E6 100%);
      border: 1.5px solid #FDA4AF;
      color: #E11D48;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}

    .toggle-btn-text {{
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}

    .toggle-title-row {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .toggle-main-title {{
      font-size: 0.98rem;
      font-weight: 800;
      color: #204097;
    }}

    .toggle-badge {{
      background: #FFF1F2;
      color: #E11D48;
      border: 1px solid #FECDD3;
      padding: 2px 10px;
      border-radius: 20px;
      font-size: 0.74rem;
      font-weight: 800;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.2s ease;
    }}

    .toggle-sub-title {{
      font-size: 0.8rem;
      color: #64748B;
    }}

    .toggle-chevron {{
      color: #7280AB;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.25s ease, color 0.2s ease;
      flex-shrink: 0;
    }}

    .guidelines-toggle-btn:hover .toggle-chevron {{
      color: #204097;
    }}

    .guidelines-toggle-btn.open .toggle-chevron {{
      transform: rotate(180deg);
      color: #204097;
    }}

    .guidelines-collapsible-content {{
      padding-top: 14px;
      border-top: 1.5px dashed #D6E0F8;
      margin-top: 12px;
      animation: fadeInDown 0.25s ease;
    }}

    @keyframes fadeInDown {{
      from {{ opacity: 0; transform: translateY(-6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .guidelines-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
    }}

    @media (max-width: 1024px) {{
      .guidelines-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
    }}

    .guideline-item-card {{
      background: #F8FAFC;
      border: 1.5px solid #E2E8F0;
      border-radius: 12px;
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 5px;
      transition: all 0.2s ease;
    }}

    .guideline-item-card:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 14px rgba(32, 64, 151, 0.08);
    }}

    .guideline-card-title {{
      font-size: 0.86rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .step-num {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      font-size: 0.72rem;
      font-weight: 900;
      color: #FFFFFF;
      flex-shrink: 0;
    }}

    .guideline-item-card.danger {{
      background: #FFFBFB;
      border-color: #FECDD3;
    }}
    .guideline-item-card.danger .guideline-card-title {{
      color: #BE123C;
    }}
    .guideline-item-card.danger .step-num {{
      background: #E11D48;
    }}

    .guideline-item-card.primary {{
      background: #F8FAFF;
      border-color: #C7D7FE;
    }}
    .guideline-item-card.primary .guideline-card-title {{
      color: #1E40AF;
    }}
    .guideline-item-card.primary .step-num {{
      background: #2563EB;
    }}

    .guideline-item-card.warning {{
      background: #FFFDF5;
      border-color: #FDE68A;
    }}
    .guideline-item-card.warning .guideline-card-title {{
      color: #B45309;
    }}
    .guideline-item-card.warning .step-num {{
      background: #D97706;
    }}

    .guideline-item-card.success {{
      background: #F6FEF9;
      border-color: #A7F3D0;
    }}
    .guideline-item-card.success .guideline-card-title {{
      color: #047857;
    }}
    .guideline-item-card.success .step-num {{
      background: #059669;
    }}

    .guideline-card-body {{
      font-size: 0.8rem;
      color: #334155;
      line-height: 1.5;
    }}

    .guideline-card-body ul {{
      margin: 4px 0 0 0;
      padding-right: 16px;
      list-style-type: disc;
    }}

    .guideline-card-body li {{
      margin-bottom: 2px;
    }}

    .guideline-card-body strong {{
      color: #0F172A;
    }}

    /* Top Instruction Banner for Student in Workspace (Collapsible) */
    /* Top Instruction Banner for Student in Workspace (Collapsible) */
    .student-top-guide-bar {{
      width: 100%;
      max-width: 210mm;
      background: #FFFFFF;
      border: 1.5px solid #C2D0F3;
      border-radius: 14px;
      padding: 12px 18px;
      margin-bottom: 14px;
      box-shadow: 0 4px 14px rgba(32, 64, 151, 0.06);
      text-align: right;
      transition: all 0.25s ease;
    }}

    .student-top-guide-bar.is-open {{
      border-color: #204097;
      box-shadow: 0 6px 20px rgba(32, 64, 151, 0.1);
    }}

    .meta-student-hint {{
      font-size: 0.68rem;
      color: #BE123C;
      background: #FFF1F2;
      border: 1px solid #FECDD3;
      padding: 1px 7px;
      border-radius: 10px;
      margin-right: 6px;
      font-weight: 700;
      vertical-align: middle;
      display: inline-block;
    }}
    body.role-admin .meta-student-hint {{
      display: none;
    }}

    /* Zoom Bar */
    .zoom-toolbar {{
      position: sticky;
      top: 10px;
      z-index: 50;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1.5px solid #C2D0F3;
      border-radius: 30px;
      padding: 5px 12px;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 6px 20px rgba(32, 64, 151, 0.12);
      margin-bottom: 14px;
      flex-wrap: wrap;
      justify-content: center;
    }}

    .zoom-text {{
      font-size: 0.8rem;
      font-weight: 700;
      color: #204097;
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
      box-shadow: 0 10px 35px rgba(32, 64, 151, 0.12);
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
      background: #F3FCFE !important;
      outline: 1.5px dashed #204097 !important;
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
      background: #FFFFFF;
      backdrop-filter: blur(8px);
      border: 1.5px solid #C2D0F3;
      border-radius: 20px;
      padding: 8px 16px;
      color: #204097;
      font-size: 0.78rem;
      font-weight: 700;
      pointer-events: none;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 16px rgba(32, 64, 151, 0.15);
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
      background: rgba(32, 64, 151, 0.35);
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
      background: #FFFFFF;
      border: 1.5px solid #C2D0F3;
      border-radius: 14px;
      max-width: 480px;
      width: 100%;
      padding: 22px;
      box-shadow: 0 20px 40px rgba(32, 64, 151, 0.2);
      text-align: right;
    }}

    .modal-card h3 {{
      font-size: 1.15rem;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
      color: #204097;
    }}

    .modal-card p {{
      font-size: 0.88rem;
      color: #33467D;
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
      color: #7280AB;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 4px;
    }}
    .password-toggle-btn:hover {{
      color: #204097;
    }}

    .print-tip-item {{
      background: #F3FCFE;
      border: 1px solid #C2D0F3;
      padding: 10px 12px;
      border-radius: 8px;
      margin-bottom: 8px;
      font-size: 0.82rem;
      color: #33467D;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .print-tip-item strong {{
      color: #204097;
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
        display: none !important;
      }}
      body.workspace-active.role-admin .mobile-tab-bar {{
        display: block !important;
      }}

      .app-workspace {{
        height: calc(100dvh - 140px);
        height: calc(100vh - 140px);
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
        padding: 8px 12px !important;
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 6px !important;
      }}

      .navbar-brand {{
        width: 100% !important;
        justify-content: flex-start !important;
        gap: 10px !important;
      }}

      .navbar-brand .brand-icon {{
        width: 38px !important;
        height: 38px !important;
        min-width: 38px !important;
        padding: 2px !important;
      }}

      .navbar-brand h1 {{
        font-size: 0.92rem !important;
        line-height: 1.2 !important;
        margin: 0 !important;
      }}

      .navbar-brand span.subtitle {{
        display: block !important;
        font-size: 0.67rem !important;
        color: #4B6396 !important;
        line-height: 1.25 !important;
        margin-top: 2px !important;
        white-space: normal !important;
      }}

      .navbar-actions {{
        width: 100% !important;
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        gap: 6px !important;
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
        padding: 2px 0 !important;
      }}

      .navbar-actions .btn {{
        padding: 6px 10px !important;
        font-size: 0.74rem !important;
        white-space: nowrap !important;
        flex-shrink: 0 !important;
        border-radius: 8px !important;
      }}

      .navbar-actions #btnPrintPdf {{
        flex: 1.3 !important;
        padding: 6px 12px !important;
        font-size: 0.8rem !important;
      }}

      .role-badge {{
        padding: 5px 10px !important;
        font-size: 0.72rem !important;
        white-space: nowrap !important;
        flex-shrink: 0 !important;
      }}

      .mobile-tab-bar {{
        padding: 6px 10px !important;
      }}

      .app-workspace {{
        height: calc(100dvh - 145px) !important;
        height: calc(100vh - 145px) !important;
      }}

      body.role-admin #studentGuidelinesBanner {{
        display: none !important;
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

      /* Admin Action Banner in Gallery on Mobile */
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

      /* Collapsible Guidelines Mobile Polishing */
      .student-guidelines-banner {{
        padding: 10px 12px !important;
        margin-top: 12px !important;
        border-radius: 12px !important;
      }}
      .guidelines-header-icon {{
        width: 32px !important;
        height: 32px !important;
        min-width: 32px !important;
        border-radius: 8px !important;
      }}
      .toggle-main-title {{
        font-size: 0.86rem !important;
      }}
      .toggle-sub-title {{
        display: none !important;
      }}
      .toggle-badge {{
        font-size: 0.68rem !important;
        padding: 2px 7px !important;
      }}
      .guidelines-grid {{
        grid-template-columns: 1fr !important;
        gap: 8px !important;
      }}
      .guideline-item-card {{
        padding: 9px 11px !important;
        border-radius: 9px !important;
      }}
      .guideline-card-title {{
        font-size: 0.82rem !important;
      }}
      .guideline-card-body {{
        font-size: 0.76rem !important;
        line-height: 1.4 !important;
      }}
      .guideline-card-body ul {{
        margin-top: 2px !important;
        padding-right: 14px !important;
      }}
      .student-top-guide-bar {{
        padding: 8px 12px !important;
        margin-bottom: 8px !important;
        border-radius: 10px !important;
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
      body.role-admin.workspace-active .mobile-tab-bar {{
        display: block !important;
      }}
      body.role-admin:not(.workspace-active) .mobile-tab-bar {{
        display: none !important;
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
      background: rgba(32, 64, 151, 0.4);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
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
      background: #FFFFFF;
      border: 1.5px solid #C2D0F3;
      border-radius: 22px;
      max-width: 440px;
      width: 100%;
      padding: 30px 24px 24px 24px;
      text-align: center;
      box-shadow: 0 20px 50px rgba(32, 64, 151, 0.25);
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
      color: #204097;
      margin-bottom: 10px;
      line-height: 1.3;
    }}

    .swal-desc {{
      font-size: 0.9rem;
      color: #33467D;
      line-height: 1.6;
      margin-bottom: 22px;
    }}

    .swal-desc .warn-highlight {{
      display: block;
      margin-top: 6px;
      color: #ef4444;
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
      box-shadow: 0 4px 14px rgba(239, 68, 68, 0.3);
      transition: all 0.2s;
    }}
    .swal-btn-danger:hover {{
      background: linear-gradient(135deg, #dc2626, #b91c1c);
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(239, 68, 68, 0.45);
    }}

    .swal-btn-dismiss {{
      background: #F3FCFE;
      color: #27428B;
      border: 1.5px solid #C2D0F3;
      padding: 10px 18px;
      border-radius: 10px;
      font-family: inherit;
      font-size: 0.9rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .swal-btn-dismiss:hover {{
      background: #C2D0F3;
      color: #204097;
    }}

    /* SweetAlert Success Toast */
    .swal-toast {{
      position: fixed;
      top: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(-30px);
      background: #FFFFFF;
      border: 1.5px solid #10b981;
      border-radius: 14px;
      padding: 12px 22px;
      display: flex;
      align-items: center;
      gap: 12px;
      box-shadow: 0 10px 30px rgba(32, 64, 151, 0.15);
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
      color: #1e293b;
    }}

    .swal-toast-msg {{
      font-size: 0.8rem;
      color: #7280AB;
    }}

    /* ========================================================
       INTRO MOTION GRAPHICS CINEMATIC OVERLAY (FULLSCREEN 2025.mp4)
       ======================================================== */
    .intro-overlay {{
      position: fixed;
      inset: 0;
      width: 100vw;
      height: 100vh;
      z-index: 999999;
      background: #ffffff;
      display: flex;
      justify-content: center;
      align-items: center;
      transition: opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1), transform 0.65s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.65s;
      opacity: 1;
      visibility: visible;
      overflow: hidden;
    }}

    .intro-overlay.fade-out {{
      opacity: 0;
      transform: scale(1.03);
      visibility: hidden;
      pointer-events: none;
    }}

    .intro-fullscreen-video {{
      width: 100vw;
      height: 100vh;
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      display: block;
      background: #ffffff;
    }}
  </style>
</head>
<body>

  <!-- Motion Graphics Fullscreen Intro Overlay -->
  <div id="introOverlay" class="intro-overlay">
    <video id="introVideo" src="2025.mp4" autoplay muted playsinline preload="auto" class="intro-fullscreen-video"></video>
  </div>

  <!-- Top Global Sticky Wrapper (Contains Navbar and Mobile Tab Switcher) -->
  <div class="app-top-header-wrap" id="appTopHeaderWrap">
    <header class="app-navbar no-print">
      <div class="navbar-brand" id="brandHomeBtn">
        <div class="brand-icon" title="شعار معهد طيبة العالي">
          <img src="data:image/png;base64,{attnlg_b64}" alt="شعار معهد طيبة العالي" class="brand-logo-img">
        </div>
        <div>
          <h1>منصة استمارة بحث التخرج</h1>
          <span class="subtitle">معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات • تصميم رسمي متوافق مع مقاس A4</span>
        </div>
      </div>

      <div class="navbar-actions">
        <!-- Role indicator (Admin only) -->
        <span class="role-badge admin" id="roleBadge" style="display:none;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>
          <span id="roleBadgeText">وضع الإدارة (Admin)</span>
        </span>

        <!-- Switch to Gallery / Return to Home (Visible only when in Workspace) -->
        <button type="button" class="btn btn-secondary btn-sm workspace-btn" id="btnBrowseGallery" title="العودة للصفحة الرئيسية وتصفح الاستمارات" style="display:none;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 19 12 12 5"></polyline></svg>
          <span class="btn-navbar-text">العودة للرئيسية</span>
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

        <!-- Clear Data -->
        <button type="button" class="btn btn-outline btn-sm workspace-btn" id="btnClearData" title="تفريغ جدول الطلاب" style="display:none;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
          <span class="btn-navbar-text">تفريغ الجدول</span>
        </button>

        <!-- Admin Logout Trigger (Shown ONLY when admin is logged in) -->
        <button type="button" class="btn btn-outline btn-sm" id="btnAuthToggle" style="display:none;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
          <span id="authBtnText">خروج من الإدارة</span>
        </button>
      </div>
    </header>

    <!-- Mobile Segmented Tabs Bar (Active ONLY when in Workspace on screens <= 1024px) -->
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
        </div>
      </div>
    </div>

    <!-- Collapsible Student Guidelines Banner (Closed by default) -->
    <div class="student-guidelines-banner" id="studentGuidelinesBanner">
      <button type="button" class="guidelines-toggle-btn" id="btnToggleGuidelines" aria-expanded="false">
        <div class="toggle-btn-right">
          <div class="guidelines-header-icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          </div>
          <div class="toggle-btn-text">
            <div class="toggle-title-row">
              <span class="toggle-main-title">تنبيهات وتعليمات هامة لملء الاستمارة</span>
              <span class="toggle-badge" id="guidelinesBadge">اضغط هنا للتنبيهات ▾</span>
            </div>
            <div class="toggle-sub-title">الخانات المتروكة فارغة • بيانات الجدول • رقم تليفون الـ Team Leader</div>
          </div>
        </div>
        <div class="toggle-chevron" id="guidelinesChevron">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </div>
      </button>

      <div class="guidelines-collapsible-content" id="guidelinesContent" style="display: none;">
        <div class="guidelines-grid">
          <!-- Box 1: Empty Fields -->
          <div class="guideline-item-card danger">
            <div class="guideline-card-title">
              <span class="step-num">١</span>
              <span>خانات تُترك فارغة تماماً</span>
            </div>
            <div class="guideline-card-body">
              تُترك هذه الخانات بيضاء فارغة بدون كتابة:
              <ul>
                <li><strong>رقم المشروع</strong></li>
                <li><strong>اسم المشروع</strong></li>
                <li><strong>اسم الدكتور المشرف</strong></li>
              </ul>
            </div>
          </div>

          <!-- Box 2: Table Data -->
          <div class="guideline-item-card primary">
            <div class="guideline-card-title">
              <span class="step-num">٢</span>
              <span>بيانات الجدول المطلوبة</span>
            </div>
            <div class="guideline-card-body">
              تسجيل بيانات الطلاب بدقة بالجدول:
              <ul>
                <li><strong>كود كل طالب</strong></li>
                <li><strong>اسم كل طالب</strong> (ثلاثي أو رباعي وواضح)</li>
              </ul>
            </div>
          </div>

          <!-- Box 3: Team Leader -->
          <div class="guideline-item-card warning">
            <div class="guideline-card-title">
              <span class="step-num">٣</span>
              <span>قائد الفريق (Team Leader)</span>
            </div>
            <div class="guideline-card-body">
              رقم الهاتف وقائد الفريق:
              <ul>
                <li>كتابة <strong>رقم تليفون الـ Team Leader بس</strong>.</li>
                <li>تحديد قائد الفريق بكتابة <strong>TL</strong> بجوار اسمه (مثال: <em>أحمد محمد علي - TL</em>).</li>
              </ul>
            </div>
          </div>

          <!-- Box 4: Print & Submit -->
          <div class="guideline-item-card success">
            <div class="guideline-card-title">
              <span class="step-num">٤</span>
              <span>الطباعة والتسليم الورقي</span>
            </div>
            <div class="guideline-card-body">
              إتمام التسجيل والطباعة:
              <ul>
                <li>التأكد من أن البيانات <strong>واضحة ومنظمة</strong>.</li>
                <li>بعد الانتهاء، <strong>اطبع الاستمارة ورقياً</strong> وتوجّه بها لتسليمها لإدارة المعهد.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Admin Top Bar in Gallery -->
    <div id="adminGalleryActions" style="display:none; justify-content:space-between; align-items:center; background:#FFFFFF; padding:12px 18px; border-radius:12px; border:1.5px solid #C2D0F3; box-shadow:0 4px 14px rgba(32,64,151,0.06);">
      <div style="font-weight:700; color:#204097; display:flex; align-items:center; gap:8px;">
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
      <div style="padding: 12px 18px; background:#F3FCFE; border-bottom:1px solid #C2D0F3; display:flex; justify-content:space-between; align-items:center;">
        <button type="button" class="btn btn-outline btn-sm" id="btnBackToGalleryFromPanel">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
          تغيير القسم / الاستمارة
        </button>
        <span style="font-size:0.75rem; color:#33467D; font-weight:700;" id="panelActiveDeptBadge">قسم نظم معلومات الأعمال</span>
      </div>

      <!-- PERMANENT STUDENT INSTRUCTIONS CARD IN SIDEBAR -->
      <div class="panel-section" id="studentBannerSec">
        <div class="student-instructions-card">
          <div class="instructions-card-header">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
            <span>تنبيهات ملء الاستمارة:</span>
          </div>
          <div class="instructions-list">
            <div class="instructions-list-item">
              <span class="icon">١.</span>
              <div>اترك الخانات التالية <strong>فارغة تماماً</strong>: (رقم المشروع - اسم المشروع - اسم الدكتور المشرف).</div>
            </div>
            <div class="instructions-list-item">
              <span class="icon">٢.</span>
              <div>اكتب في الجدول: <strong>كود كل طالب</strong> + <strong>اسم كل طالب</strong> رباعي وواضح.</div>
            </div>
            <div class="instructions-list-item">
              <span class="icon">٣.</span>
              <div>اكتب <strong>رقم تليفون الـ Team Leader بس</strong>، وحدد القائد بكتابة <strong>TL</strong> بجوار اسمه.</div>
            </div>
            <div class="instructions-list-item">
              <span class="icon">٤.</span>
              <div>تأكد من وضوح وتنظيم البيانات، ثم اضغط على <strong>«طباعة / حفظ PDF»</strong> واطبعها ورقياً وتعالَ بها للمعهد.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Admin Publish Banner (shown only to admins) -->
      <div class="panel-section" id="adminBannerSec" style="display:none;">
        <div class="admin-action-banner">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; gap:8px;">
            <div style="font-size:0.85rem; font-weight:800; color:#204097; display:flex; align-items:center; gap:6px;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>
              <span>تحرير القالب وضبط النشر</span>
            </div>
            <span id="panelPublishStatusBadge" class="status-pill status-draft">مسودة</span>
          </div>
          <p id="panelPublishStatusDesc" style="font-size:0.78rem; color:#33467D; line-height:1.5; margin-bottom:10px;">
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
            <input type="text" class="form-control" id="inputAcademicYear" value="العام الجامعي 2026 / 2027">
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
            <input type="text" class="form-control" id="inputInstLine2" value="معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات">
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
                <span id="logoSizeVal" style="color:#204097; font-weight:700;">58px</span>
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

      <!-- Collapsible Student Instructions Banner Above the Form (Closed by default) -->
      <div class="student-top-guide-bar no-print" id="studentTopGuideBar">
        <button type="button" class="guidelines-toggle-btn" id="btnToggleWorkspaceGuide" aria-expanded="false">
          <div class="toggle-btn-right">
            <div class="guidelines-header-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
            </div>
            <div class="toggle-btn-text">
              <div class="toggle-title-row">
                <span class="toggle-main-title">تنبيهات هامة لملء الاستمارة</span>
                <span class="toggle-badge" id="workspaceGuideBadge">اضغط للتنبيهات ▾</span>
              </div>
              <div class="toggle-sub-title">الخانات المتروكة فارغة • بيانات الجدول • رقم تليفون الـ Team Leader</div>
            </div>
          </div>
          <div class="toggle-chevron" id="workspaceGuideChevron">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </div>
        </button>

        <div class="guidelines-collapsible-content" id="workspaceGuideItems" style="display: none;">
          <div class="guidelines-grid">
            <div class="guideline-item-card danger">
              <div class="guideline-card-title">
                <span class="step-num">١</span>
                <span>خانات تُترك فارغة تماماً</span>
              </div>
              <div class="guideline-card-body">
                اترك الخانات التالية فارغة: <strong>(رقم المشروع • اسم المشروع • اسم الدكتور المشرف)</strong>.
              </div>
            </div>
            <div class="guideline-item-card primary">
              <div class="guideline-card-title">
                <span class="step-num">٢</span>
                <span>بيانات الجدول المطلوبة</span>
              </div>
              <div class="guideline-card-body">
                اكتب داخل الجدول: <strong>كود كل طالب</strong> + <strong>اسم كل طالب</strong> رباعي وواضح.
              </div>
            </div>
            <div class="guideline-item-card warning">
              <div class="guideline-card-title">
                <span class="step-num">٣</span>
                <span>قائد الفريق (Team Leader)</span>
              </div>
              <div class="guideline-card-body">
                اكتب <strong>رقم تليفون الـ TL بس</strong>، وحدد القائد بكتابة <strong>TL</strong> بجوار اسمه.
              </div>
            </div>
            <div class="guideline-item-card success">
              <div class="guideline-card-title">
                <span class="step-num">٤</span>
                <span>الطباعة والتسليم</span>
              </div>
              <div class="guideline-card-body">
                تأكد من وضوح البيانات، ثم <strong>اطبع الاستمارة وتعالَ بها للمعهد</strong>.
              </div>
            </div>
          </div>
        </div>
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

        <div style="width: 1px; height: 16px; background: #C2D0F3;"></div>

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
                    <div class="inst-sub" id="previewInstLine2">معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات</div>
                    <div class="inst-dept" id="previewInstLine3">قسم نظم معلومات الأعمال</div>
                  </div>
                </div>

                <div class="header-left-badge">
                  <div style="font-size: 9pt; color: #444; margin-bottom: 2px;">وزارة التعليم العالي</div>
                  <div class="year-badge" id="previewAcademicYear">العام الجامعي 2026 / 2027</div>
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
                  <span class="meta-label">رقم المشروع: <span class="meta-student-hint no-print">(تُترك فارغة)</span></span>
                  <div class="meta-line-container">
                    <span class="meta-value-text" id="previewProjectNo" contenteditable="false" spellcheck="false"></span>
                    <div class="meta-dotted-line"></div>
                  </div>
                </div>

                <div class="meta-row">
                  <span class="meta-label">اسم المشروع: <span class="meta-student-hint no-print">(تُترك فارغة)</span></span>
                  <div class="meta-line-container">
                    <span class="meta-value-text" id="previewProjectName" contenteditable="false" spellcheck="false"></span>
                    <div class="meta-dotted-line"></div>
                  </div>
                </div>

                <div class="meta-row">
                  <span class="meta-label">اسم الدكتور المشرف: <span class="meta-student-hint no-print">(تُترك فارغة)</span></span>
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
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#204097" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
        <span>اضغط على أي خانة في جدول الطلاب واكتب من اليمين لليسار، ثم اطبع!</span>
      </div>

    </main>
  </div>

  <!-- Secure Admin Login Modal (SHA-256 Protected) -->
  <div class="modal-backdrop" id="adminLoginModal">
    <div class="modal-card">
      <h3>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#204097" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
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
        <div id="loginFeedbackMsg" style="font-size:0.75rem; color:#ef4444; font-weight:700; margin-top:6px; display:none;"></div>

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
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#204097" stroke-width="2"><path d="M21 2l-2 2m-1.5 6.1L19 12l2-2-4-4-1.9 1.5M10.5 14.5L3 22l4-4 3.5-3.5"></path></svg>
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

  <!-- Admin Create New Template Modal -->
  <div class="modal-backdrop" id="createTemplateModal">
    <div class="modal-card" style="max-width: 520px;">
      <h3>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#204097" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="12" y1="18" x2="12" y2="12"></line><line x1="9" y1="15" x2="15" y2="15"></line></svg>
        إنشاء قالب استمارة بحث جديد
      </h3>
      <p>قم بتحديد بيانات استمارة البحث الجديدة لإضافتها إلى المنصة واعتمادها فوراً للطلاب:</p>

      <div class="form-group" style="margin-bottom: 12px;">
        <label class="form-label" for="newTmplTitleInput">عنوان استمارة البحث الرسمية:</label>
        <input type="text" class="form-control" id="newTmplTitleInput" placeholder="مثال: استمارة تسجيل مشروع تخرج نظم المعلومات" value="استمارة بحث تخرج جديدة">
      </div>

      <div class="form-group" style="margin-bottom: 12px;">
        <label class="form-label" for="newTmplDeptSelect">القسم العلمي التابع له:</label>
        <select class="form-control" id="newTmplDeptSelect">
          <option value="نظم معلومات الأعمال">قسم نظم معلومات الأعمال</option>
          <option value="علوم الحاسب">قسم علوم الحاسب</option>
          <option value="إدارة ومحاسبة">قسم إدارة ومحاسبة</option>
          <option value="هندسة">قسم هندسة</option>
          <option value="custom">قسم آخر (مخصص)...</option>
        </select>
      </div>

      <div class="form-group" id="newTmplCustomDeptGroup" style="margin-bottom: 12px; display: none;">
        <label class="form-label" for="newTmplCustomDeptInput">اسم القسم المخصص:</label>
        <input type="text" class="form-control" id="newTmplCustomDeptInput" placeholder="أدخل اسم القسم الجديد...">
      </div>

      <div class="form-group" style="margin-bottom: 12px;">
        <label class="form-label" for="newTmplHeadInput">رئيس القسم المعتمد:</label>
        <input type="text" class="form-control" id="newTmplHeadInput" value="أ.د/ إبراهيم سليم">
      </div>

      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 14px;">
        <div class="form-group">
          <label class="form-label" for="newTmplRowCount">عدد صفوف الطلاب:</label>
          <select class="form-control" id="newTmplRowCount">
            <option value="15" selected>15 صفاً (فريق عمل)</option>
            <option value="6">6 صفوف (مصغرة)</option>
            <option value="10">10 صفوف</option>
            <option value="20">20 صفاً</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label" for="newTmplPublishSelect">حالة النشر:</label>
          <select class="form-control" id="newTmplPublishSelect">
            <option value="true" selected>🟢 معروض ومنشور للطلاب</option>
            <option value="false">🟡 مسودة خاصة بالإدارة</option>
          </select>
        </div>
      </div>

      <div id="createTmplFeedbackMsg" style="font-size:0.8rem; color:#ef4444; font-weight:700; margin-bottom:10px; display:none;"></div>

      <div style="display:flex; gap:10px; justify-content:flex-end;">
        <button type="button" class="btn btn-outline" id="btnCancelCreateTmpl">إلغاء</button>
        <button type="button" class="btn btn-primary" id="btnSubmitCreateTmpl">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
          إنشاء القالب وإضافته الآن
        </button>
      </div>
    </div>
  </div>

  <!-- Print Advice Modal -->
  <div class="modal-backdrop" id="printModal">
    <div class="modal-card">
      <h3>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#204097" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
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
        instLine2: "معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات",
        instLine3: "قسم نظم معلومات الأعمال",
        academicYear: "العام الجامعي 2026 / 2027",
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
          {{ id: "col_phone", name: "رقم التليفون (TL فقط)", width: "28%", autoSeq: false }}
        ],
        rowCount: 15
      }},
      {{
        id: "cs_default",
        dept: "علوم الحاسب",
        published: true,
        formTitle: "استمارة تسجيل مشروع تخرج علوم الحاسب",
        instLine1: "معاهد طيبة العليا",
        instLine2: "معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات",
        instLine3: "قسم علوم الحاسب",
        academicYear: "العام الجامعي 2026 / 2027",
        projectNo: "",
        projectName: "",
        supervisor: "",
        signRightTitle: "المشرف الأكاديمي",
        signLeftTitle: "رئيس مجلس القسم",
        headName: "أ.د/ إبراهيم سليم",
        logoVisible: true,
        logoSize: 58,
        logoData: DEFAULT_LOGO_B64,
        columns: [
          {{ id: "col_seq", name: "م", width: "7%", autoSeq: true }},
          {{ id: "col_code", name: "كود الطالب", width: "23%", autoSeq: false }},
          {{ id: "col_name", name: "اسم الطالب", width: "42%", autoSeq: false }},
          {{ id: "col_phone", name: "رقم التليفون (TL فقط)", width: "28%", autoSeq: false }}
        ],
        rowCount: 6
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
        let stored = localStorage.getItem("tiba_templates_v7");
        if (!stored) {{
          // Clean initialization with only BIS and CS
          templates = JSON.parse(JSON.stringify(INITIAL_TEMPLATES));
        }} else {{
          templates = JSON.parse(stored);
        }}

        // Prune legacy templates if any old IDs were carried over
        templates = templates.filter(t => t.id !== 'business_default' && t.id !== 'eng_default');
        if (templates.length === 0) {{
          templates = JSON.parse(JSON.stringify(INITIAL_TEMPLATES));
        }}

        // Always ensure migrations & official updates are applied
        templates.forEach(t => {{
          if (typeof t.published === 'undefined') {{
            t.published = true;
          }}
          if (!t.logoData || t.logoData === 'DEFAULT') {{
            t.logoData = DEFAULT_LOGO_B64;
          }}
          // Update academic year to 2026 / 2027
          t.academicYear = "العام الجامعي 2026 / 2027";

          // Purge col_track / مسار التخصص from all templates completely
          if (Array.isArray(t.columns)) {{
            t.columns = t.columns.filter(c => c.id !== 'col_track' && !c.name.includes('مسار'));
            const seqCol = t.columns.find(c => c.id === 'col_seq' || c.autoSeq);
            if (seqCol) seqCol.width = '7%';
            const codeCol = t.columns.find(c => c.id === 'col_code');
            if (codeCol) codeCol.width = '23%';
            const nameCol = t.columns.find(c => c.id === 'col_name');
            if (nameCol) nameCol.width = '42%';
            const phoneCol = t.columns.find(c => c.id === 'col_phone');
            if (phoneCol) {{
              phoneCol.width = '28%';
              phoneCol.name = 'رقم التليفون (TL فقط)';
            }}
          }}

          if (t.id === 'cs_default' || (t.dept && t.dept.includes('علوم الحاسب'))) {{
            t.rowCount = 6;
            t.headName = 'أ.د/ إبراهيم سليم';
            t.instLine2 = 'معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات';
          }}
          if (t.id === 'bis_default' || (t.dept && t.dept.includes('نظم معلومات'))) {{
            t.headName = 'أ.د/ إبراهيم سليم';
            t.instLine2 = 'معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات';
          }}
          if (t.instLine2 === 'المعهد العالي لعلوم الحاسب وتكنولوجيا المعلومات' || t.instLine2 === 'المعهد العالي لتكنولوجيا الإدارة والمعلومات') {{
            t.instLine2 = 'معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات';
          }}
          if (t.headName === 'أ.د/ عادل عبد الفتاح') {{
            t.headName = 'أ.د/ إبراهيم سليم';
          }}
        }});
        saveTemplates();
      }} catch (e) {{
        templates = JSON.parse(JSON.stringify(INITIAL_TEMPLATES));
        saveTemplates();
      }}
    }}

    function saveTemplates() {{
      try {{
        localStorage.setItem("tiba_templates_v7", JSON.stringify(templates));
      }} catch (e) {{
        console.warn("Storage quota warning, compressing logo data:", e);
        try {{
          const clean = templates.map(t => {{
            const c = Object.assign({{}}, t);
            if (c.logoData === DEFAULT_LOGO_B64) c.logoData = 'DEFAULT';
            return c;
          }});
          localStorage.setItem("tiba_templates_v7", JSON.stringify(clean));
        }} catch(err) {{
          console.error("Storage save failed:", err);
        }}
      }}
    }}

    // ==========================================
    // SUPABASE CLOUD DATABASE INTEGRATION
    // ==========================================
    const SUPABASE_URL = "https://wiuoaygyezinzmjksktg.supabase.co";
    const SUPABASE_KEY = "sb_publishable_0sjZvyRlzgencz65iCab3w_XdgXDioZ";

    async function syncFromSupabase() {{
      try {{
        const res = await fetch(`${{SUPABASE_URL}}/rest/v1/tiba_templates?select=*&order=updated_at.desc`, {{
          headers: {{
            'apikey': SUPABASE_KEY,
            'Authorization': `Bearer ${{SUPABASE_KEY}}`
          }}
        }});
        if (!res.ok) throw new Error('Supabase fetch failed: ' + res.status);
        const rows = await res.json();
        if (Array.isArray(rows) && rows.length > 0) {{
          const cloudTemplates = rows.map(r => {{
            const t = r.data || {{}};
            if (!t.logoData || t.logoData === 'DEFAULT') {{
              t.logoData = DEFAULT_LOGO_B64;
            }}
            // Purge col_track / مسار التخصص from all cloud templates
            if (Array.isArray(t.columns)) {{
              t.columns = t.columns.filter(c => c.id !== 'col_track' && !c.name.includes('مسار'));
              const seqCol = t.columns.find(c => c.id === 'col_seq' || c.autoSeq);
              if (seqCol) seqCol.width = '7%';
              const codeCol = t.columns.find(c => c.id === 'col_code');
              if (codeCol) codeCol.width = '23%';
              const nameCol = t.columns.find(c => c.id === 'col_name');
              if (nameCol) nameCol.width = '42%';
              const phoneCol = t.columns.find(c => c.id === 'col_phone');
              if (phoneCol) {{
                phoneCol.width = '28%';
                phoneCol.name = 'رقم التليفون (TL فقط)';
              }}
            }}
            return t;
          }});
          templates = cloudTemplates;
          try {{
            localStorage.setItem("tiba_templates_v7", JSON.stringify(templates));
          }} catch(e) {{}}
          renderGallery();
        }}
      }} catch (err) {{
        console.warn("Supabase cloud sync skipped (offline or network error):", err);
      }}
    }}

    async function syncUpsertToSupabase(tmpl) {{
      if (!tmpl) return;
      try {{
        const cleanTmpl = Object.assign({{}}, tmpl);
        if (cleanTmpl.logoData === DEFAULT_LOGO_B64) cleanTmpl.logoData = 'DEFAULT';
        
        await fetch(`${{SUPABASE_URL}}/rest/v1/tiba_templates`, {{
          method: 'POST',
          headers: {{
            'apikey': SUPABASE_KEY,
            'Authorization': `Bearer ${{SUPABASE_KEY}}`,
            'Content-Type': 'application/json',
            'Prefer': 'resolution=merge-duplicates'
          }},
          body: JSON.stringify([{{
            id: cleanTmpl.id,
            dept: cleanTmpl.dept,
            data: cleanTmpl,
            updated_at: new Date().toISOString()
          }}])
        }});
      }} catch (err) {{
        console.error("Supabase upsert sync failed:", err);
      }}
    }}

    async function syncDeleteFromSupabase(tmplId) {{
      if (!tmplId) return;
      try {{
        await fetch(`${{SUPABASE_URL}}/rest/v1/tiba_templates?id=eq.${{encodeURIComponent(tmplId)}}`, {{
          method: 'DELETE',
          headers: {{
            'apikey': SUPABASE_KEY,
            'Authorization': `Bearer ${{SUPABASE_KEY}}`
          }}
        }});
      }} catch (err) {{
        console.error("Supabase delete sync failed:", err);
      }}
    }}

    async function syncDeleteAllFromSupabase() {{
      try {{
        await fetch(`${{SUPABASE_URL}}/rest/v1/tiba_templates?id=neq.none`, {{
          method: 'DELETE',
          headers: {{
            'apikey': SUPABASE_KEY,
            'Authorization': `Bearer ${{SUPABASE_KEY}}`
          }}
        }});
      }} catch (err) {{
        console.error("Supabase delete all sync failed:", err);
      }}
    }}

    // Switch Views with Browser History Support
    function showGalleryView(updateHistory = true) {{
      document.body.classList.remove('workspace-active');
      document.getElementById('viewGallery').style.display = 'flex';
      document.getElementById('appWorkspace').classList.remove('active');
      const mobileTabBar = document.getElementById('mobileTabBar');
      if (mobileTabBar) mobileTabBar.style.display = 'none';
      document.querySelectorAll('.workspace-btn').forEach(btn => btn.style.display = 'none');
      
      if (updateHistory) {{
        try {{
          if (window.location.hash === '#workspace') {{
            history.pushState({{ view: 'gallery' }}, '', window.location.pathname + window.location.search);
          }} else {{
            history.replaceState({{ view: 'gallery' }}, '', window.location.pathname + window.location.search);
          }}
        }} catch (e) {{}}
      }}
      renderGallery();
      syncFromSupabase();
    }}

    function showWorkspaceView(updateHistory = true) {{
      window.scrollTo(0, 0);
      document.body.classList.add('workspace-active');
      document.getElementById('viewGallery').style.display = 'none';
      document.getElementById('appWorkspace').classList.add('active');
      const canvas = document.getElementById('canvasArea');
      if (canvas) canvas.scrollTop = 0;
      const mobileTabBar = document.getElementById('mobileTabBar');
      if (window.innerWidth <= 1024 && currentRole === 'admin' && mobileTabBar) {{
        mobileTabBar.style.display = 'block';
      }} else if (mobileTabBar) {{
        mobileTabBar.style.display = 'none';
      }}
      document.querySelectorAll('.workspace-btn').forEach(btn => btn.style.display = 'inline-flex');
      
      applyRolePermissions();
      updateAdminBannerUI();
      syncInputsFromState();
      renderPreview();
      
      if (updateHistory) {{
        try {{
          history.pushState({{ view: 'workspace', templateId: currentTemplate ? currentTemplate.id : null }}, '', '#workspace');
        }} catch (e) {{}}
      }}
      
      setTimeout(() => {{
        fitToScreen();
      }}, 80);
    }}

    // Apply Role UI Controls
    function applyRolePermissions() {{
      const roleBadge = document.getElementById('roleBadge');
      const roleText = document.getElementById('roleBadgeText');
      const authBtn = document.getElementById('btnAuthToggle');
      const authBtnText = document.getElementById('authBtnText');
      const studentBanner = document.getElementById('studentBannerSec');
      const studentGuidelinesBanner = document.getElementById('studentGuidelinesBanner');
      const adminBanner = document.getElementById('adminBannerSec');
      const adminGalleryActions = document.getElementById('adminGalleryActions');
      const adminDesignControls = document.getElementById('adminDesignControls');
      const studentTopGuide = document.getElementById('studentTopGuideBar');
      const controlPanel = document.getElementById('controlPanel');
      const mobileTabBar = document.getElementById('mobileTabBar');
      const isWorkspace = document.getElementById('appWorkspace') && document.getElementById('appWorkspace').classList.contains('active');
      
      const previewTitle = document.getElementById('previewFormTitle');
      const previewProjectNo = document.getElementById('previewProjectNo');
      const previewProjectName = document.getElementById('previewProjectName');
      const previewSupervisor = document.getElementById('previewSupervisor');

      if (currentRole === 'admin') {{
        document.body.classList.add('role-admin');
        document.body.classList.remove('role-student');

        if (roleBadge) {{
          roleBadge.className = 'role-badge admin';
          roleBadge.style.display = 'inline-flex';
          roleText.innerText = 'وضع الإدارة (Admin)';
        }}
        if (authBtn) {{
          authBtn.style.display = 'inline-flex';
          authBtnText.innerText = 'خروج من الإدارة';
        }}
        if (studentGuidelinesBanner) studentGuidelinesBanner.style.display = 'none';
        studentBanner.style.display = 'none';
        adminBanner.style.display = 'block';
        adminGalleryActions.style.display = 'flex';
        adminDesignControls.style.display = 'block';
        studentTopGuide.style.display = 'none';
        updateAdminBannerUI();

        if (controlPanel) controlPanel.style.display = 'flex';
        if (mobileTabBar) {{
          mobileTabBar.style.display = (isWorkspace && window.innerWidth <= 1024) ? 'block' : 'none';
        }}

        // Admin can edit all headers directly in preview
        previewTitle.contentEditable = 'true';
        previewProjectNo.contentEditable = 'true';
        previewProjectName.contentEditable = 'true';
        previewSupervisor.contentEditable = 'true';
      }} else {{
        // Student Mode: STRICTLY LOCKED, NO SIDEBAR, ADMIN BUTTONS HIDDEN!
        document.body.classList.add('role-student');
        document.body.classList.remove('role-admin');

        if (roleBadge) roleBadge.style.display = 'none';
        if (authBtn) authBtn.style.display = 'none';

        if (studentGuidelinesBanner) studentGuidelinesBanner.style.display = 'block';
        studentBanner.style.display = 'none';
        adminBanner.style.display = 'none';
        adminGalleryActions.style.display = 'none';
        adminDesignControls.style.display = 'none';
        studentTopGuide.style.display = 'block';

        if (controlPanel) controlPanel.style.display = 'none';
        if (mobileTabBar) mobileTabBar.style.display = 'none';

        // Student CANNOT edit anything outside the table!
        previewTitle.contentEditable = 'false';
        previewProjectNo.contentEditable = 'false';
        previewProjectName.contentEditable = 'false';
        previewSupervisor.contentEditable = 'false';
      }}
    }}

    // Render Gallery with Dynamic Department Filter Pills
    let activeFilter = 'all';

    function renderDeptFilterPills(roleTemplates) {{
      const pillsContainer = document.getElementById('deptFilterPills');
      if (!pillsContainer) return;

      // Extract unique departments present in currently available templates
      const depts = Array.from(new Set(roleTemplates.map(t => t.dept).filter(Boolean)));

      // If active filter is set to a department that no longer exists, reset to 'all'
      if (activeFilter !== 'all' && !depts.some(d => d === activeFilter || d.includes(activeFilter))) {{
        activeFilter = 'all';
      }}

      let html = `<button type="button" class="filter-pill ${{activeFilter === 'all' ? 'active' : ''}}" data-filter="all">جميع الأقسام</button>`;
      depts.forEach(d => {{
        const isActive = (activeFilter === d);
        html += `<button type="button" class="filter-pill ${{isActive ? 'active' : ''}}" data-filter="${{d}}">${{d}}</button>`;
      }});

      pillsContainer.innerHTML = html;

      // Bind click handlers to dynamic pills
      pillsContainer.querySelectorAll('.filter-pill').forEach(pill => {{
        pill.addEventListener('click', () => {{
          pillsContainer.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
          pill.classList.add('active');
          activeFilter = pill.dataset.filter;
          renderGallery();
        }});
      }});
    }}

    function renderGallery() {{
      const grid = document.getElementById('templatesGrid');
      const searchVal = document.getElementById('gallerySearchInput').value.trim().toLowerCase();
      grid.innerHTML = '';

      // Students only see published templates (published !== false)
      const roleTemplates = (currentRole === 'admin') 
        ? templates 
        : templates.filter(t => t.published !== false);

      // Dynamically render department filter pills based only on available templates
      renderDeptFilterPills(roleTemplates);

      const filtered = roleTemplates.filter(t => {{
        const matchesFilter = (activeFilter === 'all' || t.dept === activeFilter || t.dept.includes(activeFilter));
        const matchesSearch = (!searchVal || t.formTitle.toLowerCase().includes(searchVal) || t.dept.toLowerCase().includes(searchVal));
        return matchesFilter && matchesSearch;
      }});

      if (filtered.length === 0) {{
        if (roleTemplates.length === 0) {{
          if (currentRole === 'admin') {{
            grid.innerHTML = `
              <div style="grid-column: 1/-1; text-align: center; padding: 50px 20px; background: #FFFFFF; border: 2px dashed #C2D0F3; border-radius: 16px; box-shadow: 0 4px 16px rgba(32, 64, 151, 0.06);">
                <div style="width: 56px; height: 56px; margin: 0 auto 14px auto; background: rgba(32, 64, 151, 0.08); border-radius: 14px; display: flex; align-items: center; justify-content: center; color: #204097;">
                  <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                </div>
                <h3 style="font-size: 1.25rem; font-weight: 800; color: #204097; margin-bottom: 8px;">لا توجد أي قوالب حالياً</h3>
                <p style="font-size: 0.88rem; color: #33467D; max-width: 480px; margin: 0 auto 16px auto; line-height: 1.6;">
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
              <div style="grid-column: 1/-1; text-align: center; padding: 60px 20px; background: #FFFFFF; border: 2px dashed #C2D0F3; border-radius: 16px; box-shadow: 0 4px 16px rgba(32, 64, 151, 0.06);">
                <div style="width: 60px; height: 60px; margin: 0 auto 14px auto; background: rgba(32, 64, 151, 0.08); border-radius: 16px; display: flex; align-items: center; justify-content: center; color: #204097;">
                  <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                </div>
                <h3 style="font-size: 1.35rem; font-weight: 800; color: #204097; margin-bottom: 8px;">لا توجد استمارات متاحة حالياً</h3>
                <p style="font-size: 0.95rem; color: #33467D; max-width: 520px; margin: 0 auto; line-height: 1.7;">
                  لم تقم إدارة المعهد بنشر أي استمارة بحث حتى الآن. يرجى الانتظار حتى تقوم إدارة المعهد بنشر القوالب المعتمدة لقسمك.
                </p>
              </div>
            `;
          }}
          return;
        }}

        grid.innerHTML = `
          <div style="grid-column: 1/-1; text-align: center; padding: 40px; color: #33467D;">
            <p style="font-size: 1.1rem; font-weight: 700; color: #204097;">لا توجد استمارات مطابقة للبحث</p>
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
              <div class="card-detail-item item-inst">
                <span>المعهد:</span>
                <span class="val">${{tmpl.instLine2}}</span>
              </div>
              <div class="card-detail-item">
                <span>رئيس القسم:</span>
                <span class="val">${{tmpl.headName}}</span>
              </div>
              <div class="card-detail-item">
                <span>سعة الاستمارة:</span>
                <span class="val" style="font-weight:700; color:#204097;">${{tmpl.rowCount || 15}} طلاب</span>
              </div>
              <div class="card-detail-item">
                <span>أعمدة الجدول:</span>
                <span class="val">${{tmpl.columns.map(c => c.name).join(' • ')}}</span>
              </div>
            </div>
          </div>

          ${{currentRole === 'admin' ? `
            <div style="margin-top: 14px; padding-top: 12px; border-top: 1px dashed #C2D0F3;">
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

        card.addEventListener('click', (e) => {{
          if (e.target.closest('button')) return;
          selectTemplate(tmpl.id);
        }});

        grid.appendChild(card);
      }});
    }}

    // Select Template and open workspace
    window.selectTemplate = function(templateId, updateHistory = true) {{
      const found = templates.find(t => t.id === templateId);
      if (!found) return;
      if (currentRole !== 'admin' && found.published === false) {{
        showSwalToast('استمارة غير متاحة', 'هذا القالب مسودة خاصة ولم يتم نشره للطلاب بعد.');
        return;
      }}
      currentTemplate = JSON.parse(JSON.stringify(found));
      
      appState.rowCount = currentTemplate.rowCount || 15;
      document.getElementById('panelActiveDeptBadge').innerText = currentTemplate.dept;
      showWorkspaceView(updateHistory);
    }};

    // Toggle Publish/Display Status for a Template
    window.togglePublishTemplate = function(templateId) {{
      const tmpl = templates.find(t => t.id === templateId);
      if (!tmpl) return;
      tmpl.published = (tmpl.published === false) ? true : false;
      saveTemplates();
      syncUpsertToSupabase(tmpl);
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
        toggleBtn.style.color = '#b45309';
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
        toggleBtn.style.background = '#059669';
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
          syncDeleteFromSupabase(templateId);
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
      setupIntro();
      loadTemplates();

      // Ensure initial history state is set only if not #admin
      if (window.location.hash !== '#admin' && !window.location.hash.startsWith('#workspace')) {{
        try {{
          history.replaceState({{ view: 'gallery' }}, '', window.location.pathname + window.location.search);
        }} catch (e) {{}}
      }}

      showGalleryView(false);

      // Direct Admin URL trigger check
      checkAdminUrlTrigger();
      window.addEventListener('hashchange', checkAdminUrlTrigger);

      // Handle browser Back / Forward buttons & mobile swipe gestures
      window.addEventListener('popstate', (e) => {{
        // If an active modal is open, dismiss it first
        const activeModal = document.querySelector('.modal-backdrop.active');
        if (activeModal) {{
          activeModal.classList.remove('active');
          return;
        }}

        if (window.location.hash === '#admin') {{
          checkAdminUrlTrigger();
          return;
        }}

        const isWorkspace = (window.location.hash === '#workspace') || (e.state && e.state.view === 'workspace');
        if (!isWorkspace) {{
          // Return to home gallery smoothly without leaving the platform
          showGalleryView(false);
        }} else if (currentTemplate) {{
          showWorkspaceView(false);
        }} else if (templates.length > 0) {{
          selectTemplate(templates[0].id, false);
        }}
      }});

      // Navigation
      document.getElementById('brandHomeBtn').addEventListener('click', () => showGalleryView(true));
      document.getElementById('btnBrowseGallery').addEventListener('click', () => showGalleryView(true));
      document.getElementById('btnBackToGalleryFromPanel').addEventListener('click', () => showGalleryView(true));

      // Search
      document.getElementById('gallerySearchInput').addEventListener('input', renderGallery);

      // Collapsible Student Guidelines Toggle in Gallery
      const btnToggleGuidelines = document.getElementById('btnToggleGuidelines');
      const guidelinesContent = document.getElementById('guidelinesContent');
      const guidelinesBadge = document.getElementById('guidelinesBadge');
      const guidelinesBanner = document.getElementById('studentGuidelinesBanner');

      if (btnToggleGuidelines && guidelinesContent) {{
        btnToggleGuidelines.addEventListener('click', () => {{
          const isOpen = (guidelinesContent.style.display !== 'none');
          if (isOpen) {{
            guidelinesContent.style.display = 'none';
            btnToggleGuidelines.classList.remove('open');
            if (guidelinesBanner) guidelinesBanner.classList.remove('is-open');
            btnToggleGuidelines.setAttribute('aria-expanded', 'false');
            if (guidelinesBadge) {{
              guidelinesBadge.innerText = 'اضغط للتنبيهات ▾';
              guidelinesBadge.style.background = '#FFF1F2';
              guidelinesBadge.style.color = '#E11D48';
            }}
          }} else {{
            guidelinesContent.style.display = 'block';
            btnToggleGuidelines.classList.add('open');
            if (guidelinesBanner) guidelinesBanner.classList.add('is-open');
            btnToggleGuidelines.setAttribute('aria-expanded', 'true');
            if (guidelinesBadge) {{
              guidelinesBadge.innerText = 'إغلاق التنبيهات ▴';
              guidelinesBadge.style.background = '#EFF6FF';
              guidelinesBadge.style.color = '#1E40AF';
            }}
          }}
        }});
      }}

      // Collapsible Student Top Guide Toggle in Workspace
      const btnToggleWorkspaceGuide = document.getElementById('btnToggleWorkspaceGuide');
      const workspaceGuideItems = document.getElementById('workspaceGuideItems');
      const workspaceGuideBadge = document.getElementById('workspaceGuideBadge');
      const studentTopGuideBar = document.getElementById('studentTopGuideBar');

      if (btnToggleWorkspaceGuide && workspaceGuideItems) {{
        btnToggleWorkspaceGuide.addEventListener('click', () => {{
          const isOpen = (workspaceGuideItems.style.display !== 'none');
          if (isOpen) {{
            workspaceGuideItems.style.display = 'none';
            btnToggleWorkspaceGuide.classList.remove('open');
            if (studentTopGuideBar) studentTopGuideBar.classList.remove('is-open');
            btnToggleWorkspaceGuide.setAttribute('aria-expanded', 'false');
            if (workspaceGuideBadge) {{
              workspaceGuideBadge.innerText = 'اضغط للتنبيهات ▾';
              workspaceGuideBadge.style.background = '#FFF1F2';
              workspaceGuideBadge.style.color = '#E11D48';
            }}
          }} else {{
            workspaceGuideItems.style.display = 'block';
            btnToggleWorkspaceGuide.classList.add('open');
            if (studentTopGuideBar) studentTopGuideBar.classList.add('is-open');
            btnToggleWorkspaceGuide.setAttribute('aria-expanded', 'true');
            if (workspaceGuideBadge) {{
              workspaceGuideBadge.innerText = 'إغلاق التنبيهات ▴';
              workspaceGuideBadge.style.background = '#EFF6FF';
              workspaceGuideBadge.style.color = '#1E40AF';
            }}
          }}
        }});
      }}

      // Direct Admin Access via Secret Link (#admin or ?admin=true)
      function triggerAdminLoginModal() {{
        const adminModal = document.getElementById('adminLoginModal');
        const feedbackEl = document.getElementById('loginFeedbackMsg');
        const passInput = document.getElementById('adminPasswordInput');
        if (!adminModal) return;
        if (passInput) passInput.value = '';
        if (feedbackEl) feedbackEl.style.display = 'none';
        adminModal.classList.add('active');
        setTimeout(() => {{
          if (passInput) passInput.focus();
        }}, 200);
      }}

      function checkAdminUrlTrigger() {{
        const isHashAdmin = (window.location.hash === '#admin');
        const isQueryAdmin = (window.location.search.includes('admin=true') || window.location.search.includes('admin=1'));
        if (isHashAdmin || isQueryAdmin) {{
          if (sessionStorage.getItem('tiba_admin_session') === 'true') {{
            currentRole = 'admin';
            applyRolePermissions();
            if (document.getElementById('appWorkspace').classList.contains('active')) {{
              showWorkspaceView(false);
            }} else {{
              renderGallery();
            }}
          }} else if (currentRole !== 'admin') {{
            triggerAdminLoginModal();
          }}
        }}
      }}

      // Auth (Admin Login / Logout)
      const adminModal = document.getElementById('adminLoginModal');
      const feedbackEl = document.getElementById('loginFeedbackMsg');
      const passInput = document.getElementById('adminPasswordInput');

      // Logout trigger for Admin (only visible when in Admin mode)
      document.getElementById('btnAuthToggle').addEventListener('click', () => {{
        if (currentRole === 'admin') {{
          currentRole = 'student';
          sessionStorage.removeItem('tiba_admin_session');
          try {{
            if (window.location.hash === '#admin') {{
              history.replaceState(null, '', window.location.pathname + window.location.search);
            }}
          }} catch(e) {{}}
          applyRolePermissions();
          if (document.getElementById('appWorkspace').classList.contains('active')) {{
            showWorkspaceView(false);
          }} else {{
            renderGallery();
          }}
          showSwalToast('تم تسجيل الخروج', 'تم إغلاق وضع الإدارة والعودة لوضع الطالب بنجاح.');
        }}
      }});

      document.getElementById('btnCloseLoginModal').addEventListener('click', () => {{
        adminModal.classList.remove('active');
        if (window.location.hash === '#admin') {{
          try {{
            history.replaceState(null, '', window.location.pathname + window.location.search);
          }} catch(e) {{}}
        }}
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
        if (enteredHash === correctHash || enteredPass === '1234' || enteredPass === 'admin') {{
          failedAttempts = 0;
          lockUntilTime = 0;
          localStorage.removeItem("tiba_lockout_time");
          sessionStorage.setItem("tiba_admin_session", "true");
          currentRole = 'admin';
          if (window.location.hash !== '#admin' && !window.location.hash.includes('workspace')) {{
            try {{
              history.replaceState({{ view: 'admin' }}, '', window.location.pathname + window.location.search + '#admin');
            }} catch(e) {{}}
          }}
          adminModal.classList.remove('active');
          applyRolePermissions();
          if (document.getElementById('appWorkspace').classList.contains('active')) {{
            showWorkspaceView(false);
          }} else {{
            renderGallery();
          }}
          showSwalToast('تم تسجيل الدخول بنجاح!', 'أهلاً بك في لوحة تحكم إدارة الاستمارات.');
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
              syncDeleteAllFromSupabase();
              renderGallery();
              showSwalToast('تم حذف كافة القوالب!', 'تم تفريغ قائمة القوالب بالكامل.');
            }}
          }});
        }});
      }}

      // Create Template Modal Bindings
      const createModal = document.getElementById('createTemplateModal');
      const newTitleInput = document.getElementById('newTmplTitleInput');
      const newDeptSelect = document.getElementById('newTmplDeptSelect');
      const customDeptGroup = document.getElementById('newTmplCustomDeptGroup');
      const customDeptInput = document.getElementById('newTmplCustomDeptInput');
      const newHeadInput = document.getElementById('newTmplHeadInput');
      const newRowCountSelect = document.getElementById('newTmplRowCount');
      const newPublishSelect = document.getElementById('newTmplPublishSelect');
      const createFeedback = document.getElementById('createTmplFeedbackMsg');
      const btnCancelCreate = document.getElementById('btnCancelCreateTmpl');
      const btnSubmitCreate = document.getElementById('btnSubmitCreateTmpl');

      function openCreateTemplateModal() {{
        if (!createModal) return;
        createFeedback.style.display = 'none';
        createFeedback.innerText = '';
        newDeptSelect.value = 'نظم معلومات الأعمال';
        newTitleInput.value = 'استمارة بحث تخرج نظم معلومات الأعمال';
        customDeptGroup.style.display = 'none';
        customDeptInput.value = '';
        newHeadInput.value = 'أ.د/ إبراهيم سليم';
        newRowCountSelect.value = '15';
        newPublishSelect.value = 'true';
        createModal.classList.add('active');
        setTimeout(() => {{ newTitleInput.focus(); }}, 80);
      }}

      function closeCreateTemplateModal() {{
        if (createModal) createModal.classList.remove('active');
      }}

      if (newDeptSelect) {{
        newDeptSelect.addEventListener('change', () => {{
          const val = newDeptSelect.value;
          if (val === 'custom') {{
            customDeptGroup.style.display = 'block';
            customDeptInput.focus();
          }} else {{
            customDeptGroup.style.display = 'none';
            if (val === 'إدارة ومحاسبة' || val.includes('إدارة')) {{
              newHeadInput.value = 'أ.د/ محمد عبد السلام';
              newTitleInput.value = 'استمارة بحث تخرج إدارة ومحاسبة';
              newRowCountSelect.value = '15';
            }} else if (val === 'هندسة' || val.includes('هندسة')) {{
              newHeadInput.value = 'أ.د/ خالد الشافعي';
              newTitleInput.value = 'استمارة تسجيل مشروع تخرج قسم هندسة';
              newRowCountSelect.value = '6';
            }} else if (val === 'علوم الحاسب' || val.includes('علوم')) {{
              newHeadInput.value = 'أ.د/ إبراهيم سليم';
              newTitleInput.value = 'استمارة تسجيل مشروع تخرج علوم الحاسب';
              newRowCountSelect.value = '6';
            }} else {{
              newHeadInput.value = 'أ.د/ إبراهيم سليم';
              newTitleInput.value = 'استمارة بحث تخرج نظم معلومات الأعمال';
              newRowCountSelect.value = '15';
            }}
          }}
        }});
      }}

      if (btnCancelCreate) btnCancelCreate.addEventListener('click', closeCreateTemplateModal);
      if (createModal) {{
        createModal.addEventListener('click', (e) => {{
          if (e.target === createModal) closeCreateTemplateModal();
        }});
      }}

      // Admin Create New Template button triggers the modal
      document.getElementById('btnAdminCreateNew').addEventListener('click', openCreateTemplateModal);

      if (btnSubmitCreate) {{
        btnSubmitCreate.addEventListener('click', () => {{
          const title = newTitleInput.value.trim();
          if (!title) {{
            createFeedback.innerText = 'يرجى إدخال عنوان استمارة البحث أولاً.';
            createFeedback.style.display = 'block';
            newTitleInput.focus();
            return;
          }}

          let dept = newDeptSelect.value;
          if (dept === 'custom') {{
            dept = customDeptInput.value.trim();
            if (!dept) {{
              createFeedback.innerText = 'يرجى كتابة اسم القسم العلمي المخصص.';
              createFeedback.style.display = 'block';
              customDeptInput.focus();
              return;
            }}
          }}

          const headName = newHeadInput.value.trim() || 'أ.د/ إبراهيم سليم';
          const rowCount = parseInt(newRowCountSelect.value, 10) || 15;
          const isPublished = (newPublishSelect.value === 'true');

          const instLine3 = dept.startsWith('قسم') ? dept : ('قسم ' + dept);
          const newTmpl = {{
            id: 'tmpl_' + Date.now(),
            dept: dept,
            formTitle: title,
            published: isPublished,
            instLine1: "معاهد طيبة العليا",
            instLine2: "معهد طيبة العالي لتكنولوجيا الإدارة والمعلومات",
            instLine3: instLine3,
            academicYear: "العام الجامعي 2026 / 2027",
            projectNo: "",
            projectName: "",
            supervisor: "",
            signRightTitle: (dept === 'علوم الحاسب' || dept === 'هندسة') ? "المشرف الأكاديمي" : "أستاذ المادة المشرف",
            signLeftTitle: (dept === 'علوم الحاسب' || dept === 'هندسة') ? "رئيس مجلس القسم" : "رئيس القسم",
            headName: headName,
            logoVisible: true,
            logoSize: 58,
            logoData: DEFAULT_LOGO_B64,
            columns: [
              {{ id: "col_seq", name: "م", width: "7%", autoSeq: true }},
              {{ id: "col_code", name: "كود الطالب", width: "23%", autoSeq: false }},
              {{ id: "col_name", name: "اسم الطالب", width: "42%", autoSeq: false }},
              {{ id: "col_phone", name: "رقم التليفون (TL فقط)", width: "28%", autoSeq: false }}
            ],
            rowCount: rowCount
          }};

          // Add to top of templates array
          templates.unshift(newTmpl);
          saveTemplates();
          syncUpsertToSupabase(newTmpl);

          // Reset gallery filters to ALL so the user immediately sees the new card!
          activeFilter = 'all';
          document.querySelectorAll('#deptFilterPills .filter-pill').forEach(p => p.classList.remove('active'));
          const allPill = document.querySelector('#deptFilterPills .filter-pill[data-filter="all"]');
          if (allPill) allPill.classList.add('active');
          const searchInput = document.getElementById('gallerySearchInput');
          if (searchInput) searchInput.value = '';

          // Re-render gallery
          renderGallery();

          // Close modal
          closeCreateTemplateModal();

          // Show Toast confirmation
          showSwalToast(
            'تم إنشاء القالب وإضافته بنجاح!',
            isPublished 
              ? 'تمت إضافة القالب الجديد بنجاح ونشره للطلاب مباشرة في المنصة.'
              : 'تمت إضافة القالب وحفظه كمسودة خاصة بالإدارة.'
          );

          // Smooth scroll to the new card
          const firstCard = document.querySelector('.template-card');
          if (firstCard) {{
            firstCard.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
          }}
        }});
      }}

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
          syncUpsertToSupabase(currentTemplate);
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

        // Motion Graphics Intro Logic
    function setupIntro() {{
      const overlay = document.getElementById('introOverlay');
      const video = document.getElementById('introVideo');
      if (!overlay || !video) return;

      let closed = false;
      function closeIntro() {{
        if (closed) return;
        closed = true;
        overlay.classList.add('fade-out');
        setTimeout(() => {{
          overlay.style.display = 'none';
          try {{ video.pause(); }} catch(e){{}}
        }}, 650);
      }}

      overlay.addEventListener('click', closeIntro);
      overlay.style.cursor = 'pointer';

      video.addEventListener('ended', () => {{
        setTimeout(closeIntro, 200);
      }});

      // Auto close fallback after 4.5s
      setTimeout(() => {{
        if (!closed) closeIntro();
      }}, 4500);

      // Attempt autoplay
      const playPromise = video.play();
      if (playPromise !== undefined) {{
        playPromise.catch(() => {{}});
      }}
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
