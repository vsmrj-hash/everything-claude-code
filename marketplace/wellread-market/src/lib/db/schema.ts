import { pgTable, uuid, text, integer, decimal, boolean, timestamp, pgEnum } from 'drizzle-orm/pg-core'

export const listingStatusEnum = pgEnum('listing_status', ['draft', 'active', 'archived'])
export const orderStatusEnum = pgEnum('order_status', ['pending', 'paid', 'fulfilled', 'refunded'])

export const listings = pgTable('listings', {
  id: uuid('id').primaryKey().defaultRandom(),
  sellerId: text('seller_id').notNull(),
  title: text('title').notNull(),
  description: text('description').notNull(),
  price: decimal('price', { precision: 10, scale: 2 }).notNull(),
  category: text('category').notNull(),
  coverUrl: text('cover_url'),
  fileUrl: text('file_url'),
  previewUrl: text('preview_url'),
  pageCount: integer('page_count'),
  authorName: text('author_name').notNull(),
  status: listingStatusEnum('status').default('active'),
  featured: boolean('featured').default(false),
  createdAt: timestamp('created_at').defaultNow(),
  updatedAt: timestamp('updated_at').defaultNow(),
})

export const orders = pgTable('orders', {
  id: uuid('id').primaryKey().defaultRandom(),
  buyerId: text('buyer_id').notNull(),
  listingId: uuid('listing_id').references(() => listings.id),
  stripeSessionId: text('stripe_session_id').unique(),
  stripePaymentIntentId: text('stripe_payment_intent_id'),
  amount: decimal('amount', { precision: 10, scale: 2 }).notNull(),
  status: orderStatusEnum('status').default('pending'),
  downloadUrl: text('download_url'),
  downloadExpiresAt: timestamp('download_expires_at'),
  createdAt: timestamp('created_at').defaultNow(),
})

export const reviews = pgTable('reviews', {
  id: uuid('id').primaryKey().defaultRandom(),
  listingId: uuid('listing_id').references(() => listings.id),
  reviewerId: text('reviewer_id').notNull(),
  reviewerName: text('reviewer_name').notNull(),
  rating: integer('rating').notNull(),
  comment: text('comment'),
  createdAt: timestamp('created_at').defaultNow(),
})
