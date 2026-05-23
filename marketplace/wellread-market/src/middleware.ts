import { clerkMiddleware, createRouteMatcher, auth } from '@clerk/nextjs/server'
import { NextResponse } from 'next/server'

const isProtectedRoute = createRouteMatcher(['/seller(.*)'])

export default clerkMiddleware(async (authHelper, req) => {
  if (isProtectedRoute(req)) {
    const { userId } = await authHelper()
    if (!userId) {
      const signInUrl = new URL('/sign-in', req.url)
      signInUrl.searchParams.set('redirect_url', req.url)
      return NextResponse.redirect(signInUrl)
    }
  }
})

export const config = {
  matcher: ['/((?!.+\\.[\\w]+$|_next).*)', '/', '/(api|trpc)(.*)'],
}
