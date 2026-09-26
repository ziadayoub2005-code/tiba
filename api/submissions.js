// Vercel Serverless Function for Student Submissions
// Saves and retrieves graduation project submissions in Cloud DB

const DEFAULT_FIREBASE = process.env.FIREBASE_DATABASE_URL || "https://tiba-graduation-default-rtdb.firebaseio.com";

export default async function handler(req, res) {
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
      const resp = await fetch(`${firebaseUrl}/submissions.json`);
      if (resp.ok) {
        const data = await resp.json();
        // Convert object of submissions to array if needed
        let list = [];
        if (data && typeof data === "object") {
          list = Array.isArray(data) ? data : Object.values(data);
        }
        return res.status(200).json({ success: true, submissions: list });
      }
      return res.status(200).json({ success: true, submissions: [] });
    }

    if (req.method === "POST") {
      const submission = req.body;
      const subId = submission.id || "sub_" + Date.now();
      submission.id = subId;
      submission.submittedAt = submission.submittedAt || new Date().toISOString();

      const resp = await fetch(`${firebaseUrl}/submissions/${subId}.json`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: typeof submission === "string" ? submission : JSON.stringify(submission)
      });

      if (resp.ok) {
        const saved = await resp.json();
        return res.status(200).json({ success: true, submission: saved });
      }
      return res.status(500).json({ success: false, error: "Cloud database write error" });
    }

    if (req.method === "PATCH") {
      const { id, status, adminNotes } = req.body;
      if (!id) return res.status(400).json({ success: false, error: "Missing submission id" });

      const patchData = { status, adminNotes, reviewedAt: new Date().toISOString() };
      const resp = await fetch(`${firebaseUrl}/submissions/${id}.json`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(patchData)
      });

      if (resp.ok) {
        return res.status(200).json({ success: true });
      }
      return res.status(500).json({ success: false, error: "Failed to update status" });
    }

    if (req.method === "DELETE") {
      const { id } = req.query;
      if (!id) return res.status(400).json({ success: false, error: "Missing submission id" });

      const resp = await fetch(`${firebaseUrl}/submissions/${id}.json`, {
        method: "DELETE"
      });

      if (resp.ok) {
        return res.status(200).json({ success: true });
      }
      return res.status(500).json({ success: false, error: "Failed to delete" });
    }

    res.status(405).json({ error: "Method not allowed" });
  } catch (err) {
    res.status(500).json({ success: false, error: err.message });
  }
}
