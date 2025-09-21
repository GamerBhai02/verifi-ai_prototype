from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

MOCK_RESPONSES = {
    "fake_image": {
        "verdict":"Likely Fake",
        "score":86,
        "short_reason":"Image is misattributed; original photo is from 2018 and unrelated events. Multiple fact-checks indicate mismatch.",
        "manipulation_type":"Misattribution / Out-of-context image",
        "top_sources":[
            {"title":"BOOM Fact-Check: Viral image misattributed","snippet":"The image originally published in 2018 was reused to claim a 2024 event...","url":"https://www.boomlive.in/example","date":"2019-05-10"},
            {"title":"AltNews: Context for viral claim","snippet":"This footage is older and not connected to the claim being spread...","url":"https://www.altnews.in/example","date":"2019-05-11"}
        ],
        "micro_lesson":"Check image origin (reverse image search), verify dates, and cross-check with reputable outlets."
    },
    "true_news": {
        "verdict":"Likely Real",
        "score":12,
        "short_reason":"Multiple reputable outlets report same facts and official statement corroborates event.",
        "manipulation_type":"N/A",
        "top_sources":[
            {"title":"The Hindu: Coverage of event","snippet":"Official statement and multiple on-ground reports confirm the event...","url":"https://www.thehindu.com/example","date":"2024-08-01"}
        ],
        "micro_lesson":"Cross-check across trusted outlets and prefer primary official sources."
    },
    "unclear": {
        "verdict":"Unclear",
        "score":50,
        "short_reason":"Insufficient evidence in the available sources; no verified fact-check found.",
        "manipulation_type":"Possible out-of-context or incomplete claim",
        "top_sources":[
            {"title":"No direct fact-check found","snippet":"No matching fact-check or reliable report was found for this exact claim.","url":"", "date":""}
        ],
        "micro_lesson":"Look for original sources, timestamps, and multiple independent confirmations before sharing."
    }
}

@app.route('/analyze', methods=['POST'])
def analyze():
    body = request.get_json() or {}
    text = (body.get('input_text') or "").lower()
    if "infertility" in text or "fakeimage" in text or "misattributed" in text or "vaccine causes infertility" in text:
        chosen = MOCK_RESPONSES['fake_image']
    elif "the hindu" in text or "confirmed by" in text or "official statement" in text:
        chosen = MOCK_RESPONSES['true_news']
    else:
        chosen = MOCK_RESPONSES['unclear']
    return jsonify({
        "interaction_id": str(uuid.uuid4()),
        "input_text": body.get('input_text'),
        "result": chosen
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status":"ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
