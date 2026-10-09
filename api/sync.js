// Vercel Serverless Function for Sync & Health
const DEFAULT_FIREBASE = process.env.FIREBASE_DATABASE_URL || "https://tiba-graduation-default-rtdb.firebaseio.com";

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Credentials", true);
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET,OPTIONS,POST");
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
      const start = Date.now();
      const resp = await fetch(`${firebaseUrl}/health.json`);
      const latency = Date.now() - start;
      return res.status(200).json({
        success: true,
        online: resp.ok,
        latencyMs: latency,
        provider: "firebase-rtdb",
        endpoint: firebaseUrl
      });
    }

    if (req.method === "POST") {
      // Test custom URL
      const { testUrl } = req.body || {};
      const target = (testUrl || firebaseUrl).replace(/\/$/, "");
      const start = Date.now();
      const resp = await fetch(`${target}/.json?shallow=true`);
      const latency = Date.now() - start;
      return res.status(200).json({
        success: resp.ok,
        statusCode: resp.status,
        latencyMs: latency,
        target
      });
    }

    res.status(405).json({ error: "Method not allowed" });
  } catch (err) {
    res.status(500).json({ success: false, error: err.message });
  }
}
