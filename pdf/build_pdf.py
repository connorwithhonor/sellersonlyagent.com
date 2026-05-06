#!/usr/bin/env python3
"""Sellers Only Agent - Five Questions Checklist PDF"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Colors from SOA design system
BG = HexColor('#0b0b0f')
BG_CARD = HexColor('#1a1a22')
GOLD = HexColor('#c9a84c')
GOLD_BRIGHT = HexColor('#e8c76a')
GOLD_DIM = HexColor('#8a7230')
TEXT = HexColor('#eae7de')
TEXT_DIM = HexColor('#a8a498')
TEXT_MUTED = HexColor('#706c60')
BORDER = HexColor('#2a2a35')

# Try to register serif and sans fonts if available
SERIF = 'Times-Bold'
SERIF_ITALIC = 'Times-Italic'
SERIF_REG = 'Times-Roman'
SANS = 'Helvetica'
SANS_BOLD = 'Helvetica-Bold'

OUT = '/home/claude/soa-build/pdf/five-questions-listing-agent-checklist.pdf'
os.makedirs(os.path.dirname(OUT), exist_ok=True)

# Two-page checklist: front = branded cover + intro, back = 5 questions
PAGE_W, PAGE_H = letter  # 612 x 792

c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle("Five Questions Every Seller Should Ask Their Listing Agent")
c.setAuthor("Connor MacIvor, Sellers Only Agent(TM)")
c.setSubject("Fiduciary duty checklist for home sellers")
c.setKeywords("listing agent, fiduciary duty, seller's agent, real estate, checklist, Santa Clarita")

def fill_bg():
    c.setFillColor(BG)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

def draw_gold_line(x, y, w, thickness=1.2):
    c.setStrokeColor(GOLD)
    c.setLineWidth(thickness)
    c.line(x, y, x + w, y)

def draw_border_line(x, y, w, thickness=0.5):
    c.setStrokeColor(BORDER)
    c.setLineWidth(thickness)
    c.line(x, y, x + w, y)

# ========== PAGE 1: COVER / INTRO ==========
fill_bg()

# Top kicker
c.setFillColor(GOLD)
c.setFont(SANS_BOLD, 9)
c.drawString(0.75*inch, PAGE_H - 0.75*inch, "SELLERS ONLY AGENT\u2122   \u00b7   FIDUCIARY DUTY CHECKLIST")

# Gold divider
draw_gold_line(0.75*inch, PAGE_H - 0.85*inch, PAGE_W - 1.5*inch, thickness=1.5)

# Title
c.setFillColor(TEXT)
c.setFont(SERIF, 28)
title_y = PAGE_H - 1.7*inch
c.drawString(0.75*inch, title_y, "Five Questions")
c.drawString(0.75*inch, title_y - 36, "Every Seller Should Ask")
c.drawString(0.75*inch, title_y - 72, "Their Listing Agent")

# Subtitle
c.setFillColor(TEXT_DIM)
c.setFont(SERIF_ITALIC, 14)
c.drawString(0.75*inch, title_y - 110, "Your agent's loyalty should be measurable,")
c.drawString(0.75*inch, title_y - 130, "not assumed. Bring this to every interview.")

# Intro box
box_y = PAGE_H - 4.3*inch
box_h = 2.2*inch
c.setFillColor(BG_CARD)
c.setStrokeColor(BORDER)
c.setLineWidth(0.5)
c.rect(0.75*inch, box_y, PAGE_W - 1.5*inch, box_h, fill=1, stroke=1)

# Gold accent bar on left of box
c.setFillColor(GOLD)
c.rect(0.75*inch, box_y, 0.06*inch, box_h, fill=1, stroke=0)

# Box contents
c.setFillColor(GOLD)
c.setFont(SANS_BOLD, 9)
c.drawString(1.0*inch, box_y + box_h - 24, "WHY THIS MATTERS")

c.setFillColor(TEXT)
c.setFont(SERIF_REG, 11)
intro_lines = [
    "In California, your listing agent owes you a fiduciary duty.",
    "Loyalty. Full disclosure. Your financial interest above theirs,",
    "above their friends, above anyone they might owe a favor to.",
    "",
    "That duty is clear on paper. The problem is how quietly it can",
    "be bent by networking groups, referral clubs, and relationship",
    "reciprocity most sellers never see.",
    "",
    "These five questions are designed to make the invisible visible.",
    "Ask them before you sign a listing agreement.",
    "Ask them in writing when you can. Watch how they answer."
]
ly = box_y + box_h - 48
for line in intro_lines:
    c.drawString(1.0*inch, ly, line)
    ly -= 16

# How to use
c.setFillColor(GOLD)
c.setFont(SANS_BOLD, 9)
c.drawString(0.75*inch, 2.4*inch, "HOW TO USE THIS CHECKLIST")

c.setFillColor(TEXT_DIM)
c.setFont(SERIF_REG, 11)
use_lines = [
    "1.  Print this page and the next.",
    "2.  Bring it to every listing interview.",
    "3.  Ask the questions in order. Let the agent answer each fully.",
    "4.  Write down what they said, or record the answer with permission.",
    "5.  Hire the agent whose process, not whose reflex, matches these standards."
]
uy = 2.2*inch
for line in use_lines:
    c.drawString(0.75*inch, uy, line)
    uy -= 16

# Footer
draw_border_line(0.75*inch, 0.85*inch, PAGE_W - 1.5*inch)
c.setFillColor(TEXT_MUTED)
c.setFont(SANS, 8)
c.drawString(0.75*inch, 0.65*inch, "Connor MacIvor  \u00b7  DRE #01238257  \u00b7  661-400-1720  \u00b7  sellersonlyagent.com")
c.drawRightString(PAGE_W - 0.75*inch, 0.65*inch, "Page 1 of 2")
c.setFillColor(GOLD_DIM)
c.setFont(SERIF_ITALIC, 8)
c.drawString(0.75*inch, 0.5*inch, "SYNC Brokerage  \u00b7  Flat $17,000 fee per listing  \u00b7  Undivided focus")

c.showPage()

# ========== PAGE 2: THE FIVE QUESTIONS ==========
fill_bg()

# Top strip
c.setFillColor(GOLD)
c.setFont(SANS_BOLD, 9)
c.drawString(0.75*inch, PAGE_H - 0.75*inch, "THE FIVE QUESTIONS")
draw_gold_line(0.75*inch, PAGE_H - 0.85*inch, PAGE_W - 1.5*inch, thickness=1.5)

questions = [
    {
        "num": "01",
        "q": "Will you present every written offer to me within 24 hours, in writing, with numbers and terms first and commentary separate?",
        "why": "Removes verbal framing from the initial presentation. You see the raw offer, then the analysis. You decide the weight."
    },
    {
        "num": "02",
        "q": "Do you have any referral, co-marketing, or compensation relationships with buyer's agents who may bring offers on my property?",
        "why": "Creates a written disclosure record before the offer arrives. Any undisclosed arrangement surfaces up front."
    },
    {
        "num": "03",
        "q": "Will my property hit the MLS and syndicate publicly before any private network, coming-soon list, or pocket-listing channel?",
        "why": "More buyers means more competition means higher price. Pocket listings reduce buyer pool, which reduces sale price."
    },
    {
        "num": "04",
        "q": "If a stronger offer comes from a buyer's agent you have never met, will you present it with the same energy as one from your closest referral partner, and what process ensures that?",
        "why": "The follow-up process reveals whether the answer is a reflex or a practice. Practice is what you can trust."
    },
    {
        "num": "05",
        "q": "Will you put in writing that you will not accept referral fees, kickbacks, or co-marketing benefits tied to the buyer's agent on this transaction?",
        "why": "Clean agents sign without blinking. An agent who needs to negotiate this clause is telling you where their revenue comes from."
    }
]

y = PAGE_H - 1.15*inch

for qd in questions:
    # Card background
    card_h = 1.15*inch
    c.setFillColor(BG_CARD)
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.rect(0.75*inch, y - card_h, PAGE_W - 1.5*inch, card_h, fill=1, stroke=1)

    # Gold left bar
    c.setFillColor(GOLD)
    c.rect(0.75*inch, y - card_h, 0.06*inch, card_h, fill=1, stroke=0)

    # Number
    c.setFillColor(GOLD_DIM)
    c.setFont(SERIF, 11)
    c.drawString(0.98*inch, y - 16, qd["num"])

    # Checkbox
    c.setStrokeColor(GOLD)
    c.setLineWidth(1)
    box_size = 10
    c.rect(PAGE_W - 0.98*inch - box_size, y - 16, box_size, box_size, fill=0, stroke=1)

    # Question text (wrap)
    c.setFillColor(TEXT)
    c.setFont(SERIF, 11.5)
    q_text = qd["q"]
    # naive wrap
    words = q_text.split()
    lines = []
    cur = ""
    max_chars = 78
    for w in words:
        if len(cur) + len(w) + 1 <= max_chars:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur)
            cur = w
    if cur: lines.append(cur)

    qy = y - 34
    for ln in lines[:3]:
        c.drawString(0.98*inch, qy, ln)
        qy -= 14

    # Why (italic, dim)
    c.setFillColor(TEXT_DIM)
    c.setFont(SERIF_ITALIC, 9.5)
    why_text = qd["why"]
    words = why_text.split()
    lines = []
    cur = ""
    max_chars = 90
    for w in words:
        if len(cur) + len(w) + 1 <= max_chars:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur)
            cur = w
    if cur: lines.append(cur)

    why_y = y - card_h + 20
    for ln in lines[:2]:
        c.drawString(0.98*inch, why_y, ln)
        why_y += 11

    y -= card_h + 10

# Bottom callout box
cb_y = 0.95*inch
cb_h = 0.9*inch
c.setFillColor(BG_CARD)
c.setStrokeColor(GOLD_DIM)
c.setLineWidth(1)
c.rect(0.75*inch, cb_y, PAGE_W - 1.5*inch, cb_h, fill=1, stroke=1)

c.setFillColor(GOLD)
c.setFont(SERIF, 13)
c.drawString(0.95*inch, cb_y + cb_h - 22, "The Standard, Not A Trap")

c.setFillColor(TEXT)
c.setFont(SERIF_REG, 10)
c.drawString(0.95*inch, cb_y + cb_h - 40, "You do not need a flat-fee agent to benefit from these questions.")
c.drawString(0.95*inch, cb_y + cb_h - 54, "Any seller, working with any agent, can ask them and expect honest answers.")

c.setFillColor(GOLD_BRIGHT)
c.setFont(SERIF_ITALIC, 10)
c.drawString(0.95*inch, cb_y + 12, "Ask the questions. Listen to the answers. Hire accordingly.")

# Footer
c.setFillColor(TEXT_MUTED)
c.setFont(SANS, 8)
c.drawString(0.75*inch, 0.65*inch, "Connor MacIvor  \u00b7  DRE #01238257  \u00b7  661-400-1720  \u00b7  sellersonlyagent.com")
c.drawRightString(PAGE_W - 0.75*inch, 0.65*inch, "Page 2 of 2")
c.setFillColor(GOLD_DIM)
c.setFont(SERIF_ITALIC, 8)
c.drawString(0.75*inch, 0.5*inch, "\u00a9 2026 Sellers Only Agent\u2122  \u00b7  SYNC Brokerage  \u00b7  Print freely. Share freely. Use it.")

c.save()
print(f"PDF saved: {OUT}")
print(f"Size: {os.path.getsize(OUT)} bytes")
