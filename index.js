/**
 * v0 by Vercel.
 * @see https://v0.dev/t/QdkbHmmFHxj
 */
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Badge } from '@/components/ui/badge';
import { CardHeader, CardContent, Card } from '@/components/ui/card';
import { Avatar } from '@/components/ui/avatar';

export default function Component () {
  return (
    <div className='w-full h-full p-6 lg:p-10 bg-[#f5f5f5]'>
      <header className='flex items-center justify-between'>
        <h1 className='text-4xl font-bold'>Welcome to Study Buddy!</h1>
        <div className='flex items-center space-x-4'>
          <Button variant='outline'>Log in</Button>
          <Button>Sign Up</Button>
        </div>
      </header>
      <main className='mt-10'>
        <div className='mb-8'>
          <h2 className='text-2xl font-semibold mb-4'>Find your study partner</h2>
          <div className='flex w-full max-w-md items-center space-x-2'>
            <Input placeholder='Search...' type='search' />
            <Button type='submit'>
              <MicroscopeIcon className='w-4 h-4' />
            </Button>
          </div>
        </div>
        <div>
          <h2 className='text-2xl font-semibold mb-4'>Featured Study Groups</h2>
          <div className='grid grid-cols-1 md:grid-cols-2 gap-6'>
            <Card className='rounded-lg shadow-md'>
              <CardHeader className='bg-[#ffffff] p-4'>
                <h3 className='text-xl font-semibold'>Data Science Club</h3>
                <Badge className='mt-2' variant='secondary'>
                  Data Science
                </Badge>
              </CardHeader>
              <CardContent className='p-4'>
                <p className='text-gray-600'>
                  This group focuses on learning data science through collaboration and projects.
                </p>
                <div className='flex items-center mt-4'>
                  <Avatar className='w-10 h-10' src='/placeholder.svg?height=40&width=40' />
                  <p className='ml-2 text-gray-500'>Created by John Doe</p>
                </div>
              </CardContent>
            </Card>
            <Card className='rounded-lg shadow-md'>
              <CardHeader className='bg-[#ffffff] p-4'>
                <h3 className='text-xl font-semibold'>AI Enthusiasts</h3>
                <Badge className='mt-2' variant='secondary'>
                  Artificial Intelligence
                </Badge>
              </CardHeader>
              <CardContent className='p-4'>
                <p className='text-gray-600'>Join us to discuss the latest in AI and machine learning developments.</p>
                <div className='flex items-center mt-4'>
                  <Avatar className='w-10 h-10' src='/placeholder.svg?height=40&width=40' />
                  <p className='ml-2 text-gray-500'>Created by Jane Smith</p>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </main>
    </div>
  );
}

function MicroscopeIcon (props) {
  return (
    <svg
      {...props}
      xmlns='http://www.w3.org/2000/svg'
      width='24'
      height='24'
      viewBox='0 0 24 24'
      fill='none'
      stroke='currentColor'
      strokeWidth='2'
      strokeLinecap='round'
      strokeLinejoin='round'
    >
      <path d='M6 18h8' />
      <path d='M3 22h18' />
      <path d='M14 22a7 7 0 1 0 0-14h-1' />
      <path d='M9 14h2' />
      <path d='M9 12a2 2 0 0 1-2-2V6h6v4a2 2 0 0 1-2 2Z' />
      <path d='M12 6V3a1 1 0 0 0-1-1H9a1 1 0 0 0-1 1v3' />
    </svg>
  );
}
