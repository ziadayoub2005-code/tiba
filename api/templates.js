// Vercel Serverless Function for Templates Management
// Supports Firebase Realtime Database forwarding or direct JSON storage

const DEFAULT_FIREBASE = process.env.FIREBASE_DATABASE_URL || "https://tiba-graduation-default-rtdb.firebaseio.com";

export default async function handler(req, res) {
  // Enable CORS
  res.setHeader("Access-Control-Allow-Credentials", true);
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET,OPTIONS,PATCH,DELETE,POST,PUT");
  res.setHeader(
    "Access-Control-Allow-Headers",
    "X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version"
  );

  if (req.method === "OPTIONS") {
    res.status(200).end();
    return;
  }

  const firebaseUrl = (process.env.FIREBASE_DATABASE_URL || DEFAULT_FIREBASE).replace(/\/$/, "");

  try {
    if (req.method === "GET") {
      const resp = await fetch(`${firebaseUrl}/templates.json`);
      if (resp.ok) {
        const data = await resp.json();
        return res.status(200).json({ success: true, templates: data || [] });
      }
      return res.status(200).json({ success: true, templates: [] });
    }

    if (req.method === "POST" || req.method === "PUT") {
      const body = req.body;
      const resp = await fetch(`${firebaseUrl}/templates.json`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: typeof body === "string" ? body : JSON.stringify(body)
      });
      if (resp.ok) {
        const saved = await resp.json();
        return res.status(200).json({ success: true, data: saved });
      }
      return res.status(500).json({ success: false, error: "Failed to save to cloud database" });
    }

    res.status(405).json({ error: "Method not allowed" });
  } catch (err) {
    res.status(500).json({ success: false, error: err.message });
  }
}
