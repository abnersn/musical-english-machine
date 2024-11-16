import { StepProps } from './types';

export default function Step({ title, complete, children }: StepProps) {
  if (complete) {
    return (
      <section>
        <h2>{title}</h2>
        👍 Completo
      </section>
    );
  }
  return (
    <section>
      <h2>{title}</h2>
      {children}
    </section>
  );
}
